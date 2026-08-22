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


@posts_router.get(
    "/{id}",
    response_model=PostBase,
    summary="Get post by ID",
)
def get_post(post_path: PostPath = post_id_path):
    return PostBase(id=post_path.id)


@posts_router.post(
    "",
    response_model=PostCreateResponse,
    summary="Create new post",
    status_code=201,
    description="""creates a new post, returns truncated content in message key""",
)
def create_post(data: PostCreateRequest):
    return PostCreateResponse(id=data.id, message=f"created post: {data.content[:120]}")


@posts_router.put(
    "/{id}",
    response_model=PostUpdateResponse,
    summary="Update full post body by id",
)
def update_post(
    data: PostUpdateRequest,
    post_path: PostPath = post_id_path,
):
    return PostUpdateResponse(
        id=post_path.id, message=f"updated post: {data.content[:120]}"
    )


@posts_router.delete(
    "/{id}",
    response_model=PostDeleteResponse,
    status_code=204,
)
def remove_post(post_path: PostPath = post_id_path):
    return PostDeleteResponse(id=post_path.id, message="deleted")
