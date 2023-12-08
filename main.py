import os
import openai
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.schema import HumanMessage


def load_from_env(var_name):
    env_file_path = os.path.join(os.getcwd(), ".env")
    if os.path.exists(env_file_path):
        with open(env_file_path) as f:
            for line in f:
                if line.startswith(f"{var_name}="):
                    return line.strip().split("=")[1]
    return None


def load_api_key():
    return load_from_env("OPENAI_APIKEY")


llm = OpenAI(openai_api_key=load_api_key())
chat_model = ChatOpenAI(openai_api_key=load_api_key(), temperature=0.9)

openai_api_key = load_api_key()

text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]

print(llm.invoke(text))

print(chat_model.invoke(messages))
