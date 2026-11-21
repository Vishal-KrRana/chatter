
from src.providers.ollama_provider import OllamaProvider


def main():

    provider = OllamaProvider()

    messages = [
        {
            "role": "user",
            "content": "Explain Python in two sentences."
        }
    ]

    print("Generating response...\n")

    response = provider.generate_response(messages)

    print("AI:", response)


if __name__ == "__main__":
    main()
