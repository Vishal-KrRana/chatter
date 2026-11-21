
import os
from dotenv import load_dotenv
from src.providers.gemini_provider import GeminiProvider


def main():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("GEMINI_API_KEY is missing from .env")
        return

    provider = GeminiProvider(api_key)

    messages = [
        {
            "role": "user",
            "content": "Explain Python in two sentences."
        }
    ]

    print("Generating response...\n")
    response = provider.generate_response(messages)
    print("Gemini:", response)


if __name__ == "__main__":
    main()
