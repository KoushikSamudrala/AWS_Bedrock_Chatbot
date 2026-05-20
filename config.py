"""Configuration for AWS Bedrock chatbot project.

You can run this from AWS CloudShell or your local machine.
Update the region and model ID to match the model you have access to in your AWS account.
"""

# Region where Amazon Bedrock is available in your account
BEDROCK_REGION = "us-east-1"  # Change this if you enabled Bedrock in a different region

# Default model ID for the chatbot.
# Example model IDs (make sure you have access to the chosen one):
# - "amazon.nova-lite-v1:0"
# - "anthropic.claude-3-haiku-20240307-v1:0"
MODEL_ID = "amazon.nova-lite-v1:0"

# System prompt that sets the behavior of the chatbot
SYSTEM_PROMPT = (
    "You are a friendly and concise AI assistant. "
    "Explain concepts clearly for beginners and use simple language. "
    "If you are unsure about something, say so honestly."
)

# Inference configuration for the model
INFERENCE_CONFIG = {
    "maxTokens": 512,
    "temperature": 0.7,
    "topP": 0.9,
}
