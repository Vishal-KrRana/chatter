
class ChatSession:

    def __init__(self):
        self.messages = []

    def send_message(self, provider, user_input: str) -> str:
        self.messages.append({
            "role": "user",
            "content": user_input
        })

        try:
            response = provider.generate_response(self.messages)

        except Exception:
            # Remove the user message if generation raises an exception.
            self.messages.pop()
            raise

        self.messages.append({
            "role": "assistant",
            "content": response
        })

        return response

    def clear_history(self):
        self.messages.clear()

    def get_history(self):
        return self.messages.copy()

    def display_history(self):
       if not self.messages:
           print("No conversation history available.")
           return

       print("\n--- Conversation History ---")

       for message in self.messages:
           role = message["role"].capitalize()
           content = message["content"]

           print(f"\n{role}: {content}")

       print("\n----------------------------")
