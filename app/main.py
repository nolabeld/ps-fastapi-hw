from fastapi import FastAPI

from .posts import routes

app = FastAPI(
    title="Posts management API",
    openapi_tags=[{"name": "Posts", "description": "posts crud operations"}],
    version="0.1.0",
)

app.include_router(routes.posts_router)
