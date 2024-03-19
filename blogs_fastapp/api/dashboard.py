from fastapi import APIRouter, Depends, HTTPException, Query
from ..models.blog import BlogPost
from ..models.user import User
from ..database.db import db
from .auth import get_current_user
from typing import List

router = APIRouter()

@router.get("/dashboard/", response_model=List[BlogPost])
async def dashboard(
    current_user: User = Depends(get_current_user),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1)
):
    user_tags = current_user.tags
    # Fetch all blogs matching user's followed tags
    blogs = db.blog_posts.find({"tags": {"$in": user_tags}})
    
    
    sorted_blogs = sorted(blogs, key=lambda x: len(set(x['tags']) & set(user_tags)), reverse=True)
    
    # Pagination
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paginated_blogs = sorted_blogs[start_idx:end_idx]
    
    return paginated_blogs