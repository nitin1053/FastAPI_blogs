
from fastapi import APIRouter, BackgroundTasks, HTTPException, Depends  # Import Depends
from typing import List
from pydantic import BaseModel
from ..models.blog import BlogPost
from ..models.user import User
from ..database.db import db
from .auth import get_current_user

router = APIRouter()


class Comment(BaseModel):
    text: str
    user_id: str


@router.post("/blogs/{post_id}/comment/", response_model=Comment)
async def add_comment(post_id: str, comment: Comment, current_user: User = Depends(get_current_user)):
    # Check if the blog post exists
    existing_blog = db.blog_posts.find_one({"_id": post_id})
    if not existing_blog:
        raise HTTPException(status_code=404, detail="Blog post not found")

    comment_data = comment.dict()
    comment_data["user_id"] = current_user.id
    db.blog_posts.update_one({"_id": post_id}, {"$push": {"comments": comment_data}})

    

    return comment

@router.get("/users/{user_id}/blogs/", response_model=List[BlogPost])
async def get_user_blogs(user_id: str):
    # Fetch blogs by user ID
    blogs = db.blog_posts.find({"author_id": user_id})
    return list(blogs)
