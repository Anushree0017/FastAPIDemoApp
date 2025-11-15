from app.service.user_service import UserService

def user_service() -> UserService:
    return UserService()