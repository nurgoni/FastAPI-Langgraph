from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.users import UserCreate, ShowUser
from db.session import get_db
from repository.users import (
    create_new_user, 
    get_all_users, 
    get_user_with_id
)


router = APIRouter()


@router.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user

@router.get("/users", response_model=list[ShowUser], status_code=status.HTTP_200_OK)
def fetch_all_users(db: Session = Depends(get_db)):
    users = get_all_users(db=db)
    return users

@router.get("/users/{id}", response_model=ShowUser, status_code=status.HTTP_200_OK)
def fetch_user_with_id(id: int, db: Session = Depends(get_db)):
    user = get_user_with_id(id=id, db=db)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
        )
    return user

