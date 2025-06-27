# DDNS Updater Stack

This stack provides a unified solution for updating multiple Dynamic DNS (DDNS) services. It uses [ddns-updater](https://github.com/qdm12/ddns-updater) to manage multiple DDNS providers simultaneously.

## Features

- Supports multiple DDNS providers:
  - Dynu
  - Dynv6
  - DuckDNS
- Web UI for monitoring and management
- Telegram notifications for updates
- Automatic IP detection
- Configurable update intervals

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Base directory for persistent data
DOCKER_DATA_BASEFOLDER=/opt/docker/data

# Telegram notifications
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id

# Dynu configuration
DYNU_DOMAIN=your.domain
DYNU_USERNAME=your_username
DYNU_PASSWORD=your_password

# Dynv6 configuration
DYN6_DOMAIN=your.domain
DYN6_TOKEN=your_token

# DuckDNS configuration
DUCK_HOST=your_host
DUCK_TOKEN=your_token
```

### Update Settings

- Update period: Every 60 minutes
- Cooldown period: 5 minutes
- Timezone: Europe/Rome
- Log level: Debug
- Web UI port: 8001

## Ports

- **8001:8000** (mapped): Web UI for monitoring and management (accessible externally)
- **8000** (exposed): Internal Web UI port for reverse proxy or internal access

> **Note:** The long-term plan is to reduce direct port exposure and use a reverse proxy for internal services. Both mapped and exposed ports are documented for clarity.

## Usage

1. Configure your environment variables
2. Deploy the stack:
   ```bash
   docker compose up -d
   ```
3. Access the web UI at `http://your-server:8001`

## Monitoring

The service provides:
- Web UI for real-time monitoring
- Telegram notifications for updates
- Detailed logs for troubleshooting

## Troubleshooting

1. Check logs:
   ```bash
   docker logs ddns-updater
   ```

2. Common issues:
   - IP detection failures: Check your network configuration
   - Update failures: Verify provider credentials
   - Telegram notifications: Ensure bot token and chat ID are correct

## Security Notes

- The service requires access to your DDNS provider credentials
- Web UI is exposed on port 8001
- Consider using a reverse proxy for the web UI
- Keep your environment variables secure 