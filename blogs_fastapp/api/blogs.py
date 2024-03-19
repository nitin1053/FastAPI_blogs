# api/blogs.py
from fastapi import APIRouter, Depends, HTTPException
from ..models.blog import BlogPost
from ..models.user import User
from ..database.db import db
from .auth import get_current_user
from typing import List

router = APIRouter()

@router.post("/blogs/")
async def create_blog(blog: BlogPost, current_user: User = Depends(get_current_user)):
    blog.author = current_user.username
    db.blog_posts.insert_one(blog.dict())
    return {"message": "Blog created successfully"}

# api/blogs.py
@router.get("/blogs/", response_model=List[BlogPost])
async def read_all_blogs():
    return list(db.blog_posts.find())

@router.get("/blogs/{post_id}", response_model=BlogPost)
async def read_blog(post_id: str):
    blog = db.blog_posts.find_one({"_id": post_id})
    if blog:
        return blog
    raise HTTPException(status_code=404, detail="Blog not found")

# api/blogs.py
@router.put("/blogs/{post_id}")
async def update_blog(post_id: str, blog: BlogPost, current_user: User = Depends(get_current_user)):
    existing_blog = db.blog_posts.find_one({"_id": post_id})
    if existing_blog["author"] != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to update this blog post")
    db.blog_posts.update_one({"_id": post_id}, {"$set": blog.dict()})
    return {"message": "Blog updated successfully"}

# api/blogs.py
@router.delete("/blogs/{post_id}")
async def delete_blog(post_id: str, current_user: User = Depends(get_current_user)):
    existing_blog = db.blog_posts.find_one({"_id": post_id})
    if existing_blog["author"] != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to delete this blog post")
    db.blog_posts.delete_one({"_id": post_id})
    return {"message": "Blog deleted successfully"}
