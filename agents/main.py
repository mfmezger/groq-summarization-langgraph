from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()


chat = ChatGroq(temperature=0, model_name="llama3-8b-8192")
prompt = ChatPromptTemplate.from_messages([("human", "Write a JSON about the specific phases of {topic}")])
chain = prompt | chat
for chunk in chain.stream({"topic": "The Moon"}):
    print(chunk.content, end="", flush=True)