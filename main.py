#key
import os 
from apikey import APIKEY
import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

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
    input_variables= ['title', 'wikipedia_research'],
    template = 'write me a youtube video script based on this title:  {topic} while leveraging this wikipedia research: {wikipedia_research}'                  
)
# generate the script

#Memeroy
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')
#llms 
llm = OpenAI(temperature=0.9) #creativity
title_chain = LLMChain(llm=llm, prompt= title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt= script_template, verbose=True, output_key='script', memory=script_memory)

#chain these two isntances together
wiki = WikipediaAPIWrapper()
#screen output
if prompt:
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title=title, wikipedia_research=wiki_research)
    st.write(title)
    st.write(script)
    
    #memory output
    with st.expander('Title history'):
        st.info(title_memory.buffer)
        
    with st.expander('Scripts History'):
        st.info(script_memory.buffer)
        
    with st.expander('Wikipedia History'):
        st.info(wiki_research)