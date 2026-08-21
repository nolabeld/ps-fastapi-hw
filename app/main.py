from fastapi import FastAPI

from app.posts import routes

app = FastAPI()

app.include_router(routes.posts_router)
