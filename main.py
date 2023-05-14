#key
import os 
from apikey import APIKEY
import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = APIKEY

#app
st.title("Youtube Gpt")
prompt = st.text_input("plug in your prompt")

#templates
title_template = PromptTemplate(
    input_variables= ['topic'],
    template = 'write me a youtube video tittle about {topic}'
)
#llms 
llm = OpenAI(temperature=0.9) #creativity

#screen output
if prompt:
    response = llm(prompt)
    st.write(response)
