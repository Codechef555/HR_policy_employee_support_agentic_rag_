# — Build the main Agentic RAG workflow: Route → Retrieve → Grade → Web Search → Rewrite/Retry → Generate Answer
import logging
from typing import Literal
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.graph import StateGraph, START, END
from app.core.config import get_settings
from app.rag.state import AgentState, RouteDecision, EvidenceGrade
from app.rag.vectorstore import get_retriever

logger = logging.get_logger(__name__)
settings = get_settings()

_llm = None
_web_search = None