from pydantic import BaseModel, Field


class PostPath(BaseModel):
    id: int = Field(gt=0)


class PostCreationRequest(PostPath):
    content: str


class PostUpdateRequest(BaseModel):
    content: str
