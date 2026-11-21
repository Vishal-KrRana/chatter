
from src.providers.base import AIProvider
from src.providers.dummy_provider import DummyProvider


def main():

    provider = DummyProvider()

    messages = [
        {"role": "user", "content": "Hello AI"}
    ]

    response = provider.generate_response(messages)

    print(response)


if __name__ == "__main__":
    main()
