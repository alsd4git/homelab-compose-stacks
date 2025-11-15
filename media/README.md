# Netfroz Stack

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

### Required Environment Variables
Create a `.env` file with the following variables:
```env
DOCKER_DATA_BASEFOLDER=/path/to/data
DOCKER_MEDIA_BASEFOLDER=/path/to/media
SONARR_API_KEY=your_sonarr_api_key
```

### Optional Environment Variables
```env
LOG_LEVEL=info                    # FlareSolverr log level
LOG_HTML=false                    # FlareSolverr HTML logging
CAPTCHA_SOLVER=none              # FlareSolverr captcha solver
PORT=8191                        # FlareSolverr port
```

## Services

### Sonarr
- **Port**: 8989
- **Features**:
  - TV show management
  - Automatic episode downloading
  - Quality profile management
  - Custom naming formats
- **Health Check**: Enabled

### Radarr
- **Port**: 7878
- **Features**:
  - Movie management
  - Automatic movie downloading
  - Quality profile management
  - Custom naming formats

### Prowlarr
- **Port**: 9696
- **Features**:
  - Indexer management
  - Integration with Sonarr and Radarr
  - Automatic indexer synchronization

### Jellyfin
- **Ports**: 
  - 8096 (Web UI)
  - 8920 (HTTPS)
  - 7359/UDP (Auto-discovery)
- **Features**:
  - Media streaming
  - Hardware transcoding support
  - User management
  - Multiple client support

### Jellyseerr
- **Port**: 5055
- **Features**:
  - Media requests
  - User management
  - Integration with Jellyfin
  - Request approval workflow

### qBittorrent
- **Ports**:
  - 8003 (Web UI)
  - 6881 (Torrent)
- **Features**:
  - Vuetorrent UI
  - Category management
  - Download scheduling
  - Bandwidth control

### FlareSolverr
- **Port**: 8191
- **Features**:
  - Cloudflare bypass
  - Captcha solving
  - Proxy support
  - Configurable logging

### Anime Downloader
- **Port**: 5000
- **Features**:
  - Automated anime downloading
  - Integration with Sonarr
  - Custom download paths
  - Connection management

## Ports

- **Anime Downloader**
  - 5000:5000 (mapped): Web UI/API (external)
  - 5000 (exposed): Web UI/API (internal, for reverse proxy or internal access)
- **FlareSolverr**
  - 8191:8191 (mapped): API (external)
  - 8191 (exposed): API (internal, for reverse proxy or internal access)
- **Jellyfin**
  - 8096:8096 (mapped): Web UI (external)
  - 8920:8920 (mapped): HTTPS (external)
  - 7359:7359/udp (mapped): Auto-discovery (external)
  - 8096 (exposed): Web UI (internal, for reverse proxy or internal access)
  - 8920 (exposed): HTTPS (internal, for reverse proxy or internal access)
  - 7359/udp (exposed): Auto-discovery (internal, for internal container communication)
- **Jellyseerr**
  - 5055:5055 (mapped): Web UI (external)
  - 5055 (exposed): Web UI (internal, for reverse proxy or internal access)
- **Prowlarr**
  - 9696:9696 (mapped): Web UI/API (external)
  - 9696 (exposed): Web UI/API (internal, for reverse proxy or internal access)
- **qBittorrent**
  - 8003:8003 (mapped): Web UI (external)
  - 6881:6881 (mapped): Torrent (TCP, external)
  - 6881:6881/udp (mapped): Torrent (UDP, external)
  - 8003 (exposed): Web UI (internal, for reverse proxy or internal access)
  - 6881 (exposed): Torrent (TCP, internal, for internal container communication)
  - 6881/udp (exposed): Torrent (UDP, internal, for internal container communication)
- **Radarr**
  - 7878:7878 (mapped): Web UI/API (external)
  - 7878 (exposed): Web UI/API (internal, for reverse proxy or internal access)
- **Sonarr**
  - 8989:8989 (mapped): Web UI/API (external)
  - 8989 (exposed): Web UI/API (internal, for reverse proxy or internal access)

> **Note:** Both mapped and exposed ports are documented for clarity. The long-term plan is to reduce direct port exposure and use a reverse proxy for internal services.

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

3. **Configure Services**:
   - Access Sonarr at `http://localhost:8989`
   - Access Radarr at `http://localhost:7878`
   - Access Prowlarr at `http://localhost:9696`
   - Access Jellyfin at `http://localhost:8096`
   - Access Jellyseerr at `http://localhost:5055`
   - Access qBittorrent at `http://localhost:8003`
   - Access FlareSolverr at `http://localhost:8191`
   - Access Anime Downloader at `http://localhost:5000`

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
