import streamlit as st
from openai import OpenAI
from groq import Groq
from google import genai
from google.genai import types
from qdrant_client import QdrantClient


from retrieval import rag_pipeline
from core.config import config


qdrant_client = QdrantClient(
    url=f"http://{config.QDRANT_URL}:6333"
    )


with st.sidebar:
    st.title("Chatbot UI")

    provider_list = ["openai", "groq", "google"]
    provider = st.selectbox("Select a provider", provider_list)
    if provider == "openai":
        model_name = st.selectbox("Select a model",  ["gpt-4o-mini"])
        temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    elif provider == "groq":
        model_name = st.selectbox("Select a model", ["llama-3.1-8b-instant"])
        temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    elif provider == "google":
        model_name = st.selectbox("Select a model", ["gemini-2.0-flash"])
        temperature = st.slider("Temperature", min_value=0.0, max_value=2.0, value=1.0, step=0.1)

    max_tokens = st.slider("Max Tokens", min_value=100, max_value=1000, value=500, step=100)

    st.session_state.provider = provider
    st.session_state.model_name = model_name
    st.session_state.temperature = temperature
    st.session_state.max_tokens = max_tokens

## adjust line below for all providers
if st.session_state.provider == "openai":
    client = OpenAI(api_key=config.OPENAI_API_KEY)
elif st.session_state.provider == "groq":
    client = Groq(api_key=config.GROQ_API_KEY)
elif st.session_state.provider == "google":
    client = genai.Client(api_key=config.GOOGLE_API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You should never disclose what model are you based on"}]


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])



def run_llm(client, messages, max_tokens=500):
    if st.session_state.provider == 'google':
        return client.models.generate_content(
            model=st.session_state.model_name,
            contents=[message['content'] for message in messages],
            config=types.GenerateContentConfig(
                temperature=st.session_state.temperature,
                max_output_tokens=st.session_state.max_tokens,
            )
        ).text
    else:
        return client.chat.completions.create(
            model=st.session_state.model_name,
            messages=messages,
            temperature=st.session_state.temperature,
            max_tokens=st.session_state.max_tokens
        ).choices[0].message.content



if prompt := st.chat_input("Hello! How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        #output = run_llm(client, st.session_state.messages)
        output = rag_pipeline(prompt, qdrant_client)['answer']
        st.write(output)

    st.session_state.messages.append({"role": "assistant", "content": output})
