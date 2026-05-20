# Architecture details

This document explains the flow of data in the AWS Bedrock Chatbot project.

## High-level flow

1. **User prompt**  
   The user types a prompt into a terminal, typically inside **AWS CloudShell**.

2. **Python script**  
   The `chat.py` script collects the prompt and appends it to an in-memory `history` list.

3. **Bedrock Runtime (Converse API)**  
   The script calls the Bedrock Runtime `converse` API, sending:
   - The configured **model ID**.
   - A **system prompt** that describes the assistant's behavior.
   - The full **conversation history** (all previous user and assistant messages).

4. **Model (for example Amazon Nova Lite)**  
   Amazon Bedrock forwards the request to the selected model. The model generates a response using the system prompt and the conversation history as context.

5. **AI response to user**  
   The Bedrock Runtime returns the model's response to the Python script, which then:
   - Prints the assistant's reply to the terminal.
   - Appends the assistant message to the `history` list.

This closely matches the diagram you provided: **AWS CloudShell → Python Script → Amazon Bedrock → Model (e.g., Amazon Nova Lite) → AI Response to user**.[conversation_history:19]

## Message format and roles

Messages sent to the Converse API use a consistent structure:

- Each message has a `role`: either `"user"` or `"assistant"`.
- Each message has a `content` list, which contains one or more blocks.
- For this project, each block is a simple text block.

Example structure for a user message:

```python
{
    "role": "user",
    "content": [{"text": "Explain Amazon Bedrock in simple terms."}],
}
```

Example structure for an assistant message:

```python
{
    "role": "assistant",
    "content": [{"text": "Amazon Bedrock is a fully managed service for building and scaling generative AI applications."}],
}
```

The script always sends the full list of messages so the model can maintain context across multiple turns.[web:9][web:15]

## Error handling

The `chat.py` script keeps error handling simple:

- If the `converse` call fails, the script prints an error message and keeps the loop running so you can try another prompt.
- The most common errors involve credentials, permissions, model access, or region configuration.

You can extend this project by adding more robust logging and metrics if you want to monitor usage in a production setting.
