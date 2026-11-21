

import pytest

from src.main import create_provider
from src.providers.ollama_provider import OllamaProvider
from src.providers.gemini_provider import GeminiProvider


def test_create_ollama_provider():
    provider, model = create_provider("ollama")

    assert isinstance(provider, OllamaProvider)
    assert model == "llama3.2:3b"


def test_create_gemini_provider(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-api-key")

    provider, model = create_provider("gemini")

    assert isinstance(provider, GeminiProvider)
    assert model == "gemini-4-hydrogen"


def test_missing_gemini_api_key(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)

    with pytest.raises(ValueError, match="API key not found"):
        create_provider("gemini")


def test_unknown_provider():
    with pytest.raises(ValueError, match="Unknown Provider: unknown"):
        create_provider("unknown")
