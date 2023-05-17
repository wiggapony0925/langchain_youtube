#key
import os 
from apikey import APIKEY
import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

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
title_chain = LLMChain(llm=llm, prompt= title_template, verbose=True, output_key='title')
script_chain = LLMChain(llm=llm, prompt= script_template, verbose=True, output_key='script')

#chain these two isntances together
sequential_chain = SequentialChain(chains=[title_chain, script_chain], input_variables=['topic'], output_variables=['title', 'script'], verbose=True)

#screen output
if prompt:
    response = sequential_chain({'topic': prompt})
    st.write(response['title'])
    st.write(response['scripts'])
