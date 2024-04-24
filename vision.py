from dotenv import load_dotenv
load_dotenv()  ##loading all environment variables 

import streamlit as st
import os

from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini pro model and get responses

model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_Response(input, image):

    if input != "":
        response = model.generate_content([input,image])
    else:

        response = model.generate_content(image)

    return response.text

##initialize the streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")

input = st.text_input("Input Prompt: " ,key="input")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

submit = st.button("Tell me about the image")

##if submit is clicked
if submit:
    response = get_gemini_Response(input,image)
    st.subheader("The response is: ")
    st.write(response)