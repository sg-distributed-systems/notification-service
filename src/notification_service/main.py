from core_logger import get_logger

logger = get_logger("notification-service")


def send_notification(user_id: str) -> None:
    logger.info("notification_sent", user_id=user_id)


if __name__ == "__main__":
    send_notification("user-123")
