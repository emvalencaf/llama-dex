from fastapi.exceptions import HTTPException

chat_completion_exception = HTTPException(status_code=500,
                                          detail="The model failed to generated a valid response, please try again")