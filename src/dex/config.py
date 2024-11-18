from os import getenv
from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(filename='.env',
                        usecwd=True),)

class DexConfig(BaseSettings):
    """
    LLAMADex configuration containing the keys for inference the LLAMA model at GROQ services
    """
    GROQ_API_KEY: str = str(getenv('GROQ_API_KEY',''))
    if not GROQ_API_KEY:
        raise Exception("You must provide a GROQ's api key for the LLAMA Dex work")
    
    MODEL_NAME: str = str(getenv('MODEL_NAME', 'llama-3.2-11b-vision-preview'))
    
    if not MODEL_NAME in ('llama-3.2-11b-vision-preview',
                          'llama-3.2-90b-vision-preview'):
        raise Exception("You must set a multimodal llm modal for the LLAMA Dex work")
    
    
    class Config:
        case_sensitive = True
        
dex_settings: DexConfig = DexConfig()