from sqlalchemy.orm import Session
from app.models import user
from app.schemas.user_request import UserCreateRequest, UserUpdateRequest
from fastapi import HTTPException

class UserRepository:

    def get_by_id(self, db:Session, id:int) -> user.User:
        return db.query(user.User).filter(user.User.id==id).first()
    
    def get_all(self, db:Session, skip:int=0, limit:int=10):
        return db.query(user.User).offset(skip).limit(limit).all()

    def create(self, db:Session, user_dto: UserCreateRequest):
        db_user = user.User(**user_dto.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    
    def update(self, db:Session, user_id:int, user_dto:UserUpdateRequest):
        user = self.get_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail=f"User not found with id : {user_id}")
        for field, value in user_dto.dict(exclude_unset=True).items():
            setattr(user, field, value)
        db.commit()
        db.refresh(user)


    def delete(self, db:Session, user_id:int):
        user = self.get_by_id(db, user_id)
        if not user:
            return None
        db.delete(user)
        db.commit()