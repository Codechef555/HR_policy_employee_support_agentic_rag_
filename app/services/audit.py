import json
import sqlite3
from datetime import datetime, timezone
from app.core.config import get_settings

settings = get_settings()

def init_db() -> None:
    con = sqlite3.connect(settings.audit_db_path)