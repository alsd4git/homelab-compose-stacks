# LAN Frontends Stack

Minimal private frontend stack exposed through the shared reverse-proxy network.

## Features

- **Web frontends**: lightweight PWA clients for Universo Gym and Dovesonole18.
- **Reverse-proxy ready**: joined to `npm_network` for published access.

## Configuration

### Environment Variables

This stack has no required environment variables.

## Services & Ports

| Service | Internal Port | Access Pattern | Notes |
| --- | --- | --- | --- |
| `universo-web` | `80` | `http://universo-web:80` | Universo Gym frontend on `npm_network`. |
| `dovesonole18` | `80` | `http://dovesonole18:80` | Dovesonole18 frontend on `npm_network`. |

## Container Images

| Service | Image |
| --- | --- |
| `universo-web` | `ghcr.io/alsd4git/universo-gym-client:main` |
| `dovesonole18` | `ghcr.io/alsd4git/dovesonole18:main` |

## Usage

1. Start the stack:

   ```bash
   docker compose up -d
   ```

2. Publish the service through Nginx Proxy Manager.

## Security Notes

- Keep the service behind the reverse proxy.
- If the image changes, update the published host in NPM and the stack documentation together.

## Additional Resources

- No project-specific external documentation is currently linked.
