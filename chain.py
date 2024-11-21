import os
from langchain_openai import OpenAI
from langchain.chains.conversation.base import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory


os.environ["OPENAI_API_KEY"] = os.environ.get("API_KEY")
os.environ["OPENAI_API_BASE"] = "https://api.chatanywhere.tech/v1"

# 初始化大语言模型


llm = OpenAI(
    temperature=0.5,
    model="gpt-3.5-turbo-instruct"
)

# 初始化对话链
conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory()
)

# 第一天的对话
# 回合1
conversation("我姐姐明天要过生日，我需要一束生日花束。")
print("第一次对话后的记忆:", conversation.memory.buffer)
