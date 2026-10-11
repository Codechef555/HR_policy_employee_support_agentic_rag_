from pathlib import Path 
from fastapi import FastAPI, Request 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import staticfiles
from fastapi.templating import Jinja2Templates
from app.api.routes import router 
from app.core.config import get_settings, BASE_DIR
from app.core.logging import configure_logging
from app.services.audit import init_db
