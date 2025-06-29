run-streamlit:
	streamlit run src/chatbot-ui/streamlit_app.py

build-docker-streamlit:
	docker build -t streamlit-app-latest .

run-docker-streamlit:
	docker run -v ${PWD}/.env:/app/.env -p 8501:8501 streamlit-app-latest
