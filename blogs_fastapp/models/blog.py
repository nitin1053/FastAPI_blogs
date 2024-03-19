from typing import List
from pydantic import BaseModel

class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    tags: List[str] = []
