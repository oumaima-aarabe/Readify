import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import os

st.title("Readify")

uploaded_file = st.file_uploader("Upload a CSV file to analyse")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) #create dataframe
    st.write(df.head(10)) #display the first 3 rows , wrritten to our UI
    
    prompt = st.text_area("yout prompt : ")
    if st.button("Generate"):
        if prompt:
                st.write("Generating response ...")
        else:
            st.warning("Please enter a Prompt. ")
            
load_dotenv()

my_token = os.getenv("OPENAI_API_KEY")

llm = OpenAI(my_token)
pandas_ai = PandasAI(llm)
