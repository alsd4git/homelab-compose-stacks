# Media Stack

A comprehensive media management and automation stack for your homelab environment. This stack includes tools for media organization, downloading, and streaming.

## Features

### Media Management

- **Sonarr**: TV show management and automation
- **Radarr**: Movie management and automation
- **Prowlarr**: Indexer management for Sonarr and Radarr
- **Jellyseerr**: Media request management
- **Jellyfin**: Media streaming server

### Download Management

- **qBittorrent**: Torrent client with Vuetorrent UI
- **FlareSolverr**: Cloudflare bypass solution
- **Anime Downloader**: Automated anime downloading and management

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

| Service              | External Port  | Internal Port  | Description                                    |
| -------------------- | -------------- | -------------- | ---------------------------------------------- |
| **Sonarr**           | `8989`         | `8989`         | TV show management.                            |
| **Radarr**           | `7878`         | `7878`         | Movie management.                              |
| **Prowlarr**         | `9696`         | `9696`         | Indexer management.                            |
| **qBittorrent**      | `8003`, `6881` | `8003`, `6881` | Torrent client and web UI.                     |
| **Jellyfin**         | -              | `8096`         | Media streaming (exposed via reverse proxy).   |
| **Jellyseerr**       | -              | `5055`         | Media requests (exposed via reverse proxy).    |
| **FlareSolverr**     | -              | `8191`         | Cloudflare bypass (internal service).          |
| **Anime Downloader** | -              | `5000`         | Anime downloading (exposed via reverse proxy). |

> **Note:** Most services are exposed internally and are intended to be accessed via a reverse proxy. Only essential ports are mapped externally.

## Container Images

| Service          | Image                                        |
| ---------------- | -------------------------------------------- |
| Anime Downloader | `ghcr.io/mainkronos/anime_downloader:latest` |
| FlareSolverr     | `ghcr.io/flaresolverr/flaresolverr:latest`   |
| Jellyfin         | `linuxserver/jellyfin:latest`                |
| Jellyseerr       | `fallenbagel/jellyseerr:latest`              |
| Prowlarr         | `linuxserver/prowlarr:latest`                |
| qBittorrent      | `linuxserver/qbittorrent:latest`             |
| Radarr           | `linuxserver/radarr:latest`                  |
| Sonarr           | `linuxserver/sonarr:latest`                  |

## Usage

1. **Initial Setup**:

   ```bash
   # Create required directories
   mkdir -p ${DOCKER_DATA_BASEFOLDER}/{sonarr,radarr,prowlarr,jellyfin,jellyseerr,qbittorrent,animedownloader}
   mkdir -p ${DOCKER_MEDIA_BASEFOLDER}/{tvseries,anime,downloads}
   ```

2. **Start the Stack**:

   ```bash
   docker compose up -d
   ```

3. **Access Services**:
   - Access Sonarr, Radarr, Prowlarr, and qBittorrent on their externally mapped ports.
   - Access Jellyfin, Jellyseerr, and Anime Downloader through your reverse proxy.

## Network Configuration

All services are connected through a bridge network for internal communication. External access is provided through mapped ports.

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
- [Anime Downloader Documentation](https://github.com/mainkronos/anime_downloader)
