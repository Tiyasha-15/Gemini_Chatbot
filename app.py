from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
import google.generativeai as genai 


genai.configure(api_key=os.environ['Google_Api_key'])


model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
  response = model.generate_content(question)
  return response.text


st.set_page_config(page_title="Q&A")

st.header("Genini LLM Application")

input = st.text_input("Input: ", key = "input")
submit = st.button("Ask the question")

if submit:
  response = get_gemini_response(input)
  st.subheader("the response is")
  st.write(response)
