from agents import Agent
from my_config.config import model

agent:Agent=Agent(
    name="Basic FAQ Agent",
    instructions="You are a helpful FAQ Bot.Answer user questions concisely.",
    model=model
)