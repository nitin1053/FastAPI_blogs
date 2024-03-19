from fastapi import APIRouter, Depends, HTTPException, status
from passlib.context import CryptContext
from ..models.user import User
from ..database.db import db
from .auth import create_access_token

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register/")
async def register(user: User):
    user_data = db.users.find_one({"username": user.username})
    if user_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    hashed_password = pwd_context.hash(user.password)
    user_data = user.dict()
    user_data["password"] = hashed_password
    db.users.insert_one(user_data)
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
