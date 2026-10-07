from pathlib import Path
from typing import Iterable
from langchain_core.documents import Document 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from docx import Document as DocxDocument

SUPPORTED = {".pdf", ".txt", ".md", ".docx"}