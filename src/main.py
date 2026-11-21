import os
import getpass
from src.providers.ollama_provider import OllamaProvider
from src.providers.gemini_provider import GeminiProvider
from src.providers.base import ProviderError
from dotenv import load_dotenv, set_key
from src.chat import ChatSession

def show_welcome():
    print("=" * 45)
    print("        Chatter: A MULTI-MODEL AI CHATBOT")
    print("=" * 45)
    print("Type /help to see available commands.")
    print("Type /exit to quit the application.")
    print()


def show_help():
    print("\nAvailable commands:")
    print("  /help          Show available commands")
    print("  /exit          Exit the application")
    print("  /clear         Clear the terminal")
    print("  /models        List supported models")
    print("  /use <model>   Switch active model")
    print("  /add           Add an API key")
    print("  /history       Show conversation history")
    print("  /clear-history Clear conversation history")
    print()



def handle_command(command, state, session):
    parts = command.split()
    cmd = parts[0]

    if cmd == "/help":
        show_help()

    elif cmd == "/exit":
        print("Goodbye!")
        return False

    elif cmd == "/clear":
        os.system("clear")

    elif cmd == "/models":
        print("\nAvailable models:")

        print("\n  Local:")
        print("    ollama - llama3.2:3b")

        print("\n  Cloud:")
        print("    gemini - gemini-4-hydrogen")

        print("\nActive configuration:")
        print(f"  Provider: {state['name']}")
        print(f"  Model:    {state['model']}")


    elif cmd == "/use":
        if len(parts) != 2:
            print("Usage: /use <provider>")
            return True

        name = parts[1].lower()

        if name == state["name"]:
            print(f"{name} is already active.")
            return True

        try:
            provider, model = create_provider(name)

            state["provider"] = provider
            state["name"] = name
            state["model"] = model

            print(f"Switched to {name} ({model}).")

        except ValueError as error:
            print(f"Error: {error}")

    elif cmd == "/add":
        if len(parts) != 1:
            print("Usage: /add")
            return True

        provider_name = input("Provider (gemini): ").strip().lower()

        if provider_name != "gemini":
            print("Currently, only Gemini API keys are supported.")
            return True

        api_key = getpass.getpass("Enter Gemini API key: ").strip()

        if not api_key:
            print("API key cannot be empty.")
            return True

        try:
            set_key(".env", "GEMINI_API_KEY", api_key)
            os.environ["GEMINI_API_KEY"] = api_key

            print("Gemini API key saved successfully.")

            # Refresh the provider if Gemini is currently active.
            if state["name"] == "gemini":
                provider, model = create_provider("gemini")
                state["provider"] = provider
                state["model"] = model
                print("Active Gemini provider updated.")

        except OSError as error:
            print(f"Failed to save API key: {error}")

    elif cmd == "/history":
        session.display_history()

    elif cmd == "/clear-history":
        session.clear_history()
        print("Conversation history cleared")

    else:
        print("Unknown command. Type /help for assistance.")

    return True

def create_provider(name):
    if name == "ollama":
        return OllamaProvider(), "llama3.2:3b"
    elif name == "gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Gemini API key not found. Use /add command to configure it.")
        return GeminiProvider(api_key=api_key), "gemini-4-hydrogen"
    else:
        raise ValueError(f"Unknown Provider: {name}")


def chat_loop():
    load_dotenv()

    show_welcome()

    state = {
        "name": "ollama",
        "model": "llama3.2:3b",
        "provider": OllamaProvider()
    }

    session = ChatSession()
    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                continue

            if user_input.startswith("/"):
                if not handle_command(user_input, state, session):
                    break

            else:
                try:
                    response = session.send_message(
                        state["provider"],
                        user_input
                    )
                    print(f"\nChatter: {response}")

                except ProviderError as error:
                    if error.status_code is not None:
                        print(f"\nError (HTTP {error.status_code}): {error}")
                    else:
                        print(f"\nError: {error}")

                except Exception as error:
                    print(f"\nUnexpected error: {type(error).__name__}: {error}")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

def main():
    chat_loop()


if __name__ == "__main__":
    main()
