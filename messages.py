from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages=[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="tell me about  langChain")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)