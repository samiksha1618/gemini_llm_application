from dotenv import load_dotenv
load_dotenv()

import streamlit as st  
import os
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")

def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Streamlit App UI
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the Question")

if submit:
    if input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = get_gemini_response(input)
        st.subheader("The Response is")
        st.write(response)
