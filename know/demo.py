import os
import openai
from openai import OpenAI


os.environ["OPENAI_API_KEY"] = os.environ.get("API_KEY")
os.environ["OPENAI_BASE_URL"] = "https://api.chatanywhere.tech/v1"


client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    # api_key=os.environ.get("API_KEY"),
    # base_url="https://api.chatanywhere.tech/v1"
    # base_url="https://api.chatanywhere.org/v1"
)



# 非流式响应
def gpt_35_api(messages: list):
    """为提供的对话消息创建新的回答

    Args:
        messages (list): 完整的对话消息
    """
    completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    print(completion.choices[0].message.content)

def gpt_35_api_stream(messages: list):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
    """
    stream = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")

 

if __name__ == '__main__':
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "讲解一下transformer"
            }
        ],
        temperature=0.9,
        max_tokens=60
    )
    
    print(completion.choices[0].message)


