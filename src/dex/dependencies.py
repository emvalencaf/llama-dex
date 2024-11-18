from fastapi import Depends, File, UploadFile
from langchain_groq.chat_models import ChatGroq
import base64

# dex module
from dex.config import dex_settings
from dex.prompts.dex_completion import get_dex_completion_prompt

def get_model(max_token: int = 200,
              temperature: float = 0,
              stream: bool = False):
    return ChatGroq(temperature=temperature,
                    max_tokens=max_token,
                    streaming=stream,
                    model=dex_settings.MODEL_NAME,
                    api_key=dex_settings.GROQ_API_KEY)
    
def get_chain(model: ChatGroq = Depends(get_model)):
    prompt = get_dex_completion_prompt()
    
    return prompt | model

async def get_image_base64(file: UploadFile = File(...)):
    file_content = await file.read()
    
    base64_encoded = base64.b64encode(file_content).decode("utf-8")
    
    return base64_encoded