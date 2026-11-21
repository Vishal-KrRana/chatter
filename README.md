
# Chatter: Multi Model AI Chatbot

A Python-based terminal chatbot that supports multiple AI providers, allowing users to interact with both locally hosted and cloud-based language models through a single command-line interface.

## Features

- **Multiple AI providers:** Supports Ollama for local inference and Google Gemini for cloud-based inference.
- **Provider switching:** Switch between supported providers during a conversation.
- **Conversation history:** Maintains conversation context during the current session.
- **API key management:** Add or update API keys directly through the `/add` command.
- **Error handling:** Handles API failures, connection errors, and empty responses.
- **Command-line interface:** Provides commands for model selection, history management, and application control.

## Technologies Used

- **Python 3** — Core programming language
- **Ollama** — Local AI model inference
- **Google Gemini API** — Cloud-based AI inference
- **Google Gen AI SDK** — Gemini API integration
- **python-dotenv** — Environment variable and API key management
- **pytest** — Automated testing

## Project Structure

```text
terminal-ai-chatbot/
├── src/
│   ├── main.py
│   ├── chat.py
│   └── providers/
│       ├── base.py
│       ├── ollama_provider.py
│       └── gemini_provider.py
├── tests/
│   ├── test_chat.py
│   └── test_providers.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or later
- Ollama installed for local model inference
- A downloaded Ollama model
- Gemini API key for cloud inference

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd chatter
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Local model setup

Install Ollama and download the model:

```bash
ollama pull llama3.2:3b
```

Start the Ollama server:

```bash
ollama serve
```

### Gemini configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Alternatively, start the chatbot and use `/add` to configure your API key.

## Usage

Start the application from the project root:

```bash
python -m src.main
```

### Available commands

| Command | Description |
|---|---|
| `/help` | Display available commands |
| `/exit` | Exit the application |
| `/clear` | Clear the terminal |
| `/models` | List available providers |
| `/use <provider>` | Switch AI provider |
| `/add` | Add or update an API key |
| `/history` | Display conversation history |
| `/clear-history` | Clear conversation history |

### Example

```text
You (ollama): Hello!
Chatter: Hello! How can I help you?

You (ollama): /use gemini
Switched to gemini (gemini-2.5-flash).

You (gemini): Explain REST APIs.
Chatter: ...
```

## Running Tests

Execute the test suite using:

```bash
pytest -v
```

## Architecture

The application uses a shared provider interface to abstract communication with different AI backends.

Both Ollama and Gemini implement the same `AIProvider` interface. This allows the chat session to interact with different models without depending on provider-specific implementation details.

The application separates terminal interaction, conversation management, and AI provider integration into distinct modules.

## Current Limitations

- Conversation history is stored in memory and is lost when the application exits.
- Only the configured Ollama and Gemini models are supported.
- Internet access is required for Gemini.
- Local inference performance depends on available system resources.

## Future Improvements

- Support additional AI providers.
- Add persistent conversation storage.
- Implement streaming responses.
- Allow users to configure different models dynamically.
