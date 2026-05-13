# Utilities Stack

File management, document processing, and utility services for your homelab.

## Features

- **ConvertX**: file conversion with batch support and cleanup.
- **CUP**: Docker container update puller and notifier.
- **FileBrowser Quantum**: web-based file management.
- **Telegram Files**: Telegram-backed file management.
- **UpSnap**: host-network device discovery and Wake-on-LAN.

## Configuration

### Environment Variables

Copy the example file to `.env`, then set the persistent storage paths and optional credentials:

```bash
cp .env.example .env
```

Key variables:

- `DOCKER_DATA_BASEFOLDER`
- `DOCKER_MEDIA_BASEFOLDER`
- `TELEGRAM_API_ID`
- `TELEGRAM_API_HASH`
- `FILEBROWSER_ADMIN_PASSWORD`

## Services & Ports

| Service | Internal Port | Access Pattern | Notes |
| --- | --- | --- | --- |
| ConvertX | `3000` | `http://convertx:3000` | Reverse-proxy friendly web UI. |
| CUP | `8000` | `http://cup:8000` | Reverse-proxy friendly web UI. |
| FileBrowser Quantum | `80` | `http://filebrowser-quantum:80` | Reverse-proxy friendly web UI. |
| Telegram Files | `80` | `http://telegram-files:80` | Reverse-proxy friendly web UI. |
| UpSnap | `5001` | `http://<host-ip>:5001` | Host-network service. |

> The services on `npm_network` are intended to be reached through Nginx Proxy Manager. Only the host-network service keeps a direct host endpoint.

## Container Images

| Service | Image |
| --- | --- |
| ConvertX | `ghcr.io/c4illin/convertx` |
| CUP | `ghcr.io/sergi0g/cup:latest` |
| FileBrowser Quantum | `gtstef/filebrowser` |
| Telegram Files | `ghcr.io/jarvis2f/telegram-files:latest` |
| UpSnap | `ghcr.io/seriousm4x/upsnap:latest` |

## Usage

1. Copy `.env.example` to `.env`.
2. Set the required environment variables.
3. Start the stack:

   ```bash
   docker compose up -d
   ```

## Security Notes

- `cup` mounts `/var/run/docker.sock`, so keep the stack on a trusted network.
- `upsnap` uses `network_mode: host`, which exposes it directly on the host interface.
- Keep the Telegram credentials and admin password in `.env`.

## Nginx Proxy Manager Notes

- Use the shared upload-heavy advanced block from [`docs/nginx-proxy-manager.md`](../docs/nginx-proxy-manager.md) for `FileBrowser Quantum` and `ConvertX`.
- `Telegram Files` does not need that block because it writes to disk directly and is not upload-heavy through the web UI.

## Additional Resources

- [ConvertX Documentation](https://github.com/c4illin/convertx)
- [CUP Documentation](https://github.com/sergi0g/cup)
- [FileBrowser Documentation](https://filebrowser.org/)
- [Telegram Files Documentation](https://github.com/jarvis2f/telegram-files)
- [UpSnap Documentation](https://github.com/seriousm4x/upsnap)
