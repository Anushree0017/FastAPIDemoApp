from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import base, session
from app.db.session import engine, get_db
from app.schemas.user_request import UserCreateRequest, UserUpdateRequest
from app.schemas.user_response import UserResponse
from app.api.dependencies import user_service
from app.service.user_service import UserService
from app.celery_app.chains import run_chain

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/{user_id}/run")
def run_user_chain(
        user_id:int
):
    result = run_chain(user_id)
    return {"message": "User processing started", "chain_id": result.id}

@router.post("/", response_model=str)
def create_user(
        user_request : UserCreateRequest,
        db : Session = Depends(get_db),
        service : UserService = Depends(user_service)
):
    service.create_user(db, user_request)
    return "User created"

@router.get("/", response_model=list[UserResponse])
def get_users(
        skip:int=0, limit:int=0,
        db: Session = Depends(get_db),
        service:UserService = Depends(user_service)
):
    return service.get_all_users(db, skip, limit)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(
        user_id:int,
        db:Session = Depends(get_db),
        service:UserService = Depends(user_service)
):
    user= service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User not found with id : {user_id}")
    return user

@router.put("/{user_id}", response_model=str)
def update_user(
        user_id:int,
        user_request:UserUpdateRequest,
        db:Session = Depends(get_db),
        service:UserService = Depends(user_service)
):
    user = service.update_user(db, user_id, user_request)
    return "User updated"

@router.delete("/{user_id}")
def delete_user(
        user_id : int,
        db:Session = Depends(get_db),
        service:UserService = Depends(user_service)
):
    service.delete_user(db, user_id)
    return "User deleted."