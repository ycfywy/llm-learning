import os

from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent,AgentType,create_react_agent,AgentExecutor

os.environ["OPENAI_API_KEY"] = os.environ.get("API_KEY")
os.environ["OPENAI_API_BASE"] = "https://api.chatanywhere.tech/v1"



llm = ChatOpenAI(temperature=0)
tools = load_tools(["arxiv"],)

agent_chains = create_react_agent(
    tools= tools,
    llm = llm,
    prompt=AgentType.ZERO_SHOT_REACT_DESCRIPTION
    # agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)
agent_chains_executor = AgentExecutor(agent=agent_chains,tools=tools,verbose=True)

agent_chains_executor.invoke({"input":"介绍一下2005.14165这篇论文的创新点?"})