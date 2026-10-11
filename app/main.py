from pathlib import Path 
from fastapi import FastAPI, Request 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import staticfiles
from fastapi.templating import Jinja2Templates