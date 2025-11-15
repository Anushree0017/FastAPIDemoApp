from fastapi import FastAPI
from app.api.v1 import user_router
from app.db import base
from app.db.session import engine
from app.core.config import settings

# Create DB tables (optional if using Alembic)
base.Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(title=settings.APP_NAME)

# Include Routers
app.include_router(user_router.router)

@app.get("/")
def root():
    return {"message": f"Welcome to {settings.APP_NAME}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=True)
