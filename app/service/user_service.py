from sqlalchemy.orm import Session
from app.repository.user_repo import UserRepository
from app.schemas.user_request import UserCreateRequest, UserUpdateRequest

class UserService :
    def __init__(self):
        self.repo = UserRepository()

    def get_user_by_id(self, db:Session, user_id : int):
        return self.repo.get_by_id(db, user_id)
    
    def get_all_users(self, db:Session, skip:int, limit:int):
        return self.repo.get_all(db, skip, limit)
    
    def create_user(self, db:Session, user_dto : UserCreateRequest):
        self.repo.create(db, user_dto)

    def update_user(self, db:Session, user_id:int, user_dto : UserUpdateRequest):
        self.repo.update(db, user_id, user_dto)
    
    def delete_user(self, db:Session, user_id:int):
        self.repo.delete(db, user_id)