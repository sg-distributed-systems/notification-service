from core_logger import get_logger

logger = get_logger("notification-service")


def send_notification(user_id: str) -> None:
    logger.info("notification_sent", user_id=user_id)


def main() -> None:
    send_notification("user-123")


if __name__ == "__main__":
    main()
