#########################################################
# simple chain example
#########################################################

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from colorama import Fore, Style

llm = ChatGoogleGenerativeAI(api_key="PUT_YOUR_API_KEY",model="gemini-2.0-flash",temperature=0.5)
chain = llm | StrOutputParser()

query = "tell me 20 linux commands "

for chunk in chain.stream(input=query):
    print(Fore.LIGHTBLUE_EX + chunk, end="", flush=True)

#########################################################
# using vision multimodal
#########################################################

from google import genai

import PIL.Image

image = PIL.Image.open('path/to/image')

client = genai.Client(api_key="PUT_YOUR_API_KEY")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["What is this image?", image])

print(response.text)

#########################################################
# adding memory
#########################################################

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os


llm = ChatGoogleGenerativeAI(api_key="PUT_YOUR_API_KEY",model="gemini-2.0-flash",temperature=0.5)
chain = llm | StrOutputParser()


prompt = """
you are a helpfull and friendly ai, look carefully in the history bellow of the conversation with the human.

conversation history :
{history}

user question : {query}
"""

if not os.path.exists("memory.txt"):
    with open("memory.txt", 'w') as f:
        f.write("")  

with open("memory.txt",'r') as f:
    history = f.read()

query = input("enter your question : ")
prompt = prompt.replace("{query}", query)
prompt = prompt.replace("{history}", history)

chunks = []
for chunk in chain.stream(input=prompt):
    print(chunk, end="", flush=True)
    chunks.append(chunk)
response = ''.join(chunks)

with open("memory.txt","a") as f:
    history = "user question : " + query + "\n" + "ai response : " + response + "\n"
    f.write(history)

