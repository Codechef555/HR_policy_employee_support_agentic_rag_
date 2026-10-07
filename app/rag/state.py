#**`app/rag/state.py`** — Define the LangGraph shared state containing the question, retrieved documents, grades, answer, retries, citations, and trace

from typing import List, Literal
from typing_extensions import TypedDict
from pydantic import BaseModel, Field
from langchain_core.documents import Document