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

def llm():
    global _llm
    if _llm is None:
        if not settings.openai_api_key:
            raise RuntimeError("openai_api_key is missing")
        _llm = ChatOpenAI(
            model = settings.openai_model,
            temperature = 0,
            api_key = settings.openai_api_key,
        )
    return _llm

def web_search_tool():
    global _web_search
    if _web_search is None:
        if not settings.tavily_api_key:
            raise RuntimeError("tavily_api_key is missing")
        _web_search = TavilySearch(
            tavily_api_key = settings.tavily_api_key,
            max_results = 5,
            topic="general",
            include_answer=True,
            include_raw_content=False
        )
    return _web_search

def add_trace(state: AgentState, message: str):
    return [*state.get("trace",[]), message]