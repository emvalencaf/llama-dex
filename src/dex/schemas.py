from pydantic import BaseModel


"""
Entry
"""
class DexEntry(BaseModel):
    name: str
    entry: str

"""
Completion Metadata will serve as metrics of performances and to measure price for each interaction
"""
class CompletionMetadata(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    prompt_time: float
    completion_time: float

"""

"""
class ChatCompletionResponse(BaseModel):
    data: DexEntry
    metadata: CompletionMetadata