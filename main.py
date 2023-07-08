import streamlit as st
from embedchain import OpenSourceApp

# Create a new instance of the bot
pat_chat_bot = OpenSourceApp()

# Add online resources
# pat_chat_bot.add("youtube_video", "https://www.youtube.com/watch?v=<patent_related_video>")
pat_chat_bot.add("pdf_file", "https://www.uspto.gov/web/offices/pac/mpep/consolidated_laws.pdf")
# pat_chat_bot.add("web_page", "https://www.uspto.gov/patents")

# Add local resources
pat_chat_bot.add_local("qna_pair", ("What is a utility patent?", "A utility patent is a patent that covers the creation of a new or improved—and useful—product, process, or machine. It generally permits its owner to exclude others from making, using, or selling the invention for a period of up to twenty years from the date of patent application filing, subject to the payment of maintenance fees."))

# Create an input field in the Streamlit app for user input
user_input = st.text_input("You:")

if user_input:
    # Generate the chatbot's response
    response = pat_chat_bot.chat(user_input)

    # Display the chatbot's response in the Streamlit app
    st.write('Chatbot:', response)
