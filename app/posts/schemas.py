from pydantic import BaseModel, Field


class PostPath(BaseModel):
    id: int = Field(gt=0)


class PostBase(BaseModel):
    id: int


class PostCreateRequest(PostBase):
    content: str


class PostCreateResponse(PostBase):
    message: str


class PostUpdateRequest(PostBase):
    content: str


class PostUpdateResponse(PostCreateResponse): ...


class PostDeleteResponse(PostBase):
    message: str
