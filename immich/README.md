# Immich Stack

A self-hosted photo and video backup solution with a modern web interface and machine learning features.

## Features

- **Web UI**: photo and video management interface.
- **Machine learning**: recognition and indexing support.
- **Database backend**: Redis and PostgreSQL backing services.
- **Persistent storage**: separate upload and database paths.

## Configuration

### Environment Variables

This stack requires a `.env` file for configuration. A complete and recommended set of variables can be found in the `.env.example` file.

**To get started:**

1. Copy the `.env.example` file to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file and edit the variables to match your environment.

**Key variables include:**

- `UPLOAD_LOCATION`: The absolute path on your host machine where Immich will store uploaded photos and videos.
- `DB_DATA_LOCATION`: The absolute path for storing PostgreSQL data.
- `IMMICH_VERSION`: The version of Immich to run. It is recommended to use `v3` for the latest stable release, which supports in-app updates.
- `DB_PASSWORD`: A secure password for the database.
- `DB_USERNAME`: The database user (defaults to `postgres`).
- `DB_DATABASE_NAME`: The name of the database (defaults to `immich`).

## Services & Ports

| Service | Internal Port | Access Pattern | Notes |
| --- | --- | --- | --- |
| Immich Server | `2283` | `http://immich_server:2283` | Web UI/API on `npm_network`. |
| Immich Machine Learning | internal only | internal only | ML service for recognition and embedding generation. |
| Redis | internal only | internal only | Cache and queue backend. |
| PostgreSQL | internal only | internal only | Primary database. |

> **Note:** The stack is intended to be reached through the reverse proxy on `npm_network`.

## Container Images

| Service          | Image                                                            |
| ---------------- | ---------------------------------------------------------------- |
| Immich Server    | `ghcr.io/immich-app/immich-server`                               |
| Machine Learning | `ghcr.io/immich-app/immich-machine-learning`                     |
| Redis            | `docker.io/valkey/valkey:9`                                      |
| Database         | `ghcr.io/immich-app/postgres:14-vectorchord0.4.3-pgvectors0.2.0` |

## Usage

1. Configure your environment variables
2. Deploy the stack:

   ```bash
   docker compose up -d
   ```

3. Publish the web interface through Nginx Proxy Manager using the host you assign for Immich.

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
