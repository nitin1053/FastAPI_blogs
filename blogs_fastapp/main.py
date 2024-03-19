from fastapi import FastAPI
from .api import auth, blogs, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(blogs.router)
app.include_router(users.router)
