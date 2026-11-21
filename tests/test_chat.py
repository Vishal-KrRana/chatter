

from src.chat import ChatSession
from src.providers.base import AIProvider


class MockProvider(AIProvider):

    def generate_response(self, messages: list[dict]) -> str:
        return "Mock response"


def test_send_message():
    session = ChatSession()
    provider = MockProvider()

    response = session.send_message(provider, "Hello")

    assert response == "Mock response"
    assert len(session.messages) == 2

    assert session.messages[0] == {
        "role": "user",
        "content": "Hello"
    }

    assert session.messages[1] == {
        "role": "assistant",
        "content": "Mock response"
    }


def test_clear_history():
    session = ChatSession()
    provider = MockProvider()

    session.send_message(provider, "Hello")
    session.clear_history()

    assert session.messages == []


def test_get_history():
    session = ChatSession()
    provider = MockProvider()

    session.send_message(provider, "Hello")

    history = session.get_history()

    assert len(history) == 2

import pytest
from src.providers.base import ProviderError


class FailingProvider(AIProvider):

    def generate_response(self, messages: list[dict]) -> str:
        raise ProviderError(
            "Connection failed",
            status_code=503
        )


def test_failed_message_is_not_saved():
    session = ChatSession()
    provider = FailingProvider()

    with pytest.raises(ProviderError) as error:
        session.send_message(provider, "Hello")

    assert error.value.status_code == 503
    assert session.messages == []
