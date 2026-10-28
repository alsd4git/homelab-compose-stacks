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

RomM follows the upstream `latest` tag. Back up its data and review upstream
release notes before redeploying. MariaDB also follows the `latest` tag used by
the official example.

## Usage

1. Copy `.env.example` to `.env`.
2. Set the database credentials and `LOCAL_RETROPIE_BASE`.
3. Start the stack:

   ```bash
   docker compose up -d
   ```

4. Access RomM through Nginx Proxy Manager on the host you configure for the service.

## RomM 5.3.0 migration

RomM 5.3.0 no longer detects the library layout from `filesystem.roms_folder`
and `filesystem.firmware_folder`. Those keys must be removed from
`config.yml`, otherwise the container refuses to start. This stack uses the
recommended Structure A layout (`/romm/library/roms/{platform}` and
`/romm/library/bios/{platform}`), so the config must contain:

```yaml
filesystem:
  structure:
    default: "roms/{platform}/{game}"
    firmware: "bios/{platform}"
```

Keep the existing `exclude`, `system`, `scan` and `emulatorjs` sections when
migrating; only replace the two removed filesystem keys. Back up MariaDB and
`config.yml`, redeploy the intended image version, then run a small library scan before a
full rescan. The 5.3.0 release also changes emulator-streaming configuration
to one entry per container; this stack does not enable streaming, so no
streaming migration is needed here.

This migration applies when upgrading from an older configuration, including
when moving directly to 5.4.0. The base Compose file uses `latest`; only the
optional 5.4.0 library-fixes override below pins an upstream image digest.

## Security Notes

- Keep `ROMM_AUTH_SECRET_KEY` and database credentials in `.env`.
- The web UI is only exposed through the reverse proxy network.
- The game library and BIOS paths should point to trusted local storage.

## Additional Resources

- [RomM Documentation](https://docs.romm.app/)

## Updates

### Local fixes for RomM 5.4.0

The optional library-fixes image closes SQLAlchemy connection pools before
an RQ child process exits. Without it, successful jobs can increment MariaDB's
`Aborted_clients` counter and log "Got an error reading communication packets".
This corrects connection shutdown rather than suppressing database warnings.
It also reads CIA title IDs from their matching ticket and TMD, uses sigil's
raw-CD reader for PS2 BIN/CUE files, and recognizes sigil's typed "not found"
errors. Other formats continue through the bundled sigil implementation.

Build and select it with the override:

```bash
docker compose -f compose.yaml -f compose.library-fixes.yaml build romm
docker compose -f compose.yaml -f compose.library-fixes.yaml up -d romm
```

For an image-only Portainer stack, build the image on its Docker host first,
then use `image: local/romm:5.4.0-library-fixes` and `pull_policy: never` for
RomM. Keep all existing environment variables, mounts and networks.
The Dockerfile pins the upstream image digest, and the patch checks the exact
worker and adapter sources. Review or remove the patches when upgrading
beyond 5.4.0. This local image needs to be built on each deployment host;
it is not published to a registry.

These patches are experimental. The PS2 reader calls internal sigil native
symbols, so the fixed image digest and source checks must remain in place.
Before deployment, validate the image build and extraction against known CIA
and PS2 BIN/CUE samples, including invalid inputs. Compose validation alone
does not verify native compatibility or title ID correctness.

### Standard upstream updates

Before redeploying, back up MariaDB and `/romm/config/config.yml`, then review
the matching official release notes and configuration reference. After
redeploying through Portainer, verify that the container is running, its
configuration parses correctly, and a small library scan completes without
errors. RomM reads `config.yml` from `/romm/config/config.yml`.
