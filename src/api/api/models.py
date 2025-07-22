from pydantic import BaseModel, Field
from typing import List, Any, Optional


class RAGRequest(BaseModel):
    query: str = Field(..., description="The query to search the RAG database")


class RAGUsedImage(BaseModel):
    image_url: str = Field(..., description="The image URL")
    price: str = Field(..., description="The price of the item")
    description: str = Field(..., description="The description of the item")

class RAGResponse(BaseModel):
    request_id: str = Field(..., description="The request ID")
    answer: str = Field(..., description="The answer to the query")
    used_image_urls: List[RAGUsedImage]
