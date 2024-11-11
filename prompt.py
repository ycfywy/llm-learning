import os
from openai import OpenAI
os.environ["OPENAI_API_KEY"] = os.environ.get("API_KEY")
os.environ["OPENAI_BASE_URL"] = "https://api.chatanywhere.tech/v1"





"""

Prompt using openai api in chat model 


client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

# 获取并打印助手的回复

print(response.choices[0].message.content)



"""


"""

Prompt (Few-Shot) using langchain api in Text model


"""

