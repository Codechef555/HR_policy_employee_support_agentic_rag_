#**`app/rag/state.py`** — Define the LangGraph shared state containing the question, retrieved documents, grades, answer, retries, citations, and trace

from typing import List, Literal
from typing_extensions import TypedDict
from pydantic import BaseModel, Field
from langchain_core.documents import Document

class RouteDecision(BaseModel):
    route: Literal["kb", "direct"] = Field(description="kb for HR/policy questions; direct for greetings/simple chat")


class EvidenceGrade(BaseModel):
    grade: Literal['good','weak'] = Field(description="Whether evidence is sufficient to answer")