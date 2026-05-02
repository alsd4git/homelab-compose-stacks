# Automation Stack

Docker event automation, image monitoring, and automatic container updates through Telegram.

## Features

- **Docker Telegram Notifier**: sends container lifecycle events to Telegram.
- **Diun**: watches container images for updates and reports them to Telegram.
- **Watchtower**: updates running containers on a schedule and reports results to Telegram.

## Configuration

### Environment Variables

This stack requires a `.env` file for configuration. Copy the example file, then set the Telegram credentials and data root:

```bash
cp .env.example .env
```

Key variables:

- `DOCKER_DATA_BASEFOLDER`: persistent data root
- `TELEGRAM_BOT_TOKEN`: Telegram bot token
- `TELEGRAM_CHAT_ID`: Telegram chat ID

## Services & Ports

| Service | Access Pattern | Notes |
| --- | --- | --- |
| Diun | internal only | No published web UI; consumes the Docker socket. |
| Docker Telegram Notifier | internal only | No published web UI; consumes the Docker socket. |
| Watchtower | internal only | No published web UI; consumes the Docker socket. |

## Container Images

| Service | Image |
| --- | --- |
| Diun | `crazymax/diun:latest` |
| Docker Telegram Notifier | `lorcas/docker-telegram-notifier:latest` |
| Watchtower | `nickfedor/watchtower:latest` |

## Usage

1. Copy `.env.example` to `.env`.
2. Fill in `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`.
3. Deploy the stack:

   ```bash
   docker compose up -d
   ```

## Security Notes

- All services mount `/var/run/docker.sock`, so deploy only in trusted networks.
- The Telegram token and chat ID must live in `.env`, not in the compose file.
- Watchtower runs on a schedule and can update containers automatically, so keep the container allowlist intentional.

## Additional Resources

- [Docker Security Documentation](https://docs.docker.com/engine/security/)
- [Diun Documentation](https://crazymax.dev/diun/)
- [Docker Telegram Notifier](https://github.com/luc-ass/docker-telegram-notifier)
- [Watchtower Documentation](https://containrrr.dev/watchtower/)
