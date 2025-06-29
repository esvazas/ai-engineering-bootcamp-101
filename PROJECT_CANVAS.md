# Project Canvas: AI-Powered Amazon Product Assistant

## 1. Problem Statement

**Objective**:
To enhance customer satisfaction and enagagement with Amazon marketplace by developing a dynamic AI assistant with a basic Q&A system (at first) and more advanced agent-driven application (later).

## 2. Data & Knowledge
We will leverage public Amazon product datasets such as the open Amazon product reviews and metadata. These provide rich textual information (product titles, descriptions and customer reviews) that our assistant will use to answer questions and make recommendations. For manageability, a subset of the data (for example, a specific product category or a few thousand products) will be selected and indexed. The dataset can be found [here](https://amazon-reviews-2023.github.io/#grouped-by-category).


## 3. AI Approach & Methodology
We'll start with a Retrieval-Augmented Generation (RAG) along with a fine-tuned large language model (LLM) to efficiently utilize contextual embeddings for precise information retrieval and content generation. Further implementation will include progression through an agent performing various actions (e.g. clarifying details, giving recommenteations, estimating delivery, managing cart operations) that can further be conceptualised into a multi-agent system.


## 4. Performance Metrics & Evaluation Rules
North star metric: transactions per active user.

However, we'll also monitor a bunch of supporting metrics:
- technical metrics: P50 and P99 latency, top-k precision, model downtime, query throughput
- operational metrics: #support tickets per active user, #sessions per active user, user retention rate, cost per interaction
- business metrics: cart value per active user, pGMV per active user,


## 5. Resources & Stakeholders
Everything in this project will be implemented by a Data Scientist. Required resourses consists of:
- costs for interacting with LLMs through the API (mostly OPENAI);
- computing capacity for fine-tuning LLM;
- ...


## 6. Risks & Mitigation

**Anticipated Risks**:
- Handling large-scale data with LLMs, ensuring data privacy, and managing potential biases in outputs.

**Mitigation Strategies**:
- Implement robust data management and regular bias checks.
- Implement continious monitoring for associated costs.
- Implement continious monitoring for technical metrics (defined above).
- Enhance security protocols to safeguard data integrity.
- Continuously assess risks and adapt mitigation strategies accordingly.

## 7. Deployment & Integration
TODO

## 8. Timeline & Milestones
TODO; but we'll work in a weekly sprints iteratively upscaling RAG -> agent -> multi-agent product system for Amazon.
