# Amazon UX Chatbot with RAG

A comprehensive AI engineering project that demonstrates working with multiple LLM providers, data processing, and building interactive applications. Enhanced with Retrieval-Augmented Generation (RAG) capabilities for improved question-answering.

## Use Cases

### Amazon UX Chatbot
- **Purpose**: Interactive chatbot for Amazon Electronics product support and reviews
- **Features**:
  - OpenAI support for streamlit app
  - RAG-enhanced responses using product documentation
  - Vector database (Qdrant) for semantic search
  - Streamlit UI for user interaction


## Quick Start


### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-engineering-bootcamp-101
   ```

2. **Install dependencies with uv**
   ```bash
   uv sync
   source .venv\Scripts\activate
   ```

### Environment Setup
Copy the example environment file and add your API keys:

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file with your actual API keys
# Required for RAG and evaluation
OPENAI_API_KEY=your_openai_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
```

### Run the System

# Run the complete system (includes Qdrant, chatbot, and evaluation)
```
make run-docker-compose
```
# Or run evaluation component:
```
make run-eval
```

## Architecture
- `src/chatbot_ui/`: RAG pipeline and UI
- `evals/`: Evaluation scripts and metrics
- `data/`: Document storage
- `notebooks/`: Exploration and preprocessing

## Observability

### Metrics & Tracing
- **LangSmith Integration**: Comprehensive tracing of LLM calls, RAG pipeline, and evaluation runs
- **Ragas Metrics**: Automated evaluation of RAG performance across multiple dimensions
- **Experiment Tracking**: Compare different model configurations and RAG strategies
- **Performance Monitoring**: Track response times, token usage, and retrieval quality

### Key Metrics Tracked
- **RAG Quality**: Faithfulness, relevancy, context precision/recall
- **System Performance**: Response latency, token consumption, retrieval speed
- **User Experience**: Answer accuracy, conversation flow, context relevance

## Observability, Tracing & Evaluation

- **Tracing & Metrics Dashboard:**
  All LLM and RAG pipeline calls are traced and logged via [LangSmith](https://smith.langchain.com/).

  **How to Inspect:**
  1. Run the system with tracing enabled (tracing is active by default if you set `LANGSMITH_API_KEY` in your `.env`).
  2. Use the following Makefile commands:
     - `make run-docker-compose` — Runs the full system with tracing and evaluation enabled.
     - `make run-eval` — Runs the evaluation script and logs results to LangSmith.
  3. Go to your [LangSmith dashboard](https://smith.langchain.com/) and log in with your account linked to your `LANGSMITH_API_KEY`.
  4. Find experiment runs, traces, and metrics for each evaluation and chatbot session.

- **Evaluation Results:**
  Automated RAG evaluation metrics (faithfulness, relevancy, context precision/recall, factual correctness) are logged to LangSmith.

  **How to Inspect:**
  1. Run `make run-eval` to execute the evaluation pipeline.
  2. In the LangSmith dashboard, select your experiment (e.g., `rag-evaluation-dataset`) to view detailed metric results and compare runs.

