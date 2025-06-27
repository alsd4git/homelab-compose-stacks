# Dockerini Services Recap

> **Note:** Both mapped and exposed ports are listed for each service. The long-term plan is to reduce direct port exposure and use a reverse proxy for internal services.

This document provides a comprehensive overview of all services in the Dockerini project, organized by stack, with their port mappings and status.

## Standardized Stacks

### DDNS Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| DDNS Updater | mapped | 8000 | 8001 | Web UI for monitoring and management (external) | ✅ Standardized |
| DDNS Updater | exposed | 8000 | - | Internal Web UI port for reverse proxy or internal access | ✅ Standardized |

### NPM Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| Nginx Proxy Manager | mapped | 80 | 80 | Public HTTP traffic (external) | ✅ Standardized |
| Nginx Proxy Manager | mapped | 443 | 443 | Public HTTPS traffic (external) | ✅ Standardized |
| Nginx Proxy Manager | mapped | 81 | 83 | Admin Web UI (external) | ✅ Standardized |
| Nginx Proxy Manager | exposed | 80 | - | Internal HTTP port for reverse proxy or internal access | ✅ Standardized |
| Nginx Proxy Manager | exposed | 443 | - | Internal HTTPS port for reverse proxy or internal access | ✅ Standardized |
| Nginx Proxy Manager | exposed | 81 | - | Internal Admin Web port for reverse proxy or internal access | ✅ Standardized |
| Step CA | mapped | 9000 | 9001 | Step CA API (external) | ✅ Standardized |
| Step CA | exposed | 9000 | - | Internal Step CA API port for reverse proxy or internal access | ✅ Standardized |

### Pi-hole Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| Pi-hole | mapped | 53 | 53 | DNS (TCP, external) | ✅ Standardized |
| Pi-hole | mapped | 53 | 53/udp | DNS (UDP, external) | ✅ Standardized |
| Pi-hole | mapped | 80 | 81 | Web interface (external, recommended to use reverse proxy instead) | ✅ Standardized |
| Pi-hole | mapped | 443 | 443 | HTTPS (self-signed cert, external, recommended to use reverse proxy instead) | ✅ Standardized |
| Pi-hole | mapped | 67 | 67/udp | DHCP server (external, optional) | ✅ Standardized |
| Pi-hole | exposed | 80 | - | Web interface (internal, for reverse proxy or internal access) | ✅ Standardized |
| Pi-hole | exposed | 443 | - | HTTPS (self-signed cert, internal, for reverse proxy or internal access) | ✅ Standardized |
| Pi-hole | exposed | 53 | - | DNS (internal, for internal container communication) | ✅ Standardized |
| Pi-hole | exposed | 67 | - | DHCP (internal, for internal container communication) | ✅ Standardized |

### WG-Easy Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| WireGuard Easy | mapped | 51820/udp | 51820/udp | WireGuard VPN (external) | ✅ Standardized |
| WireGuard Easy | mapped | 51821/tcp | 51821/tcp | Web interface (external) | ✅ Standardized |
| WireGuard Easy | exposed | 51820/udp | - | WireGuard VPN (internal, for reverse proxy or internal access) | ✅ Standardized |
| WireGuard Easy | exposed | 51821/tcp | - | Web interface (internal, for reverse proxy or internal access) | ✅ Standardized |

### Tools Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| ConvertX | mapped | 3000 | 3003 | Web UI (external) | ✅ Standardized |
| ConvertX | exposed | 3000 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| CUP | mapped | 8000 | 8004 | Web UI (external) | ✅ Standardized |
| CUP | exposed | 8000 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| FileBrowser | mapped | 80 | 8085 | Web UI (external) | ✅ Standardized |
| FileBrowser | exposed | 80 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| Scrutiny | mapped | 8080 | 8083 | Web UI (external) | ✅ Standardized |
| Scrutiny | mapped | 8086 | 8086 | InfluxDB (external) | ✅ Standardized |
| Scrutiny | exposed | 8080 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| Scrutiny | exposed | 8086 | - | InfluxDB (internal, for reverse proxy or internal access) | ✅ Standardized |
| Speedtest Tracker | mapped | 80 | 8084 | Web UI (external) | ✅ Standardized |
| Speedtest Tracker | exposed | 80 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| Stirling PDF | mapped | 8080 | 8082 | Web UI (external) | ✅ Standardized |
| Stirling PDF | exposed | 8080 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| Telegram Files | mapped | 80 | 6543 | Web UI (external) | ✅ Standardized |
| Telegram Files | exposed | 80 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| UpSnap | host | 5001 | 5001 | Web UI (host networking, exposed directly on the host) | ✅ Standardized |

