# main.py
from fastapi import FastAPI
from .api import auth, blogs, users, dashboard, bonus

app = FastAPI()

app.include_router(auth.router)
app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(dashboard.router)
app.include_router(bonus.router)  # Include the bonus routes
