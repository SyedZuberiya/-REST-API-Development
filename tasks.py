from .celery_worker import celery_app
import logging

@celery_app.task
def send_notification(message: str):
    logging.info(f"Notification: {message}")
    return message