### Netfroz Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| Anime Downloader | mapped | 5000 | 5000 | Web UI/API (external) | ✅ Standardized |
| Anime Downloader | exposed | 5000 | - | Web UI/API (internal, for reverse proxy or internal access) | ✅ Standardized |
| FlareSolverr | mapped | 8191 | 8191 | API (external) | ✅ Standardized |
| FlareSolverr | exposed | 8191 | - | API (internal, for reverse proxy or internal access) | ✅ Standardized |
| Jellyfin | mapped | 8096 | 8096 | Web UI (external) | ✅ Standardized |
| Jellyfin | mapped | 8920 | 8920 | HTTPS (external) | ✅ Standardized |
| Jellyfin | mapped | 7359/udp | 7359/udp | Auto-discovery (external) | ✅ Standardized |
| Jellyfin | exposed | 8096 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| Jellyfin | exposed | 8920 | - | HTTPS (internal, for reverse proxy or internal access) | ✅ Standardized |
| Jellyfin | exposed | 7359/udp | - | Auto-discovery (internal, for internal container communication) | ✅ Standardized |
| Jellyseerr | mapped | 5055 | 5055 | Web UI (external) | ✅ Standardized |
| Jellyseerr | exposed | 5055 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| Prowlarr | mapped | 9696 | 9696 | Web UI/API (external) | ✅ Standardized |
| Prowlarr | exposed | 9696 | - | Web UI/API (internal, for reverse proxy or internal access) | ✅ Standardized |
| qBittorrent | mapped | 8003 | 8003 | Web UI (external) | ✅ Standardized |
| qBittorrent | mapped | 6881 | 6881 | Torrent (TCP, external) | ✅ Standardized |
| qBittorrent | mapped | 6881/udp | 6881/udp | Torrent (UDP, external) | ✅ Standardized |
| qBittorrent | exposed | 8003 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| qBittorrent | exposed | 6881 | - | Torrent (TCP, internal, for internal container communication) | ✅ Standardized |
| qBittorrent | exposed | 6881/udp | - | Torrent (UDP, internal, for internal container communication) | ✅ Standardized |
| Radarr | mapped | 7878 | 7878 | Web UI/API (external) | ✅ Standardized |
| Radarr | exposed | 7878 | - | Web UI/API (internal, for reverse proxy or internal access) | ✅ Standardized |
| Sonarr | mapped | 8989 | 8989 | Web UI/API (external) | ✅ Standardized |
| Sonarr | exposed | 8989 | - | Web UI/API (internal, for reverse proxy or internal access) | ✅ Standardized |

### Home Dashboard & Monitoring Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| Dashdot | mapped | 3001 | 3002 | Web UI (external) | ✅ Standardized |
| Dashdot | exposed | 3001 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| Dozzle | mapped | 8080 | 8081 | Web UI (external) | ✅ Standardized |
| Dozzle | exposed | 8080 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| Glances | mapped | 61208 | 61208 | Web UI/API (external) | ✅ Standardized |
| Glances | exposed | 61208 | - | Web UI/API (internal, for reverse proxy or internal access) | ✅ Standardized |
| Home Assistant | mapped | 8123 | 8123 | Web UI (external) | ✅ Standardized |
| Home Assistant | exposed | 8123 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| Homepage | mapped | 3000 | 3001 | Web UI (external) | ✅ Standardized |
| Homepage | exposed | 3000 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| Homebox | mapped | 7745 | 3100 | Web UI (external) | ✅ Standardized |
| Homebox | exposed | 7745 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| Homarr | mapped | 7575 | 7575 | Web UI (external) | ✅ Standardized |
| Homarr | exposed | 7575 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| NetAlertX | mapped | 20211 | 20211 | Web UI (external) | ✅ Standardized |
| NetAlertX | exposed | 20211 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| WatchYourLAN | mapped | 8840 | 8840 | Web UI (external) | ✅ Standardized |
| WatchYourLAN | exposed | 8840 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |

