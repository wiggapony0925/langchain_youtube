#key
import os 
from apikey import APIKEY
import streamlit as st 
from langchain.llms import OpenAI



os.environ['OPENAI_API_KEY'] = APIKEY

#app
st.title("Youtube Gpt")
prompt = st.text_input("plug in your prompt")