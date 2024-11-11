import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# 创建 ChatOpenAI 实例
chat = ChatOpenAI(model="gpt-4", 
                  temperature=0.8, 
                  max_tokens=60,
                  api_key=os.getenv("API_KEY"),
                  base_url="https://api.chatanywhere.org")

# print(os.getenv("API_KEY"))
# 准备消息
messages = [
    SystemMessage(content="你是一个很棒的智能助手"),
    HumanMessage(content="请给我的花店起个名")
]

# 使用 invoke 方法获取响应
response = chat.invoke(messages)

# 打印响应
print(response)
