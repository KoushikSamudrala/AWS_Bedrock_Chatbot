"""Simple multi-turn chatbot using Amazon Bedrock's Converse API.

This script is designed to be run from AWS CloudShell or a local terminal.
It maintains conversation history in memory so that the model can respond
with context across multiple turns.
"""

from bedrock_client import converse_with_bedrock


def format_user_message(text: str) -> dict:
    """Create a message dict in the format expected by the Converse API."""

    return {
        "role": "user",
        "content": [
            {
                "text": text,
            }
        ],
    }


def format_assistant_message(text: str) -> dict:
    """Create an assistant message dict for the conversation history."""

    return {
        "role": "assistant",
        "content": [
            {
                "text": text,
            }
        ],
    }


def main():
    print("=== AWS Bedrock CLI Chatbot ===")
    print("Type your message and press Enter.")
    print("Type 'exit' or 'quit' to end the chat.\n")

    # Conversation history as a list of messages
    history = []

    while True:
        user_input = input("You: ")

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        # Add the new user message to the history
        history.append(format_user_message(user_input))

        try:
            # Call Bedrock with the full history
            assistant_reply = converse_with_bedrock(history)
        except Exception as exc:  # Broad catch to keep CLI experience simple
            print("[Error calling Bedrock]:", exc)
            # Optionally, remove the last user message so it can be retried
            history.pop()
            continue

        # Add assistant reply to history and show it to the user
        history.append(format_assistant_message(assistant_reply))
        print(f"Assistant: {assistant_reply}\n")


if __name__ == "__main__":
    main()
