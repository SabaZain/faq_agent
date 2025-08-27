import chainlit as cl
from agents import Runner
from my_agents.faq_agent import agent

@cl.on_message
async def main(message: cl.Message):
    user_input=message.content
    result=Runner.run_sync(starting_agent=agent,input=user_input)
    await cl.Message(content=result.final_output).send()