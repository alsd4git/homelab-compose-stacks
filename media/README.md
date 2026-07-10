# Media Stack

A comprehensive media management and automation stack for your homelab environment. This stack includes tools for media organization, downloading, and streaming.

## Features

### Media Management

- **Sonarr**: TV show management and automation
- **Radarr**: Movie management and automation
- **Prowlarr**: Indexer management for Sonarr and Radarr
- **Seerr**: Media request management
- **Jellyfin**: Media streaming server
- **Cinerr**: Media browser for library discovery
- **Medialyze**: Media browser for library discovery

### Download Management

- **qBittorrent**: Torrent client with Vuetorrent UI
- **qbit_manage**: qBittorrent maintenance and tagging automation
- **Byparr**: Cloudflare bypass solution
- **AW Downloader**: Automated anime downloading and management

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

- `DOCKER_DATA_BASEFOLDER`: The absolute path for storing persistent data.
- `DOCKER_MEDIA_BASEFOLDER`: The absolute path for your media files.
- `QBITTORRENT_USERNAME`: qBittorrent Web UI username used by `qbit_manage`
- `QBITTORRENT_PASSWORD`: qBittorrent Web UI password used by `qbit_manage`
- `AW_APP_KEY`: Application key used by AW Downloader.

## Services & Ports

| Service           | Internal Port | Access Pattern              | Description                                   |
| ----------------- | ------------- | --------------------------- | --------------------------------------------- |
| **Sonarr**        | `8989`        | `http://sonarr:8989`        | TV show management.                           |
| **Radarr**        | `7878`        | `http://radarr:7878`        | Movie management.                             |
| **Prowlarr**      | `9696`        | `http://prowlarr:9696`      | Indexer management.                           |
| **qBittorrent**   | `6881`, `6881/udp` | `http://qbittorrent:8003` | Torrent client and web UI; torrent ports are mapped on host. |
| **qbit_manage**   | `8181`             | `http://qbit-manage:8181` | qBittorrent housekeeping, tagging, recheck automation, and internal Web UI/API. |
| **Jellyfin**      | `8096`        | `http://jellyfin:8096`      | Media streaming.                              |
| **Seerr**         | `5055`        | `http://seerr:5055`         | Media requests.                               |
| **Cinerr**        | `8080`        | `http://cinerr:8080`        | Media library browser.                        |
| **Medialyze**     | `8080`        | `http://medialyze:8080`     | Media library browser.                        |
| **Byparr**        | `8191`        | `http://byparr:8191`        | Cloudflare bypass.                            |
| **AW Downloader** | `6547`        | `http://aw-downloader:6547` | Anime downloading and management backend.     |

> **Note:** Most services are meant to be reached through `npm_network`; qBittorrent also publishes its torrent ports on the host for peer connectivity.

> **Jellyfin note:** the media mount is writable so Jellyfin can store metadata sidecars and library state when needed.

> **qbit_manage note:** create `${DOCKER_DATA_BASEFOLDER}/qbit-manage/config.yml` from `qbit-manage/config.yml.example`, keep the qBittorrent credentials in the stack env, and leave cleanup/cat-moves disabled unless you are ready to automate deletions. In the current setup it stays in tagging/recheck mode only, and the category map should mirror the real qBittorrent folder layout, e.g. `/downloads/Radarr/` and `/downloads/Sonarr/`.

> **Web UI note:** every service with an internal web UI should be exposed on `npm_network` for Nginx Proxy Manager and added to Homepage for quick access; keep direct host exposure reserved for protocols that actually need it.

> **Network note:** shared bridge networks are consumed with `external: true` only. In this repository `npm_network` is a pre-created shared network referenced by every stack, while `pihole_network` is created by the Pi-hole stack and consumed by `media` for DNS attribution.

> **Pi-hole attribution note:** if you want Pi-hole to log queries per container, point that container's `dns` entry at the Pi-hole IP on `pihole_network` instead of using a container name. For the current stack this is `10.250.250.10`, and `Prowlarr` now joins `pihole_network` as the first test case so that resolver can actually be reached from inside the container. Docker still resolves through its embedded DNS, but the upstream resolver is the fixed Pi-hole IP.

> **NPM extra-config note:** when a service needs LAN/Tailscale access or TinyAuth gating, keep the snippet in `media/NPM-extraconf.conf` and follow the shared policy in [`docs/nginx-proxy-manager.md`](../docs/nginx-proxy-manager.md).

## Container Images

| Service          | Image                                        |
| ---------------- | -------------------------------------------- |
| AW Downloader    | `ghcr.io/savvymeat/aw-downloader:latest`     |
| Cinerr           | `alexkouzel/cinerr:latest`                   |
| Medialyze        | `ghcr.io/frederikemmer/medialyze:latest`     |
| Byparr           | `ghcr.io/thephaseless/byparr:latest`         |
| Jellyfin         | `linuxserver/jellyfin:latest`                |
| Seerr            | `ghcr.io/seerr-team/seerr:latest`             |
| Prowlarr         | `linuxserver/prowlarr:latest`                |
| qBittorrent      | `linuxserver/qbittorrent:latest`             |
| qbit_manage      | `ghcr.io/stuffanthings/qbit_manage:latest`   |
| Radarr           | `linuxserver/radarr:latest`                  |
| Sonarr           | `linuxserver/sonarr:latest`                  |

## Usage

1. **Initial Setup**:

   ```bash
   # Create required directories
   mkdir -p ${DOCKER_DATA_BASEFOLDER}/{sonarr,radarr,prowlarr,jellyfin,jellyseerr,qbittorrent,qbit-manage,aw-downloader,cinerr,medialyze}
   mkdir -p ${DOCKER_MEDIA_BASEFOLDER}/{tvseries,anime,downloads}
   ```

2. **Start the Stack**:

   ```bash
   docker compose up -d
   ```

3. **Access Services**:
   - Access services through Nginx Proxy Manager or directly via their container DNS names on `npm_network`.

## Security Notes

1. **API Keys**: Keep your Sonarr API key secure and don't share it
2. **Port Exposure**: Only expose necessary ports to the internet
3. **Authentication**: Enable authentication on all services
4. **Updates**: Keep all services updated to the latest versions

## Troubleshooting

1. **Service Not Starting**:
   - Check logs: `docker compose logs <service_name>`
   - Verify environment variables
   - Check port conflicts

2. **Download Issues**:
   - Verify qBittorrent configuration
   - Check Byparr status
   - Verify indexer status in Prowlarr

3. **Media Not Showing**:
   - Check file permissions
   - Verify media paths
   - Check Sonarr/Radarr configuration

## Additional Resources

- [Sonarr Documentation](https://wiki.servarr.com/sonarr)
- [Radarr Documentation](https://wiki.servarr.com/radarr)
- [Prowlarr Documentation](https://wiki.servarr.com/prowlarr)
- [Jellyfin Documentation](https://jellyfin.org/docs)
- [qBittorrent Documentation](https://github.com/qbittorrent/qBittorrent/wiki)
- [qbit_manage Wiki](https://github.com/StuffAnThings/qbit_manage/wiki)
- [Byparr Documentation](https://github.com/ThePhaseless/Byparr)
- [Seerr Documentation](https://github.com/seerr-team/seerr)
- [AW Downloader Documentation](https://github.com/savvymeat/aw-downloader)
