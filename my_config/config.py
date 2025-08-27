from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel,set_tracing_disabled
import os

set_tracing_disabled(True)
load_dotenv(override=True)

gemini_api_key=os.getenv("GEMINI-API-KEY")
gemini_base_url=os.getenv("GEMINI-BASE-PATH")
gemini_model_name=os.getenv("GEMINI-MODEL-NAME")

client=AsyncOpenAI(api_key=gemini_api_key,base_url=gemini_base_url)
model=OpenAIChatCompletionsModel(model=gemini_model_name,openai_client=client)