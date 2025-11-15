from celery import Celery
import os

broker_url = os.getenv("CELERY_BROKER_URL")
backend_url = "rpc://"

celery_app = Celery(
    "celery_app",
    broker=broker_url,
    backend=backend_url,
    include=["app.celery_app.tasks"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Kolkata",
    enable_utc=False,
)