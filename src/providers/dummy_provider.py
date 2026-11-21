
from src.providers.base import AIProvider


class DummyProvider(AIProvider):

    def generate_response(self, messages: list[dict]) -> str:

        latest_message = messages[-1]["content"]

        return f"Dummy AI received: {latest_message}"
