# Tracearr Stack

Traceability and media import stack built around PostgreSQL 18 and Redis, with the web UI attached to the shared reverse-proxy network.

## Features

- **Web UI**: internal application interface exposed through `npm_network`.
- **PostgreSQL 18**: primary relational store on a private backend network.
- **Redis cache**: internal cache and queue backend.
- **Named volumes**: persistent storage uses Docker-managed volumes instead of host bind mounts.

## Configuration

### Environment Variables

Copy the example file to `.env`, then generate strong secrets for the database and application cookies:

```bash
cp .env.example .env
openssl rand -hex 32
```

Key variables:

- `DB_PASSWORD`
- `JWT_SECRET`
- `COOKIE_SECRET`
- `CORS_ORIGIN`
- `LOG_LEVEL`
- `TZ`

## Services & Ports

| Service | Internal Port | Access Pattern | Role |
| --- | --- | --- | --- |
| `tracearr` | `3000` | `http://tracearr:3000` | Web UI |
| `tracearr-db` | `5432` | internal only | PostgreSQL 18 |
| `tracearr-redis` | `6379` | internal only | Redis cache |

## Container Images

| Service | Image |
| --- | --- |
| Tracearr | `ghcr.io/connorgallopo/tracearr:latest` |
| PostgreSQL | `timescale/timescaledb-ha:pg18.1-ts2.25.0` |
| Redis | `redis:8-alpine` |

## Usage

1. Copy `.env.example` to `.env`.
2. Generate and store the secrets in `.env`.
3. Start the stack:

   ```bash
   docker compose up -d
   ```

## Security Notes

- Keep the database and cookie secrets in `.env`.
- PostgreSQL and Redis remain on the private `tracearr_network`.
- The web UI is intended to be published only through the reverse proxy.

## Additional Resources

- [Tracearr GitHub](https://github.com/connorgallopo/tracearr)
