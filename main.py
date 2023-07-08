import os
import streamlit as st
from collections import deque
from embedchain import App

# Set the OpenAI API key
@st.cache(allow_output_mutation=True)
def set_api_key(api_key):
    os.environ["OPENAI_API_KEY"] = api_key

# Set the title in the middle of the page
st.title("Your Patent Guide to U.S. Law")

# Sidebar form for API key
with st.sidebar.form(key='api_key_form'):
    api_key = st.text_input('Enter your OpenAI API key', value="", type="password")
    submitted = st.form_submit_button('Enter')
    if submitted:
        set_api_key(api_key)

# If the API key is entered, display the chat interface
if os.getenv("OPENAI_API_KEY"):
    # Create the patent chatbot
    pat_chat_bot = App()

    # Add online resources
    # pat_chat_bot.add("youtube_video", "https://www.youtube.com/watch?v=<patent_related_video>")
    pat_chat_bot.add("pdf_file", "https://www.uspto.gov/web/offices/pac/mpep/consolidated_laws.pdf")
    # pat_chat_bot.add("web_page", "https://www.uspto.gov/patents")

    # Add local resources
    pat_chat_bot.add_local("qna_pair", ("What is a utility patent?", "A utility patent is a patent that covers the creation of a new or improved—and useful—product, process, or machine. It generally permits its owner to exclude others from making, using, or selling the invention for a period of up to twenty years from the date of patent application filing, subject to the payment of maintenance fees."))

    # Create the chat interface
    st.markdown("**Chat Interface**")
    user_input = st.text_input("Type your question here...")

    # Get or initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = deque([], maxlen=5)

    if st.button("Send"):
        response = pat_chat_bot.chat(user_input)
        st.session_state.chat_history.appendleft((user_input, response))

    # Display the chat history
    for user_msg, bot_msg in st.session_state.chat_history:
        st.markdown(f"> **User**: {user_msg}\n> **Bot**: {bot_msg}")
else:
    st.write("Please enter your OpenAI API key to continue.")
