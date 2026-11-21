
from ollama import Client
from src.providers.base import AIProvider, ProviderError


class OllamaProvider(AIProvider):

    def __init__(
        self,
        model: str = "llama3.2:3b",
        host: str = "http://localhost:11434"
    ):
        self.model = model
        self.client = Client(host=host)



    def generate_response(self, messages: list[dict]) -> str:
        try:
            response = self.client.chat(
                model=self.model,
                messages=messages
            )

            content = response["message"]["content"]

            if not content:
                raise ProviderError("Ollama returned an empty response.")

            return content

        except ProviderError:
            raise

        except Exception as error:
            raise ProviderError(
                f"Ollama request failed: {type(error).__name__}: {error}"
            ) from error
