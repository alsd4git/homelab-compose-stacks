# Immich Stack

A self-hosted photo and video backup solution with a modern web interface and machine learning features.

## Features
- Web-based UI for photo and video management
- Machine learning for photo recognition
- Redis and Postgres integration
- Persistent configuration and media storage

## Configuration

### Required Environment Variables
Create a `.env` file with the following variables:
```env
UPLOAD_LOCATION=/path/to/upload
DB_DATA_LOCATION=/path/to/dbdata
IMMICH_VERSION=release
DB_PASSWORD=your_db_password
DB_USERNAME=your_db_user
DB_DATABASE_NAME=your_db_name
```

## Ports

- 2283:2283 (mapped): Web UI/API (external)
- 2283 (exposed): Web UI/API (internal, for reverse proxy or internal access)

> **Note:** Both mapped and exposed ports are documented for clarity. The long-term plan is to reduce direct port exposure and use a reverse proxy for internal services.

## Usage

1. Configure your environment variables
2. Deploy the stack:
   ```bash
   docker compose up -d
   ```
3. Access the web interface at `http://your-server:2283`

## Security Notes
- Change the default admin credentials
- Only expose necessary ports to the internet
- Keep Immich updated
- Monitor logs for unusual activity

## Troubleshooting
- Check logs: `docker logs immich_server`
- Port conflicts: Ensure no other services use the same ports
- Database issues: Verify volume permissions and free space

## Additional Resources
- [Immich Documentation](https://immich.app/docs/)
- [Immich GitHub](https://github.com/immich-app/immich)
- [Docker Compose Documentation](https://docs.docker.com/compose/) 