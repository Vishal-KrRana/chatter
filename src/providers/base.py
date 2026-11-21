
from abc import ABC, abstractmethod


class AIProvider(ABC):

    @abstractmethod
    def generate_response(self, messages: list[dict]) -> str:
        """
        Generate a response using the selected AI model.

        messages: Conversation history
        returns: AI-generated response
        """
        pass

class ProviderError(Exception):
    """Raised when a AI provider fails to generate a response."""
    def __init__(self, message: str, status_code: int | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code
