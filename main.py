import os
import streamlit as st
from embedchain import App

# Create the patent chatbot
pat_chat_bot = App()

api_key = ""

# Sidebar form
with st.sidebar.form(key='my_form'):
    st.write("Enter your OpenAI API key")
    api_key = st.text_input('', type="password")
    submit_button = st.form_submit_button('Submit')

if submit_button:
    os.environ["OPENAI_API_KEY"] = api_key

st.title("AI Patent Guide")

# If the API key is entered, display the text box for user question
if api_key:
    user_question = st.text_input("Enter your question related to patent")
else:
    user_question = ""
    st.write("Please enter your OpenAI API key to continue.")

# Add online resources
pat_chat_bot.add("youtube_video", "https://www.youtube.com/watch?v=<patent_related_video>")
pat_chat_bot.add("pdf_file", "https://www.uspto.gov/sites/default/files/documents/USPTOManualPatents.pdf")
pat_chat_bot.add("web_page", "https://www.uspto.gov/patents")

# Add local resources
pat_chat_bot.add_local("qna_pair", ("What is a utility patent?", "A utility patent is a patent that covers the creation of a new or improved—and useful—product, process, or machine. It generally permits its owner to exclude others from making, using, or selling the invention for a period of up to twenty years from the date of patent application filing, subject to the payment of maintenance fees."))

# If the API key is set and user question has been entered, generate the answer
if api_key and user_question:
    try:
        response = pat_chat_bot.chat(user_question)
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
