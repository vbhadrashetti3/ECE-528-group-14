from openai import OpenAI
import streamlit as st

import warnings
warnings.filterwarnings('ignore')

from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import pipeline
import regex as re

model_path = "llama-2-7b-custom"

model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)



st.title("Mental Health assistant - llama2")

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
        
        gen = pipeline('text-generation', model=model, tokenizer=tokenizer, max_length=800)
        result = gen(prompt)
        response = result[0]['generated_text'].replace(prompt, '')
        pattern = re.compile(r'\[/INST\]')
        if re.search(pattern, response):
            response = response.split("[/INST]")
            full_response += response[1]
        else:
            full_response += response

        message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})











