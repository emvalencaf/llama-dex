from fastapi import APIRouter, Depends, status

from langchain_core.runnables import RunnableSerializable


from dex.dependencies import get_chain, get_image_base64
from dex.schemas import ChatCompletionResponse, CompletionMetadata, DexEntry
from dex.services import chain_invoke
from dex.utils import json_parse
from dex.exceptions import chat_completion_exception

router = APIRouter(tags=['dex entry'])

@router.post(
    "/chat_completion",
    summary="Processes a base64 input and returns a pokedex's entry like response",
    response_description="Data processed by the model and execution metadata",
    response_model=ChatCompletionResponse,
    status_code=200,
    responses={
        status.HTTP_200_OK: {
            "description": "Successful response",
            "content": {
                "application/json": {
                    "example": {
                        "data": {
                            "name": "Human",
                            "entry": "Humans are a species of primates characterized by advanced cognitive abilities...",
                            "identified": True,
                        },
                        "metadata": {
                            "prompt_tokens": 728,
                            "completion_tokens": 108,
                            "prompt_time": 0.048733782,
                            "completion_time": 0.167690731,
                        },
                    }
                }
            },
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Error in processing user request due to the lack of file",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "type": "missing",
                                "loc": ["body", "file"],
                                "msg": "Field required",
                                "input": "null",
                            }
                        ]
                    }
                }
            },
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Internal server error due to an invalid JSON response generated by the model",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "The model failed to generate a valid response, please try again"
                    }
                }
            },
        },
    },
)
def chat_completion(base64_content: str = Depends(get_image_base64),
                    chain: RunnableSerializable = Depends(get_chain)):
    
    # invoke llm chat completion of the image passed
    response = chain_invoke(user_input=base64_content,
                            chain=chain)
        
    json_parsed = json_parse(response.content)
    
    # Entry must always be a JSON
    # Since Gen AI output can be different than a JSON it's necessary to treat    
    try:
        entry = DexEntry(**json_parsed) if json_parsed else None
    except Exception as er:
        print("The JSON generated by the model is not valid. Please check the format and try again.")
        print(er)
        raise chat_completion_exception
    
    metadata_dict: dict = response.response_metadata["token_usage"]
    
    completion_tokens: int = metadata_dict.get("completion_tokens")
    prompt_tokens: int = metadata_dict.get("prompt_tokens")
    completion_time: float = metadata_dict.get("completion_time")
    prompt_time: float = metadata_dict.get("prompt_time")
    
    metadata = CompletionMetadata(completion_time=completion_time,
                                  completion_tokens=completion_tokens,
                                  prompt_tokens=prompt_tokens,
                                  prompt_time=prompt_time)
    
    if not entry:
        raise chat_completion_exception
    
    return { "data": entry, "metadata" : metadata }