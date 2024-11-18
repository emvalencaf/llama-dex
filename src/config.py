from os import getenv
from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(filename='.env',
                        usecwd=True),)

class GlobalConfig(BaseSettings):
    API_V_STR: str = str(getenv("API_V_STR",'/api/v1'))
    
    BACKEND_HOST: str = str(getenv('BACKEND_HOST', 'localhost'))
    BACKEND_PORT: int = int(getenv('BACKEND_PORT', 8000))
    
    ENVIRONMENT: str = str(getenv("ENVIRONMENT", "DEVELOPMENT"))
    
    FRONTEND_URL: str = str(getenv("FRONTEND_URL", "http://locallhost:3000"))
    
    class Config:
        case_sensitive = True
        

global_settings: GlobalConfig = GlobalConfig()