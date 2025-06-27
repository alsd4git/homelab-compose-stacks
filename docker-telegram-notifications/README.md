# Docker Telegram Notifications Stack

This stack provides a comprehensive solution for monitoring Docker containers and receiving notifications via Telegram. It combines three powerful tools:

## Components

### 1. Docker Telegram Notifier
- **Image**: [lorcas/docker-telegram-notifier](https://github.com/luc-ass/docker-telegram-notifier)
- **Purpose**: Sends notifications about Docker container events (start, stop, die, etc.) to Telegram
- **Documentation**: [GitHub Repository](https://github.com/luc-ass/docker-telegram-notifier)

### 2. Diun
- **Image**: [crazymax/diun](https://github.com/crazy-max/diun)
- **Purpose**: Docker image update notifier that monitors Docker images for updates
- **Documentation**: [Official Documentation](https://crazymax.dev/diun/)

### 3. Watchtower
- **Image**: [containrrr/watchtower](https://github.com/containrrr/watchtower)
- **Purpose**: Automatically updates running Docker containers to their latest version
- **Documentation**: [Official Documentation](https://containrrr.dev/watchtower/)

## Configuration

1. Create a `.env` file based on `.env.example`
2. Set up a Telegram bot using [@BotFather](https://t.me/botfather)
3. Get your chat ID (you can use [@userinfobot](https://t.me/userinfobot))
4. Configure the schedule for updates in the compose file

## Environment Variables

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token from @BotFather
- `TELEGRAM_CHAT_ID`: Your Telegram chat ID
- `DOCKER_DATA_BASEFOLDER`: Base directory for persistent data (default: /opt/docker/data)

## Usage

1. Configure your environment variables
2. Deploy the stack:
   ```bash
   docker compose up -d
   ```

## Maintenance

The stack is configured to:
- Run Watchtower updates every Monday, Wednesday, and Friday at 1 PM
- Check for image updates every 6 hours with Diun
- Send notifications for all Docker events
- Automatically restart services if they fail 