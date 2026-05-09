# Monitoring Stack

System monitoring, dashboarding, and homelab visibility for the services in this repository. This stack mixes host-level observability, Docker log access, network discovery, and two dashboard options so you can choose the experience that fits your setup.

## Features

### System Monitoring

- **Beszel**: lightweight host and container monitoring with a separate agent.
- **Dashdot**: visual system dashboard for CPU, memory, disk, and host-level stats.
- **Dozzle**: real-time Docker log viewer.
- **Glances**: system and container overview with a web UI.
- **Scrutiny**: disk health and S.M.A.R.T. monitoring.
- **Speedtest Tracker**: historical internet speed test tracking.

### Home Automation & Network

- **Home Assistant**: home automation and device orchestration.
- **NetAlertX**: network discovery and alerting.
- **WatchYourLAN**: LAN device discovery and visibility.

### Dashboard & Management

- **Homarr**: primary dashboard in the compose stack.
- **Homebox**: asset and inventory management.
- **Homepage**: optional local dashboard template, mounted from your private config directory.

## Configuration

### Environment Variables

This stack requires a `.env` file for configuration. A complete and recommended set of variables can be found in the `.env.example` file.

```bash
cp .env.example .env
```

**Key variables include:**

- `DOCKER_DATA_BASEFOLDER`: persistent data root
- `DOCKER_MEDIA_BASEFOLDER`: media storage root
- `PUBLIC_DOMAIN`: base domain used by Homepage and public URLs
- `BESZEL_SSH_KEY`: SSH public key for Beszel agent authentication
- `BESZEL_TOKEN`: Beszel agent token
- `BESZEL_HUB_URL`: public Beszel hub URL
- `NPM_EMAIL` and `NPM_PASSWORD`: Nginx Proxy Manager credentials reused by the Homepage widget
- `BESZEL_USERNAME` and `BESZEL_PASSWORD`: Beszel dashboard credentials reused by the Homepage widget

Optional variables:

- `HOMARR_SECRET_ENCRYPTION_KEY`: Homarr encryption secret
- `IMMICH_API_KEY`: Immich API key for the Homepage widget
- `TRACEARR_API_KEY`: Tracearr API key for the Homepage widget
- `SPEEDTEST_TRACKER_APP_KEY`: Speedtest Tracker app key
- `SPEEDTEST_TRACKER_API_TOKEN`: Speedtest Tracker API token used by the Homepage widget

Homepage can be mounted from `${DOCKER_DATA_BASEFOLDER}/homepage/config`, and it also receives read-only mounts for `${DOCKER_DATA_BASEFOLDER}`, `${DOCKER_MEDIA_BASEFOLDER}`, and `/sys` so the `resources` widget can report disk usage and temperature data for the host mounts.

The services on `npm_network` are intended to be reverse-proxied through Nginx Proxy Manager. Host-network services keep their direct host endpoints because they need local network visibility.

## Services & Ports

| Service | Internal Port | Public Access Pattern | Notes |
| --- | --- | --- | --- |
| Beszel | `8090` | `https://beszel.${PUBLIC_DOMAIN}` | Host and container monitoring UI. |
| Beszel Agent | - | internal only | Connects the monitored host to the Beszel hub. |
| Dashdot | `3001` | `https://dashdot.${PUBLIC_DOMAIN}` | Host metrics dashboard. |
| Dozzle | `8080` | `https://dozzle.${PUBLIC_DOMAIN}` | Docker log viewer. |
| Glances | `61208` | `https://glances.${PUBLIC_DOMAIN}` | Live system metrics. |
| Home Assistant | `8123` | `http://<host-ip>:8123` | Direct host access by design. |
| Homebox | `7745` | `https://homebox.${PUBLIC_DOMAIN}` | Asset and inventory manager. |
| Homarr | `7575` | `https://homarr.${PUBLIC_DOMAIN}` | Primary dashboard in the compose stack. |
| Homepage | `3000` | `https://homepage.${PUBLIC_DOMAIN}` | Optional dashboard alternative. |
| NetAlertX | `20211` | `http://<host-ip>:20211` | Direct host access for network scanning. |
| Scrutiny | `8080` | `https://scrutiny.${PUBLIC_DOMAIN}` | Disk health monitoring UI. |
| Speedtest Tracker | `80` | `https://speedtest-tracker.${PUBLIC_DOMAIN}` | Internet speed history. |
| WatchYourLAN | `8840` | `http://<host-ip>:8840` | Direct host access for LAN discovery. |

## Container Images

