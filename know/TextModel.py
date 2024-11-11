import os
import openai
from openai import OpenAI


os.environ["OPENAI_API_KEY"] = os.environ.get("API_KEY")



client = OpenAI()

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  temperature=0.5,
  max_tokens=100,
  prompt="请给我的花店起个名")