### KaraKeep Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| KaraKeep Web | mapped | 3000 | 3005 | Web UI (external) | ✅ Standardized |
| KaraKeep Web | exposed | 3000 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| KaraKeep Chrome | exposed | 9222 | - | Chrome remote debugging (internal, for reverse proxy or internal access) | ✅ Standardized |
| KaraKeep MeiliSearch | exposed | 7700 | - | MeiliSearch API (internal, for reverse proxy or internal access) | ✅ Standardized |

### Transmission Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| Transmission | mapped | 9091 | 9091 | Web UI (external) | ✅ Standardized |
| Transmission | mapped | 51413 | 51413 | Torrent (TCP, external) | ✅ Standardized |
| Transmission | mapped | 51413/udp | 51413/udp | Torrent (UDP, external) | ✅ Standardized |
| Transmission | exposed | 9091 | - | Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |
| Transmission | exposed | 51413 | - | Torrent (TCP, internal, for internal container communication) | ✅ Standardized |
| Transmission | exposed | 51413/udp | - | Torrent (UDP, internal, for internal container communication) | ✅ Standardized |

### Paperless-ngx Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| Paperless-ngx | mapped | 8000 | 8002 | Web UI/API (external) | ✅ Standardized |
| Paperless-ngx | exposed | 8000 | - | Web UI/API (internal, for reverse proxy or internal access) | ✅ Standardized |

### RustDesk Relay Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| HBBS | host | 21115/tcp | 21115/tcp | ID registration | ✅ Standardized |
| HBBS | host | 21116/tcp | 21116/tcp | Relay connections | ✅ Standardized |
| HBBS | host | 21118/tcp | 21118/tcp | TCP hole punching | ✅ Standardized |
| HBBR | host | 21117/tcp | 21117/tcp | NAT traversal | ✅ Standardized |
| HBBR | host | 21119/tcp | 21119/tcp | TCP hole punching | ✅ Standardized |

### NPM Plus Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| NPM Plus | mapped | 80 | 808 | Public HTTP Port (external) | ✅ Standardized |
| NPM Plus | mapped | 443 | 4434 | Public HTTPS Port (external) | ✅ Standardized |
| NPM Plus | mapped | 82 | 85 | Admin Web UI (external) | ✅ Standardized |
| NPM Plus | exposed | 80 | - | HTTP (internal, for reverse proxy or internal access) | ✅ Standardized |
| NPM Plus | exposed | 443 | - | HTTPS (internal, for reverse proxy or internal access) | ✅ Standardized |
| NPM Plus | exposed | 82 | - | Admin Web UI (internal, for reverse proxy or internal access) | ✅ Standardized |

### Menu Gucci Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| Menu Gucci Bot | none | - | - | No ports exposed (Telegram bot only) | ✅ Standardized |

### Immich Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| Immich Server | mapped | 2283 | 2283 | Web UI/API (external) | ✅ Standardized |
| Immich Server | exposed | 2283 | - | Web UI/API (internal, for reverse proxy or internal access) | ✅ Standardized |

