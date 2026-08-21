from fastapi import APIRouter, Depends

from .schemas import PostCreationRequest, PostPath, PostUpdateRequest

posts_router = APIRouter(prefix="/posts")

post_id_path = Depends(PostPath)


@posts_router.get("/{id}")
def get_post(post_path: PostPath = post_id_path):
    return {"id": post_path.id}


@posts_router.post("/")
def create_post(data: PostCreationRequest):
    return {"id": data.id, "message": f"created post: {data.content[:120]}"}


@posts_router.put("/{id}")
def update_post(
    data: PostUpdateRequest,
    post_path: PostPath = post_id_path,
):
    return {"id": post_path.id, "message": f"updated post: {data.content[:120]}"}


@posts_router.delete("/{id}")
def remove_post(post_path: PostPath = post_id_path):
    return {"id": post_path.id, "message": "deleted"}
