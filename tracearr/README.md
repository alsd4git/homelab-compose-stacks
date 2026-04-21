# Tracearr Stack

Tracearr is a self-hosted traceability and media import stack with PostgreSQL 18 and Redis. This version is structured for a reverse-proxied homelab setup and keeps the web UI on `npm_network`.

## Notes

- This compose uses PostgreSQL 18 and is intended for new installations only.
- The web UI is exposed internally on port `3000`.
- PostgreSQL and Redis stay on the private `tracearr_network`.
- Persistent data uses Docker-managed named volumes, not host bind mounts.
- Runtime secrets live in `.env`, not in the compose file.

## Configuration

1. Copy `.env.example` to `.env`.
2. Generate strong secrets for `DB_PASSWORD`, `JWT_SECRET`, and `COOKIE_SECRET`.
3. Keep the generated secrets in `.env`.

Suggested secret generation:

```bash
openssl rand -hex 32
```

## Services

| Service | Internal Port | Access Pattern | Role |
| --- | ---: | --- | --- |
| `tracearr` | `3000` | `http://tracearr:3000` | Web UI |
| `tracearr-db` | `5432` | internal only | PostgreSQL 18 |
| `tracearr-redis` | `6379` | internal only | Redis cache |

## Storage Layout

- `tracearr_backups`
- `tracearr_timescale_data`
- `tracearr_redis_data`

## Usage

```bash
docker compose up -d
```
