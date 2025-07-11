import os
from langsmith import Client
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import Faithfulness, ResponseRelevancy, ContextPrecision, NonLLMContextRecall, ContextRecall
from qdrant_client import QdrantClient


from chatbot_ui.retrieval import rag_pipeline
from chatbot_ui.core.config import config


ls_client = Client(api_key=config.LANGSMITH_API_KEY)
qdrant_client = QdrantClient(url="http://localhost:6333")


ragas_llm = LangchainLLMWrapper(
    ChatOpenAI(
        model='gpt-4.1'
    )
)
ragas_embeddings = LangchainEmbeddingsWrapper(
    OpenAIEmbeddings(
        model='text-embedding-3-small'
    )
)


async def ragas_response_relevance(run, example):
    sample = SingleTurnSample(
        user_input=run.outputs['question'],
        response=run.outputs['answer'],
        retrieved_contexts=run.outputs['retrieved_context']
    )
    scorer = ResponseRelevancy(llm=ragas_llm, embeddings=ragas_embeddings)
    return await scorer.single_turn_ascore(sample)


async def ragas_context_precision(run, example):
    sample = SingleTurnSample(
        user_input=run.outputs['question'],
        response=run.outputs['answer'],
        retrieved_contexts=run.outputs['retrieved_context']
    )
    scorer = ContextPrecision(llm=ragas_llm)
    return await scorer.single_turn_ascore(sample)


async def ragas_context_recall_llm_based(run, example):
    sample = SingleTurnSample(
        user_input=run.outputs['question'],
        response=run.outputs['answer'],
        reference=example.outputs['ground_truth'],
        retrieved_contexts=run.outputs['retrieved_context']
    )
    scorer = ContextRecall(llm=ragas_llm)
    return await scorer.single_turn_ascore(sample)


async def ragas_context_recall_non_llm_based(run, example):
    sample = SingleTurnSample(
        reference_contexts=example.outputs['contexts'],
        retrieved_contexts=run.outputs['retrieved_context']
    )
    scorer = NonLLMContextRecall()
    return await scorer.single_turn_ascore(sample)


async def ragas_faithfulness(run, example):
    sample = SingleTurnSample(
        user_input=run.outputs['question'],
        response=run.outputs['answer'],
        retrieved_contexts=run.outputs['retrieved_context']
    )
    scorer = Faithfulness(llm=ragas_llm)
    await scorer.single_turn_ascore(sample)


results = ls_client.evaluate(
    lambda x: rag_pipeline(x['question'], qdrant_client),
    data='rag-evaluation-dataset',
    evaluators=[
        ragas_response_relevance,
        ragas_context_precision,
        ragas_context_recall_llm_based,
        ragas_context_recall_non_llm_based,
        ragas_faithfulness
    ],
    experiment_prefix='rag-evaluation-dataset'
)
