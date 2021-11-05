import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
api_key = os.getenv("API_KEY")

class Settings:
    PROJECT_TITLE: str = "Weather"
    PROJECT_VERSION: str = "0.1.1"
    
    API_KEY: str = os.getenv("API_KEY")

settings = Settings()