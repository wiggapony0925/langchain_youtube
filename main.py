#key
import os 
from apikey import APIKEY
import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

os.environ['OPENAI_API_KEY'] = APIKEY

#app
st.title("Youtube Gpt")
prompt = st.text_input("plug in your prompt")

#templates
script_template = PromptTemplate(
    input_variables= ['title'],
    template = 'write me a youtube video script based on this title:  {topic}'
)
# generate the script
#llms 
llm = OpenAI(temperature=0.9) #creativity
title_chain = LLMChain(llm=llm, prompt= script_template, verbose=True)

#screen output
if prompt:
    response = title_chain.run(topic=prompt)
    st.write(response)