| Service | Image |
| --- | --- |
| Beszel | `henrygd/beszel:latest` |
| Beszel Agent | `henrygd/beszel-agent:latest` |
| Dashdot | `mauricenino/dashdot:latest` |
| Dozzle | `amir20/dozzle:latest` |
| Glances | `nicolargo/glances:latest-full` |
| Home Assistant | `linuxserver/homeassistant:latest` |
| Homebox | `ghcr.io/sysadminsmedia/homebox:latest-rootless` |
| Homarr | `ghcr.io/homarr-labs/homarr:latest` |
| Homepage | `ghcr.io/gethomepage/homepage:latest` |
| NetAlertX | `ghcr.io/netalertx/netalertx:latest` |
| Scrutiny | `ghcr.io/analogj/scrutiny:master-omnibus` |
| Speedtest Tracker | `linuxserver/speedtest-tracker:latest` |
| WatchYourLAN | `aceberg/watchyourlan:v2` |

## Usage

### Initial Setup

1. Create the data directories:

   ```bash
   mkdir -p ${DOCKER_DATA_BASEFOLDER}/{beszel,homeassistant,homebox,homarr,homepage,netalertx,scrutiny,speedtest-tracker,wyl2,glances}
   ```

2. Seed the Homepage config if you plan to use it:

   ```bash
   mkdir -p ${DOCKER_DATA_BASEFOLDER}/homepage/config
   cp -R monitoring/homepage/config/. ${DOCKER_DATA_BASEFOLDER}/homepage/config/
   ```

3. If needed, create the Homarr appdata directory:

   ```bash
   mkdir -p ${DOCKER_DATA_BASEFOLDER}/homarr/appdata
   ```

4. Start the stack:

   ```bash
   docker compose up -d
   ```

### Access

- Beszel: `https://beszel.${PUBLIC_DOMAIN}`
- Dashdot: `https://dashdot.${PUBLIC_DOMAIN}`
- Dozzle: `https://dozzle.${PUBLIC_DOMAIN}`
- Glances: `https://glances.${PUBLIC_DOMAIN}`
- Home Assistant: `http://<host-ip>:8123`
- Homebox: `https://homebox.${PUBLIC_DOMAIN}`
- Homarr: `https://homarr.${PUBLIC_DOMAIN}`
- Homepage: `https://homepage.${PUBLIC_DOMAIN}`
- NetAlertX: `http://<host-ip>:20211`
- Scrutiny: `https://scrutiny.${PUBLIC_DOMAIN}`
- Speedtest Tracker: `https://speedtest-tracker.${PUBLIC_DOMAIN}`
- WatchYourLAN: `http://<host-ip>:8840`

If you expose these services through Nginx Proxy Manager, keep the public hostnames in sync with `PUBLIC_DOMAIN` in `.env`.

## Security Notes

**Docker Socket Access**

These services can talk to the Docker daemon and should only be run in trusted networks:

- `beszel-agent`
- `dozzle`
- `glances`
- `homepage`
- `homarr`

**Host Mode and Privileged Services**

- `beszel-agent` uses `network_mode: host` for host visibility.
- `homeassistant` uses `network_mode: host` and `privileged: true` for Bluetooth and device discovery.
- `netalertx` and `watchyourlan` use `network_mode: host` for LAN scanning.
- `dashdot` uses `privileged: true` for host metrics.
- `scrutiny` needs `SYS_RAWIO` and device access to read disk health.

**Public Exposure**

- Homepage does not provide built-in authentication. Keep it behind a reverse proxy with auth, TLS, or a VPN.
- Avoid committing `.env` or any live hostnames. The repo only uses placeholder values and environment substitution.

## Additional Resources

- [Beszel Documentation](https://github.com/henrygd/beszel)
- [Dashdot Documentation](https://github.com/MauriceNino/dashdot)
- [Dozzle Documentation](https://github.com/amir20/dozzle)
- [Glances Documentation](https://glances.readthedocs.io/)
- [Home Assistant Documentation](https://www.home-assistant.io/docs/)
- [Homebox Documentation](https://github.com/sysadminsmedia/homebox)
- [Homepage Documentation](https://gethomepage.dev/)
- [Homarr Documentation](https://homarr.dev/)
- [NetAlertX Documentation](https://github.com/jokobsk/NetAlertX)
- [Scrutiny Documentation](https://github.com/AnalogJ/scrutiny)
- [Speedtest Tracker Documentation](https://docs.linuxserver.io/images/docker-speedtest-tracker)
- [WatchYourLAN Documentation](https://github.com/aceberg/WatchYourLAN)
