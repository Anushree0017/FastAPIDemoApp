from celery import chain
from app.celery_app.tasks import *

def run_chain(user_id: int):
    task_chain = chain(
        task1.s(user_id),
        task2.s(),
        task3.s(),
        task4.s()
    )
    return task_chain.apply_async()