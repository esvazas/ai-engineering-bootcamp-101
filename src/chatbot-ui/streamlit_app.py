import streamlit as st
from openai import OpenAI
from groq import Groq
from google import genai
from core.config import config

## Lets create a sidebar with a dropdown model list and provider list
with st.sidebar:
    st.title("Chatbot UI")

    provider_list = ["openai", "groq", "google"]
    provider = st.selectbox("Select a provider", provider_list)
    if provider == "openai":
        model_name = st.selectbox("Select a model",  ["gpt-4o-mini"])
    elif provider == "groq":
        model_name = st.selectbox("Select a model", ["llama-3.1-8b-instant"])
    elif provider == "google":
        model_name = st.selectbox("Select a model", ["gemini-2.0-flash"])

    st.session_state.provider = provider
    st.session_state.model_name = model_name

## adjust line below for all providers
if st.session_state.provider == "openai":
    client = OpenAI(api_key=config.OPENAI_API_KEY)
elif st.session_state.provider == "groq":
    client = Groq(api_key=config.GROQ_API_KEY)
elif st.session_state.provider == "google":
    client = genai.Client(api_key=config.GOOGLE_API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you today?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])



def run_llm(client, messages, max_tokens=500):
    if st.session_state.provider == 'google':
        return client.models.generate_content(
            model=st.session_state.model_name,
            contents=[message['content'] for message in messages],
        ).text
    else:
        return client.chat.completions.create(
            model=st.session_state.model_name,
            messages=messages,
            max_tokens=max_tokens
        ).choices[0].message.content



if prompt := st.chat_input("Hello! How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        output = run_llm(client, st.session_state.messages)
        st.write(output)

    st.session_state.messages.append({"role": "assistant", "content": output})
