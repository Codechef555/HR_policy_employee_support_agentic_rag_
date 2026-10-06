from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    app_name: str = "Enterprise HR Policy Agentic RAG Copilot"
    app_env: str = "development"
    openai_api_key: str = ""
    tavily_api_key: str = ""
    pinecone_api_key: str = ""
    pinecone_index_name: str = "fde-hr-policy-rag"
    pinecone_namespace: str = "company-hr-kb"
    embedding_model: str = "text-embedding-3-small"
    openai_model: str = "gpt-4o-mini"
    top_k: int = 4
    max_retries: int = 1