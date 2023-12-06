import streamlit as st

import os
import datetime
import numpy as np
import os
import vertexai
from vertexai.language_models import ChatModel, InputOutputTextPair

credential_path = "nlp-chatbot-405618-5fa9f1339a89.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


st.title("Mental Health assistant - PaLM")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        vertexai.init(project="nlp-chatbot-405618", location="us-central1")
        chat_model = ChatModel.from_pretrained("chat-bison")
        parameters = {
            "candidate_count": 1,
            "max_output_tokens": 1024,
            "temperature": 0.2,
            "top_p": 0.8,
            "top_k": 40
        }
        chat = chat_model.start_chat(
            context="""You are a mental health professional and guides people and provide solutions""",
        )
        response = chat.send_message(prompt, **parameters)

        full_response += response.text
        message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})



