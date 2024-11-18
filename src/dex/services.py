from fastapi import Depends

from langchain_core.runnables import RunnableSerializable
from langchain_core.messages import AIMessage

def chain_invoke(user_input: str,
                 chain: RunnableSerializable) -> AIMessage:
    """
    Invoke the chain
    """
    return chain.invoke(input={
        "image_data" : user_input,
    })