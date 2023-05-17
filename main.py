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
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template = 'write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables= ['title'],
    template = 'write me a youtube video script based on this title:  {topic}'
)
# generate the script
#llms 
llm = OpenAI(temperature=0.9) #creativity
title_chain = LLMChain(llm=llm, prompt= title_template, verbose=True)
script_chain = LLMChain(llm=llm, prompt= script_template, verbose=True)

#chain these two isntances together
sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose=True)#list of sequence 

#screen output
if prompt:
    response = sequential_chain.run(prompt)
    st.write(response)
