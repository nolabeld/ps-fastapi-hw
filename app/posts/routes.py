from fastapi import APIRouter

posts_router = APIRouter(prefix="/posts")


@posts_router.get("/{id}")
def get_post(id: int):
    return {"id": id}


@posts_router.post("/")
def create_post():
    return ""


@posts_router.put("/{id}")
def update_post(id: int):
    return id


@posts_router.delete("/{id}")
def remove_post(id: int):
    return "deleted"