### AdGuard Stack
| Service | Port Type | Internal Port | External Port | Usage | Status |
|---------|-----------|--------------|---------------|-------|---------|
| AdGuard Home | mapped | 53/tcp | 54 | DNS (TCP, external) | ✅ Standardized |
| AdGuard Home | mapped | 53/udp | 54 | DNS (UDP, external) | ✅ Standardized |
| AdGuard Home | mapped | 67/udp | 67 | DHCP server (UDP, external) | ✅ Standardized |
| AdGuard Home | mapped | 68/udp | 68 | DHCP client (UDP, external, optional) | ✅ Standardized |
| AdGuard Home | mapped | 80/tcp | 86 | HTTP web interface (external) | ✅ Standardized |
| AdGuard Home | mapped | 443/tcp | 443 | HTTPS web interface (external, optional) | ✅ Standardized |
| AdGuard Home | mapped | 443/udp | 443 | HTTPS web interface (UDP, external, optional) | ✅ Standardized |
| AdGuard Home | mapped | 3000/tcp | 3000 | API (external) | ✅ Standardized |
| AdGuard Home | mapped | 853/tcp | 853 | DNS-over-TLS (DoT, external) | ✅ Standardized |
| AdGuard Home | mapped | 784/udp | 784 | DNS-over-QUIC (DoQ, external) | ✅ Standardized |
| AdGuard Home | mapped | 853/udp | 853 | DNS-over-DTLS (DoT, external) | ✅ Standardized |
| AdGuard Home | mapped | 8853/udp | 8853 | DNS-over-TLS (DoT, external) | ✅ Standardized |
| AdGuard Home | mapped | 5443/tcp | 5443 | DNSCrypt (TCP, external) | ✅ Standardized |
| AdGuard Home | mapped | 5443/udp | 5443 | DNSCrypt (UDP, external) | ✅ Standardized |
| AdGuard Home | exposed | 53/tcp | - | DNS (TCP, internal, for reverse proxy or internal access) | ✅ Standardized |
| AdGuard Home | exposed | 53/udp | - | DNS (UDP, internal, for reverse proxy or internal access) | ✅ Standardized |
| AdGuard Home | exposed | 67/udp | - | DHCP server (internal, for reverse proxy or internal access) | ✅ Standardized |
| AdGuard Home | exposed | 68/udp | - | DHCP client (internal, for reverse proxy or internal access) | ✅ Standardized |
| AdGuard Home | exposed | 80/tcp | - | HTTP web interface (internal, for reverse proxy or internal access) | ✅ Standardized |
| AdGuard Home | exposed | 443/tcp | - | HTTPS web interface (internal, for reverse proxy or internal access) | ✅ Standardized |
| AdGuard Home | exposed | 443/udp | - | HTTPS web interface (internal, for reverse proxy or internal access) | ✅ Standardized |
| AdGuard Home | exposed | 3000/tcp | - | API (internal, for reverse proxy or internal access) | ✅ Standardized |
| AdGuard Home | exposed | 853/tcp | - | DNS-over-TLS (DoT, internal, for reverse proxy or internal access) | ✅ Standardized |
| AdGuard Home | exposed | 784/udp | - | DNS-over-QUIC (DoQ, internal, for reverse proxy or internal access) | ✅ Standardized |
| AdGuard Home | exposed | 853/udp | - | DNS-over-DTLS (DoT, internal, for reverse proxy or internal access) | ✅ Standardized |
| AdGuard Home | exposed | 8853/udp | - | DNS-over-TLS (DoT, internal, for reverse proxy or internal access) | ✅ Standardized |
| AdGuard Home | exposed | 5443/tcp | - | DNSCrypt (TCP, internal, for reverse proxy or internal access) | ✅ Standardized |
| AdGuard Home | exposed | 5443/udp | - | DNSCrypt (UDP, internal, for reverse proxy or internal access) | ✅ Standardized |

## TODO Items

### High Priority

1. Testing and Validation:
   - Test all standardized stacks
   - Test network connectivity
   - Validate environment variables

### Medium Priority
1. Documentation:
   - Create READMEs for remaining stacks
   - Add troubleshooting guides
   - Create deployment guides

2. Security:
   - Add security hardening measures
   - Implement backup strategies
   - Add monitoring and logging solutions

### Low Priority
1. Development:
   - Implement automated testing
   - Add CI/CD pipelines
   - Create development environment setup
   - Add contribution guidelines
   - Implement version control strategy
   - Add performance optimization guides

## Notes
- All standardized stacks have consistent formatting
- Environment variables have fallback values
- Network naming has been standardized
- Each standardized stack has comprehensive documentation 