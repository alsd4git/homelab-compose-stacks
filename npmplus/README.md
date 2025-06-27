# NPM Plus Stack

A reverse proxy solution with additional features, based on Nginx Proxy Manager.

## Features
- Web-based UI for managing reverse proxy hosts
- Automatic SSL certificate management
- Custom admin port
- IPv6 support (configurable)
- Persistent configuration and data storage

## Configuration

### Required Environment Variables
Create a `.env` file with the following variables:
```env
DOCKER_DATA_BASEFOLDER=/opt/docker/data
```

## Ports

- 808:80 (mapped): Public HTTP Port (external)
- 4434:443 (mapped): Public HTTPS Port (external)
- 85:82 (mapped): Admin Web UI (external)
- 80 (exposed): HTTP (internal, for reverse proxy or internal access)
- 443 (exposed): HTTPS (internal, for reverse proxy or internal access)
- 82 (exposed): Admin Web UI (internal, for reverse proxy or internal access)

> **Note:** Both mapped and exposed ports are documented for clarity. The long-term plan is to reduce direct port exposure and use a reverse proxy for internal services.

## Usage

1. Configure your environment variables
2. Deploy the stack:
   ```bash
   docker compose up -d
   ```
3. Access the admin UI at `http://your-server:85`

## Security Notes
- Change the default admin credentials
- Only expose necessary ports to the internet
- Keep NPM Plus updated
- Monitor logs for unusual activity

## Troubleshooting
- Check logs: `docker logs npmplus`
- Port conflicts: Ensure no other services use the same ports
- SSL issues: Verify certificate configuration

## Additional Resources
- [NPM Plus Documentation](https://github.com/ZoeyVid/NPMplus)
- [Docker Compose Documentation](https://docs.docker.com/compose/) 