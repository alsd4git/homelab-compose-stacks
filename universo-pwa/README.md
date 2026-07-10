# Universo PWA Stack

Minimal frontend stack for `universo-web` exposed through the shared reverse-proxy network.

## Features

- **Single web frontend**: lightweight PWA front end for the Universo service.
- **Reverse-proxy ready**: joined to `npm_network` for published access.

## Configuration

### Environment Variables

This stack has no required environment variables.

## Services & Ports

| Service | Internal Port | Access Pattern | Notes |
| --- | --- | --- | --- |
| `universo-web` | `80` | `http://universo-web:80` | Web frontend on `npm_network`. |

## Container Images

| Service | Image |
| --- | --- |
| `universo-web` | `universo-web:latest` |

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
