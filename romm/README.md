# RomM Stack

Game library manager with a MariaDB backend and reverse-proxy friendly networking.

## Features

- **Web UI**: central interface for browsing and managing game libraries.
- **MariaDB backend**: persistent metadata storage on an internal network.
- **Library mounts**: ROMs and BIOS are mounted from a configurable base directory.
- **Runtime secrets**: database credentials and auth secrets stay in `.env`.

## Configuration

### Environment Variables

Copy the example file to `.env`, then set the database credentials and library root:

```bash
cp .env.example .env
```

Key variables:

- `ROMM_DB_NAME`
- `ROMM_DB_USER`
- `ROMM_DB_PASSWORD`
- `ROMM_DB_ROOT_PASSWORD`
- `ROMM_AUTH_SECRET_KEY`
- `LOCAL_RETROPIE_BASE`

## Services & Ports

| Service | Internal Port | Access Pattern | Notes |
| --- | --- | --- | --- |
| RomM | `8080` | `http://romm:8080` | Web UI on `npm_network`. |
| MariaDB | `3306` | internal only | Database stays on the private `romm_network`. |

## Container Images

| Service | Image |
| --- | --- |
| RomM | `rommapp/romm:latest` |
| MariaDB | `mariadb:latest` |

The official RomM quick-start intentionally uses floating tags for both images.
Treat each update as a backup-and-verify event rather than pinning an arbitrary
MariaDB version that diverges from the upstream reference.

## Usage

1. Copy `.env.example` to `.env`.
2. Set the database credentials and `LOCAL_RETROPIE_BASE`.
3. Start the stack:

   ```bash
   docker compose up -d
   ```

4. Access RomM through Nginx Proxy Manager on the host you configure for the service.

## Security Notes

- Keep `ROMM_AUTH_SECRET_KEY` and database credentials in `.env`.
- The web UI is only exposed through the reverse proxy network.
- The game library and BIOS paths should point to trusted local storage.

## Additional Resources

- [RomM Documentation](https://docs.romm.app/)

## Updates

The `latest` tag follows the upstream stable release, including major versions.
Before a major update, back up MariaDB and review the matching official release
notes and configuration reference. After redeploying through Portainer, verify
that the container is running, its configuration parses correctly, and a small
library scan completes without errors. RomM 5 continues to read `config.yml`
from `/romm/config/config.yml`; existing configuration should remain minimal
and rely on defaults for settings not deliberately overridden.
