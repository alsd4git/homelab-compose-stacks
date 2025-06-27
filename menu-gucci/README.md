# Menu Gucci Stack

A Telegram bot for menu management and notifications.

## Features
- Telegram bot for menu management
- User whitelisting
- Persistent log storage

## Configuration

### Required Environment Variables
Create a `.env` file with the following variables:
```env
DOCKER_DATA_BASEFOLDER=/opt/docker/data
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_WHITELIST_USERS=your_whitelisted_users
```

## Ports

- No ports are exposed. This service is a Telegram bot and does not provide a web UI or API.

> **Note:** If a web UI or API is added in the future, mapped and exposed ports will be documented. The long-term plan is to reduce direct port exposure and use a reverse proxy for internal services.

## Usage

1. Configure your environment variables
2. Deploy the stack:
   ```bash
   docker compose up -d
   ```
3. Interact with the bot via Telegram

## Security Notes
- Keep your Telegram bot token secure
- Only whitelist trusted users
- Monitor logs for unusual activity

## Troubleshooting
- Check logs: `docker logs python-menu-gucci`
- Bot not responding: Verify bot token and whitelisted users

## Additional Resources
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Docker Compose Documentation](https://docs.docker.com/compose/) 