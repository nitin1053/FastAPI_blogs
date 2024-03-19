from typing import List
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str
    tags: List[str] = []
