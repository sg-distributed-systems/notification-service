# notification-service

Sends notifications to users via various channels.

## Why this repo exists

A dedicated notification service decouples message delivery from business logic, enabling support for multiple channels (email, SMS, push) without modifying other services.

## Core Components

### `send_notification(user_id: str)`
Sends a notification to the specified user.

**Logs:**
- `notification_sent` — Logged when a notification is successfully delivered

### `load_config(service_name: str) -> ServiceConfig`
Loads service configuration from environment variables including `APP_ENV` and `SHUTDOWN_TIMEOUT_SECONDS`.

### `AppError`
Base exception class for application errors. Provides `to_log_fields()` for structured error logging.

### `install_signal_handlers(service_logger_name: str)`
Installs SIGINT/SIGTERM handlers for graceful shutdown with logging.

### `init_correlation_id() -> str`
Initializes a correlation ID from the `CORRELATION_ID` environment variable or generates a UUID4.

## HTTP Interface

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/healthz` | GET | Liveness probe |
| `/readyz` | GET | Readiness probe |
| `/notifications/send` | POST | Sends a notification to a user |

### Running the service

```bash
uvicorn src.notification_service.app:app --host 0.0.0.0 --port 8006
```
