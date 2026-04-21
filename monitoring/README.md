# Monitoring Stack

System monitoring, observability, and dashboarding for your homelab. This stack provides real-time metrics, log viewing, network monitoring, and customizable dashboards for service discovery and management.

## Features

### System Monitoring

- **Beszel**: A lightweight, agent-based server monitoring tool.
- **Dashdot**: A modern server dashboard for monitoring system metrics.
- **Dozzle**: A real-time log viewer for Docker containers.
- **Glances**: A cross-platform monitoring tool that provides a comprehensive overview of your system.
- **Scrutiny**: A hard drive health monitoring tool that combines smartd monitoring with a web UI.
- **Speedtest Tracker**: A self-hosted internet speed test tracker.

### Home Automation & Network

- **Home Assistant**: An open-source home automation platform.
- **NetAlertX**: A network device monitoring tool with alerts.
- **WatchYourLAN**: A network device discovery and monitoring tool.

### Dashboard & Management

- **Homarr**: A modern, customizable dashboard for your services.
- **Homebox**: A simple and efficient file management and sharing tool.

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
- `DOCKER_MEDIA_BASEFOLDER`: The absolute path for media files.
- `BESZEL_SSH_KEY`: Your SSH public key for Beszel agent authentication.
- `BESZEL_TOKEN`: A secret token for the Beszel agent.
- `BESZEL_HUB_URL`: The public URL of your Beszel hub.
- `HOMARR_SECRET_ENCRYPTION_KEY`: An optional secret key for Homarr.
- `SPEEDTEST_TRACKER_APP_KEY`: An optional app key for Speedtest Tracker.

## Services & Ports

| Service               | Internal Port | Access Pattern                    | Description                          |
| --------------------- | ------------- | --------------------------------- | ------------------------------------ |
| **Beszel**            | `8090`        | `http://beszel:8090`              | Web interface for server monitoring. |
| **Dashdot**           | `3001`        | `http://dashdot:3001`             | Modern server dashboard.             |
| **Dozzle**            | `8080`        | `http://dozzle:8080`              | Real-time Docker log viewer.         |
| **Glances**           | `61208`       | `http://glances:61208`            | System monitoring web UI/API.        |
| **Home Assistant**    | `8123`        | `http://<host-ip>:8123`           | Home automation platform.            |
| **Homebox**           | `7745`        | `http://homebox:7745`             | Asset and inventory management.      |
| **Homarr**            | `7575`        | `http://homarr:7575`              | Customizable service dashboard.      |
| **NetAlertX**         | `20211`       | `http://<host-ip>:20211`          | Network device monitoring.           |
| **Scrutiny**          | `8080`        | `http://scrutiny:8080`            | Hard drive health monitoring UI.     |
| **Speedtest Tracker** | `80`          | `http://speedtest-tracker:80`     | Internet speed test tracker.         |
| **WatchYourLAN**      | `8840`        | `http://<host-ip>:8840`           | Network device discovery.            |

> **Note:** The services that sit on `npm_network` are meant to be reverse-proxied via Nginx Proxy Manager. Host-network services keep their direct host endpoints.

## Container Images

| Service           | Image                                            |
| ----------------- | ------------------------------------------------ |
| Beszel            | `henrygd/beszel:latest`                          |
| Beszel Agent      | `henrygd/beszel-agent:latest`                    |
| Dashdot           | `mauricenino/dashdot:latest`                     |
| Dozzle            | `amir20/dozzle:latest`                           |
| Glances           | `nicolargo/glances:latest-full`                  |
| Home Assistant    | `linuxserver/homeassistant:latest`               |
| Homebox           | `ghcr.io/sysadminsmedia/homebox:latest-rootless` |
| Homarr            | `ghcr.io/homarr-labs/homarr:latest`              |
| NetAlertX         | `jokobsk/netalertx:latest`                       |
| Scrutiny          | `ghcr.io/analogj/scrutiny:master-omnibus`        |
| Speedtest Tracker | `linuxserver/speedtest-tracker:latest`           |
| WatchYourLAN      | `aceberg/watchyourlan:v2`                        |

## Usage

1. **Initial Setup**:

   ```bash
   # Create required directories
   mkdir -p ${DOCKER_DATA_BASEFOLDER}/{beszel,homeassistant,homebox,homarr,netalertx,scrutiny,speedtest-tracker,wyl2,glances}
   ```

2. **Start the Stack**:

   ```bash
   docker compose up -d
   ```

3. **Access Services**:
   - Access Beszel at `http://localhost:8090`
   - Access Dashdot at `http://localhost:3002`
   - Access Dozzle at `http://localhost:8081`
   - Access Glances at `http://localhost:61208`
   - Access Home Assistant at `http://localhost:8123`
   - Access Homebox at `http://localhost:3100`
   - Access Homarr at `http://localhost:7575`
   - Access NetAlertX at `http://localhost:20211`
   - Access Scrutiny at `http://localhost:8083`
   - Access Speedtest Tracker at `http://localhost:8084`
   - Access WatchYourLAN at `http://localhost:8840`

## Security Considerations

**⚠️ Privileged Access & Host Mode**:

- **Beszel Agent**: Runs in `network_mode: host` to monitor the host system.
- **Dashdot**: Runs with `privileged: true` for full host access for system metrics.
- **Home Assistant**: Runs with `privileged: true` and `network_mode: host` for Bluetooth and device discovery.
- **NetAlertX** & **WatchYourLAN**: Use `network_mode: host` for network scanning.
- **Scrutiny**: Requires `SYS_RAWIO` capability and device access (e.g., `/dev/sda`) to read S.M.A.R.T. data.

**⚠️ Docker Socket Access**:
The following services mount `/var/run/docker.sock`, granting access to the Docker daemon:

- **Beszel Agent**, **Dozzle**, **Glances**, **Homarr**.

These configurations are powerful but require that the stack be deployed only in trusted networks.

## Additional Resources

- [Beszel Documentation](https://github.com/henrygd/beszel)
- [Dashdot Documentation](https://github.com/MauriceNino/dashdot)
- [Dozzle Documentation](https://github.com/amir20/dozzle)
- [Glances Documentation](https://glances.readthedocs.io/)
- [Home Assistant Documentation](https://www.home-assistant.io/docs/)
- [Homebox Documentation](https://github.com/sysadminsmedia/homebox)
- [Homarr Documentation](https://homarr.dev/)
- [NetAlertX Documentation](https://github.com/jokobsk/NetAlertX)
- [Scrutiny Documentation](https://github.com/AnalogJ/scrutiny)
- [Speedtest Tracker Documentation](https://docs.linuxserver.io/images/docker-speedtest-tracker)
- [WatchYourLAN Documentation](https://github.com/aceberg/WatchYourLAN)
