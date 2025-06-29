# AI Engineering Bootcamp 101

A comprehensive AI engineering project that demonstrates working with multiple LLM providers, data processing, and building interactive applications.

## 🚀 Features

- **Multi-Provider LLM Integration**: Support for OpenAI, Google Gemini, and Groq APIs
- **Interactive Chatbot UI**: Streamlit-based web interface for testing different LLM models
- **Amazon Dataset Processing**: Tools for processing and analyzing Amazon Electronics review data
- **Jupyter Notebooks**: Educational notebooks for exploring LLM calls and dataset analysis
- **Docker Support**: Containerized deployment options

## 📁 Project Structure

```
ai-engineering-bootcamp-101/
├── data/                          # Amazon Electronics dataset files
├── notebooks/                     # Jupyter notebooks for exploration
│   ├── 00-explore-llm-calls.ipynb
│   └── 01-explore-amazon-dataset.ipynb
├── src/
│   └── chatbot-ui/               # Streamlit chatbot application
│       ├── core/
│       │   └── config.py         # Configuration management
│       └── streamlit_app.py      # Main Streamlit app
├── main.py                       # Simple entry point
├── pyproject.toml               # Project dependencies
├── Makefile                     # Build and run commands
└── Dockerfile                   # Docker configuration
```

## 🛠️ Setup

### Prerequisites

- Python 3.11+
- API keys for:
  - OpenAI
  - Google Gemini
  - Groq

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-engineering-bootcamp-101
   ```

2. **Install dependencies**
   ```bash
   pip install -e .
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   GOOGLE_API_KEY=your_google_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

## 🚀 Usage

### Running the Chatbot UI

**Option 1: Direct Streamlit run**
```bash
make run-streamlit
```

**Option 2: Docker deployment**
```bash
make build-docker-streamlit
make run-docker-streamlit
```

**Option 3: Manual Streamlit run**
```bash
streamlit run src/chatbot-ui/streamlit_app.py
```

The chatbot UI will be available at `http://localhost:8501`


## 🔧 Configuration

Configuration is managed through `src/chatbot-ui/core/config.py` using Pydantic settings. The system automatically loads environment variables for API keys.


---

**Note**: Make sure to keep your API keys secure and never commit them to version control.

