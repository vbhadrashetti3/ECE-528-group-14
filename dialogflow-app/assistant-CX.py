import streamlit as st
import streamlit.components.v1 as components

st.title("Mental Health Assistant - Dialogflow CX + PaLM2 (bison)")
components.html(
"""<link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
<script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>
<df-messenger
  project-id="nlp-chatbot-405618"
  agent-id="bff423a1-f65c-4054-9331-2e03df4568fa"
  language-code="en">
  <df-messenger-chat
   chat-title="Talk to your mental health assistant,">
  </df-messenger-chat>
</df-messenger>
<style>
  df-messenger {
    z-index: 999;
    position: fixed;
    bottom: 0;
    right: 0;
    top: 0;
    width: 800px;
  }
</style>""",    height=600,width=800)
st.markdown('<style>iframe {border: 1px solid #bfbfbf !important}</style>', unsafe_allow_html=True)