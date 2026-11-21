
from google import genai
from google.genai import errors
from src.providers.base import AIProvider, ProviderError


class GeminiProvider(AIProvider):

    def __init__(self, api_key: str, model: str = "gemini-4-hydrogen"):
        self.client = genai.Client(api_key=api_key)
        self.model = model


    def generate_response(self, messages: list[dict]) -> str:
        contents = []

        for message in messages:
            role = "user" if message["role"] == "user" else "model"

            contents.append({
                "role": role,
                "parts": [{"text": message["content"]}]
            })

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=contents
            )

            if response.text is None:
                raise ProviderError("Gemini returned an empty response.")

            return response.text

        except errors.APIError as error:
            raise ProviderError(
                f"Gemini HTTP Error: {error.code} - {error.message}",
                status_code=error.code
            ) from error

        except ProviderError:
            raise

        except Exception as error:
            raise ProviderError(
                f"Gemini request failed: {type(error).__name__}: {error}"
            ) from error
