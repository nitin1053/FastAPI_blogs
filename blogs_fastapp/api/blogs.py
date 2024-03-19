from fastapi import APIRouter, Depends, HTTPException, status
from ..models.blog import BlogPost
from ..models.user import User
from ..database.db import db
from .auth import get_current_user

router = APIRouter()

@router.post("/blogs/")
async def create_blog(blog: BlogPost, current_user: User = Depends(get_current_user)):
    blog.author = current_user.username
    db.blog_posts.insert_one(blog.dict())
    return {"message": "Blog created successfully"}
