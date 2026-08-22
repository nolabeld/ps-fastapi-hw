from fastapi import APIRouter, Depends

from .schemas import (
    PostBase,
    PostCreateRequest,
    PostCreateResponse,
    PostDeleteResponse,
    PostPath,
    PostUpdateRequest,
    PostUpdateResponse,
)

posts_router = APIRouter(prefix="/posts", tags=["Posts"])

post_id_path = Depends(PostPath)


@posts_router.get("/{id}", response_model=PostBase)
def get_post(post_path: PostPath = post_id_path):
    return PostBase(id=post_path.id)


@posts_router.post("", response_model=PostCreateResponse)
def create_post(data: PostCreateRequest):
    return PostCreateResponse(id=data.id, message=f"created post: {data.content[:120]}")


@posts_router.put("/{id}", response_model=PostUpdateResponse)
def update_post(
    data: PostUpdateRequest,
    post_path: PostPath = post_id_path,
):
    return PostUpdateResponse(
        id=post_path.id, message=f"updated post: {data.content[:120]}"
    )


@posts_router.delete("/{id}", response_model=PostDeleteResponse)
def remove_post(post_path: PostPath = post_id_path):
    return PostDeleteResponse(id=post_path.id, message="deleted")
