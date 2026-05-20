"""Wrapper around the Amazon Bedrock Runtime client.

This module exposes a simple function to send a multi-turn conversation
(history + new user message) to a Bedrock model using the Converse API.
"""

import boto3
from botocore.config import Config

from config import BEDROCK_REGION, MODEL_ID, INFERENCE_CONFIG, SYSTEM_PROMPT


def get_bedrock_runtime_client():
    """Create and return a Bedrock Runtime client.

    This relies on your AWS credentials being configured.
    In CloudShell, this is usually handled for you automatically.
    Locally, make sure you have run `aws configure` or set env vars.
    """

    boto_config = Config(
        region_name=BEDROCK_REGION,
        retries={"max_attempts": 3, "mode": "standard"},
    )

    return boto3.client("bedrock-runtime", config=boto_config)


def converse_with_bedrock(messages):
    """Call the Bedrock Converse API with the given chat history.

    Args:
        messages (list[dict]): List of message objects in the format
            expected by the Converse API. Each message includes a
            `role` ("user" or "assistant") and `content`.

    Returns:
        str: The assistant's response text.
    """

    client = get_bedrock_runtime_client()

    response = client.converse(
        modelId=MODEL_ID,
        system=[{"text": SYSTEM_PROMPT}],
        messages=messages,
        inferenceConfig=INFERENCE_CONFIG,
    )

    # For text responses, the first content block contains the assistant reply
    output_message = response["output"]["message"]
    contents = output_message.get("content", [])

    # Find the first text block
    for block in contents:
        if "text" in block:
            return block["text"]

    # Fallback if the response format is unexpected
    return "[No text reply returned by the model]"
