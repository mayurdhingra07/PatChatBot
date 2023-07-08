import os
from embedchain import App
import streamlit as st

# Create a form for the API key
with st.form(key='api_key_form'):
    # Prompt the user to enter their OpenAI API key
    api_key = st.text_input('Enter your OpenAI API key', type='password')
    # Create a submit button for the form
    submitted = st.form_submit_button('Enter')

# If the form has been submitted, process the API key
if submitted and api_key:
    # Set the OpenAI API key
    os.environ["OPENAI_API_KEY"] = api_key

    # Create the patent chatbot
    pat_chat_bot = App()

    # Add online resources
    # pat_chat_bot.add("youtube_video", "https://www.youtube.com/watch?v=<patent_related_video>")
    pat_chat_bot.add("pdf_file", "https://www.uspto.gov/web/offices/pac/mpep/consolidated_laws.pdf")
    # pat_chat_bot.add("web_page", "https://www.uspto.gov/patents")

    # Add local resources
    pat_chat_bot.add_local("qna_pair", ("What is a utility patent?", "A utility patent is a patent that covers the creation of a new or improved—and useful—product, process, or machine. It generally permits its owner to exclude others from making, using, or selling the invention for a period of up to twenty years from the date of patent application filing, subject to the payment of maintenance fees."))

    # Query the chatbot
    st.write(pat_chat_bot.query("What is a utility patent?"))

    # Interact with the chatbot
    st.write(pat_chat_bot.chat("What is a patent?"))
