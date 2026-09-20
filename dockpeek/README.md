# Dockpeek Stack

Docker container overview using a restricted socket proxy instead of mounting the Docker socket directly into the web app.

## Configuration

Copy `.env.example` to `.env` and set the login credentials and secret key:

```bash
cp .env.example .env
```

Key variables:

- `DOCKPEEK_SECRET_KEY`
- `DOCKPEEK_USERNAME`
- `DOCKPEEK_PASSWORD`

## Services & Ports

| Service | Port | Notes |
| --- | --- | --- |
| Dockpeek | `3420:8000` | Web UI via direct host mapping. |
| Socket Proxy | internal only | Exposes only the Docker API sections Dockpeek needs. |

## Security Notes

- Keep credentials in `.env`; do not hardcode them in the compose file.
- The socket proxy limits Docker API access, but it still talks to the Docker daemon. Keep this stack on trusted hosts only.

## Additional Resources

- [Dockpeek](https://github.com/dockpeek/dockpeek)
- [linuxserver/socket-proxy](https://github.com/linuxserver/docker-socket-proxy)
