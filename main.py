from my_agents.faq_agent import agent
from agents import Runner

print("Welcome to FAQ Chatbot...")
while True:
    user_question = input("User: ")
    if user_question.lower() in ["exit","quit"]:
        print("Thankyou for interacting with Chatbot!")
        break
    result=Runner.run_sync(starting_agent=agent,input=user_question)
    print(result.final_output)
