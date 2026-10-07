from app.core.config import get_settings

settings = get_settings()

print(f'App name: {settings.app_name}')
print(f'Web search Tavily name: {settings.tavily_api_key}')