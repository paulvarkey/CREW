import requests

from autogen_core.models import UserMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelFamily
from autogen_agentchat.agents import AssistantAgent
from autogen_core import CancellationToken
from autogen_core.tools import FunctionTool
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.ui import Console
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_core.model_context import BufferedChatCompletionContext, ChatCompletionContext
from autogen_agentchat.conditions import ExternalTermination, TextMentionTermination

from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio

import requests

import requests

# Define the Ollama server URL and model
OLLAMA_URL = "http://10.148.54.160:11434/api/generate"
MODEL_NAME = "deepseek-llm:67b"

# Define the prompt
prompt = "What is the capital of France?"

# Send the request to the Ollama server
response = requests.post(
    OLLAMA_URL,
    json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False  # Set to True if you want streaming responses
    }
)

# Print the response
if response.status_code == 200:
    print("Response:", response.json()["response"])
else:
    print("Error:", response.status_code, response.text)

breakpoint()


model_client = OpenAIChatCompletionClient(
    model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
    base_url="http://10.148.54.160:8000/v1/completions",
    api_key="placeholder",
    model_info={
    },
)

autogen = AssistantAgent(
            name="agent",
            description="desc",
            model_client=model_client,
            system_message="you are an assistant agent",
            model_context=BufferedChatCompletionContext(buffer_size=5)
            )


response = asyncio.run(autogen.run(task=TextMessage(content="what is the capital of france", source="user"), cancellation_token=CancellationToken()))