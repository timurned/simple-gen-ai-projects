from openai import OpenAI
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# configure OpenAI service client 
client = OpenAI()
deployment = "gpt-3.5-turbo"

num_facts = input("Number of facts (for example, 5): ")
historical_figure = input("The name of a historical figure (for example, Napoleon): ")

# define the prompt
prompt = f"Show me {num_facts} cool facts about {historical_figure}."
messages = [{"role": "user", "content": prompt}]
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=600, temperature = 0.1)

# print response
print("Cool facts:")
print(completion.choices[0].message.content)
