# RomM Stack

RomM game library manager with MariaDB backend, adapted for a reverse-proxied homelab setup.

## Configuration

1. Copy `.env.example` to `.env`.
2. Set the database credentials and `ROMM_AUTH_SECRET_KEY`.
3. Set `LOCAL_RETROPIE_BASE` to the root folder that contains `roms/` and `BIOS/`.

## Notes

- The RomM web container is exposed internally on `8080` and joins `npm_network`.
- MariaDB stays on the internal `romm_network`.
- The ROM library and BIOS are mounted from `LOCAL_RETROPIE_BASE`.
- Runtime secrets live in `.env`, not in the compose file.
