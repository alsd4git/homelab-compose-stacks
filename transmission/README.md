# Transmission Stack

A BitTorrent client with a web interface for easy management and monitoring.

## Features
- Web-based UI (Flood UI)
- Torrent download and management
- Watch directory for auto-add
- User authentication
- Persistent configuration and downloads

## Configuration

### Required Environment Variables
Create a `.env` file with the following variables:
```env
DOCKER_DATA_BASEFOLDER=/opt/docker/data
DOCKER_MEDIA_BASEFOLDER=/opt/docker/media
USERNAME=your_username
PASSWORD=your_password
```

## Ports

- 9091:9091 (mapped): Web UI (external)
- 51413:51413 (mapped): Torrent (TCP, external)
- 51413:51413/udp (mapped): Torrent (UDP, external)
- 9091 (exposed): Web UI (internal, for reverse proxy or internal access)
- 51413 (exposed): Torrent (TCP, internal, for internal container communication)
- 51413/udp (exposed): Torrent (UDP, internal, for internal container communication)

> **Note:** Both mapped and exposed ports are documented for clarity. The long-term plan is to reduce direct port exposure and use a reverse proxy for internal services.

## Usage

1. Configure your environment variables
2. Deploy the stack:
   ```bash
   docker compose up -d
   ```
3. Access the web interface at `http://your-server:9091`

## Security Notes
- Change the default web interface credentials
- Only expose necessary ports to the internet
- Keep Transmission updated
- Monitor logs for unusual activity

## Troubleshooting
- Check logs: `docker logs transmission`
- Port conflicts: Ensure no other services use the same ports
- Download issues: Verify volume permissions and free space

## Additional Resources
- [Transmission Documentation](https://github.com/transmission/transmission)
- [Flood UI Documentation](https://github.com/jesec/flood)
