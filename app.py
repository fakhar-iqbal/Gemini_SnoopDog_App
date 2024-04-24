from dotenv import load_dotenv
load_dotenv()  ##loading all environment variables 

import streamlit as st
import os

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini pro model and get responses

model = genai.GenerativeModel("gemini-pro")

def get_gemini_Response(question):

    response = model.generate_content(question)

    return response.text

##Initialize our streamlit app

st.set_page_config(page_title="Ask the LLM Model", page_icon=":robot_face:")

with open("style.css") as f:
        
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Add header with logo
st.markdown("""
<div style="display: flex; align-items: center; margin-bottom: 20px;">
    <img src="https://i.pinimg.com/originals/18/a0/2c/18a02c402f6cfec2cd40d8bb4eac4637.png" alt="LLM" style="height: 50px; margin-right: 10px;">
    <h1 style="margin-bottom: 0;">Ask the LLM Model</h1>
</div>
""", unsafe_allow_html=True)

    # Input field for the question
question = st.text_area("Enter your question:", height=200)

    # Submit button
submit_button = st.button("Ask the Question")

## when submit is hit:

if submit_button:
    response = get_gemini_Response(question)

    st.subheader("The response is ")
    st.write(response)

