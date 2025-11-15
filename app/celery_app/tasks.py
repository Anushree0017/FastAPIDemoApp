from app.celery_app.workers import celery_app
import logging

@celery_app.task
def task1(user_id: int):
    logging.info(f"Running task 1 for user {user_id}")
    return {"user_id": user_id, "result": "task1 done"}

@celery_app.task
def task2(prev_result):
    logging.info(f"Running task 2 with input: {prev_result}")
    return {"result": "task2 done"}

@celery_app.task
def task3(prev_result):
    logging.info(f"Running task 3 with input: {prev_result}")
    return {"result": "task3 done"}

@celery_app.task
def task4(prev_result):
    logging.info(f"Running task 4 with input: {prev_result}")
    return {"result": "task4 done"}