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
- **FlareSolverr**: Cloudflare bypass solution
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
- `SONARR_API_KEY`: Your API key for Sonarr.

## Services & Ports

| Service           | Internal Port | Access Pattern              | Description                                   |
| ----------------- | ------------- | --------------------------- | --------------------------------------------- |
| **Sonarr**        | `8989`        | `http://sonarr:8989`        | TV show management.                           |
| **Radarr**        | `7878`        | `http://radarr:7878`        | Movie management.                             |
| **Prowlarr**      | `9696`        | `http://prowlarr:9696`      | Indexer management.                           |
| **qBittorrent**   | `8003`        | `http://qbittorrent:8003`   | Torrent client and web UI.                    |
| **Jellyfin**      | `8096`        | `http://jellyfin:8096`      | Media streaming.                              |
| **Seerr**         | `5055`        | `http://seerr:5055`         | Media requests.                               |
| **Cinerr**        | `8080`        | `http://cinerr:8080`        | Media library browser.                        |
| **Medialyze**     | `8080`        | `http://medialyze:8080`     | Media library browser.                        |
| **FlareSolverr**  | `8191`        | `http://flaresolverr:8191`  | Cloudflare bypass.                            |
| **Byparr**        | `8191`        | `http://byparr:8191`        | Cloudflare bypass.                            |
| **AW Downloader** | `6547`        | `http://aw-downloader:6547` | Anime downloading and management backend.     |

> **Note:** All services are meant to be reached through `npm_network`; there are no host mappings in this stack.

## Container Images

| Service          | Image                                        |
| ---------------- | -------------------------------------------- |
| AW Downloader    | `ghcr.io/savvymeat/aw-downloader:latest`     |
| Cinerr           | `alexkouzel/cinerr:latest`                   |
| Medialyze        | `ghcr.io/frederikemmer/medialyze:latest`     |
| Byparr           | `ghcr.io/thephaseless/byparr:latest`         |
| FlareSolverr     | `ghcr.io/alsd4git/flaresolverr:latest`       |
| Jellyfin         | `linuxserver/jellyfin:latest`                |
| Seerr            | `ghcr.io/seerr-team/seerr:latest`             |
| Prowlarr         | `linuxserver/prowlarr:latest`                |
| qBittorrent      | `linuxserver/qbittorrent:latest`             |
| Radarr           | `linuxserver/radarr:latest`                  |
| Sonarr           | `linuxserver/sonarr:latest`                  |

## Usage

1. **Initial Setup**:

   ```bash
   # Create required directories
   mkdir -p ${DOCKER_DATA_BASEFOLDER}/{sonarr,radarr,prowlarr,jellyfin,jellyseerr,qbittorrent,aw-downloader,cinerr,medialyze}
   mkdir -p ${DOCKER_MEDIA_BASEFOLDER}/{tvseries,anime,downloads}
   ```

2. **Start the Stack**:

   ```bash
   docker compose up -d
   ```

3. **Access Services**:
   - Access services through Nginx Proxy Manager or directly via their container DNS names on `npm_network`.

## Network Configuration

All services are connected through `npm_network` for internal access and reverse proxying.

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
   - Check FlareSolverr status
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
- [FlareSolverr Documentation](https://github.com/FlareSolverr/FlareSolverr)
- [Seerr Documentation](https://github.com/seerr-team/seerr)
- [AW Downloader Documentation](https://github.com/savvymeat/aw-downloader)
