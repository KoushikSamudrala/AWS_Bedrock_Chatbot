# AWS Bedrock Chatbot (Python CLI)

A simple, beginner-friendly chatbot built with **Python** and **Amazon Bedrock**. The chatbot runs in a terminal (for example, in **AWS CloudShell**) and talks to a single Amazon Bedrock model (such as **Amazon Nova Lite**) using the **Converse API** with multi-turn conversation history.

---

## 1. Project overview

This project lets you send prompts from a terminal to an Amazon Bedrock model and get AI responses back. Each question and answer is added to a conversation history, so the model can respond with context across multiple turns.

You can:
- Run the chatbot from AWS CloudShell or your local machine.
- Use a single Bedrock model configured in `config.py`.
- Customize the system prompt to control the assistant's behavior.
- Keep multi-turn chat history in memory for more contextual answers.

---

## 2. Architecture

At a high level, the data flow looks like this:

1. You type a **prompt** into the terminal (for example, in AWS CloudShell).
2. A **Python script** sends the prompt, along with previous messages, to **Amazon Bedrock** using the Converse API.
3. Amazon Bedrock forwards the request to the configured model (for example **Amazon Nova Lite**).
4. The model returns an AI-generated response, which is printed back to your terminal.

This maps to the diagram you provided: AWS CloudShell → Python script → Amazon Bedrock → model (e.g., Amazon Nova Lite) → AI response to user.

---

## 3. Prerequisites

Before running this project, make sure you have:

- An **AWS account** with access to **Amazon Bedrock** in at least one supported region.[web:15]
- **Model access enabled** (for example, **Amazon Nova Lite** or another Bedrock text model) in that region.[web:15]
- **Python 3.9+** installed (CloudShell already includes Python, but you can also run this locally).
- **AWS credentials**:
  - In **CloudShell**, credentials are preconfigured for your account.
  - Locally, run `aws configure` to set your access key, secret key, and default region.[web:12]

---

## 4. Getting started

You can run this project either from AWS CloudShell or from your local machine.

### 4.1. Clone the repository

In AWS CloudShell or your local terminal:

```bash
git clone https://github.com/KoushikSamudrala/AWS_Bedrock_Chatbot.git
cd AWS_Bedrock_Chatbot
```

### 4.2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
```

### 4.3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4.4. Configure the project

Open `config.py` and update these values if needed:

- `BEDROCK_REGION` – the region where Bedrock is enabled for your account (for example, `us-east-1`).[web:15]
- `MODEL_ID` – the ID of a text-capable Bedrock model that your account can use (for example, `amazon.nova-lite-v1:0`).[web:15]
- `SYSTEM_PROMPT` – a string describing how the assistant should behave.
- `INFERENCE_CONFIG` – controls max tokens, temperature, and topP.

You can keep the defaults or adjust them as you experiment.

---

## 5. Running the chatbot

From the project root directory:

```bash
python chat.py
```

You should see something like:

```text
=== AWS Bedrock CLI Chatbot ===
Type your message and press Enter.
Type 'exit' or 'quit' to end the chat.
```

Then you can start chatting:

```text
You: Explain what Amazon Bedrock is.
Assistant: ...
```

To exit, type `exit` or `quit` and press Enter.

---

## 6. How multi-turn conversation works

The script keeps a Python list called `history` that stores messages in the format expected by the Bedrock Converse API.[web:9][web:15]

For each turn:
1. Your new message is added to `history` as a `user` message.
2. The full `history` list is sent to `converse` along with the system prompt.
3. The model returns an `assistant` message, which is appended to `history`.
4. The assistant's text is printed in the terminal.

Because the entire history is passed each time, the model can refer back to earlier parts of the conversation and respond in a more contextual way.[web:9][web:11][web:15]

---

## 7. Customizing the system prompt

The system prompt in `config.py` defines how the assistant should behave. For example, it can be:

- More formal or more casual.
- Targeted at beginners or advanced users.
- Focused on a specific domain (like AWS, machine learning, or Python).

Experiment with different system prompts to see how they change the chatbot's responses.[web:8]

---

## 8. My learnings

While building this project, I learned:

- **How to connect a Python script to Amazon Bedrock** using the Bedrock Runtime client and the Converse API.[web:12][web:15]
- **How system prompts influence model behavior**, and how to define them cleanly in a configuration file.[web:9]
- **How to represent chat history as a list of messages** with `user` and `assistant` roles so that the model can maintain context across multiple turns.[web:7][web:11]
- **How to run Bedrock experiments from AWS CloudShell**, where credentials are already configured, and how to reuse the same script locally with `aws configure`.
- **How to structure a small but complete project** with separate modules for configuration, the Bedrock client, and the CLI script so it is easy to extend later.

You can add your own bullet points here that reflect what you learned while following the project.

---

## 9. Troubleshooting

Here are some common issues and how to fix them:

- **Error: AccessDeniedException or model not found**  
  - Make sure the chosen `MODEL_ID` is enabled for your AWS account in the selected region.[web:15]

- **Error: Invalid region or endpoint**  
  - Check that `BEDROCK_REGION` in `config.py` matches a region where Bedrock is available and enabled.[web:15]

- **Credentials or auth errors when running locally**  
  - Run `aws configure` and ensure the profile you are using has permissions for `bedrock:InvokeModel` or the Bedrock Converse API via the runtime client.[web:12]

- **No text returned by the model**  
  - Some models or configurations might return different content types. This script expects text responses and will show `[No text reply returned by the model]` if it cannot find a text block.

---

## 10. Next steps and extensions

Once this basic chatbot is working, you can extend it by:

- Adding **logging** of prompts and responses for later review.
- Saving conversation history to a file or database.
- Building a **web UI** (for example, with Flask or a JavaScript frontend) on top of the same Bedrock client code.
- Integrating other Bedrock features like **knowledge bases** or **RAG** to answer questions with custom data.[web:8]

This repository is a good starting point for more advanced GenAI projects on AWS.
