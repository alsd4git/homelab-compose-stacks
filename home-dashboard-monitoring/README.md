# Home Dashboard & Monitoring Stack

A comprehensive stack for home monitoring, dashboard management, and system metrics visualization. This stack provides tools for monitoring system resources, managing home automation, and creating customizable dashboards.

## Features

### System Monitoring

- **Dashdot**: System metrics dashboard with hardware monitoring
- **Glances**: Real-time system monitoring and metrics
- **Dozzle**: Docker container log viewer

### Home Automation

- **Home Assistant**: Open-source home automation platform
- **NetAlertX**: Network device monitoring and alerts
- **WatchYourLAN**: Network device discovery and monitoring

### Dashboard Management

- **Homepage**: Customizable dashboard for your services
- **Homarr**: Modern dashboard for your services
- **Homebox**: File sharing and management dashboard

## Configuration

### Required Environment Variables

Create a `.env` file with the following variables:

```env
DOCKER_DATA_BASEFOLDER=/path/to/data
DOCKER_MEDIA_BASEFOLDER=/path/to/media
```

## Services

### Dashdot

- **Port**: 3002
- **Features**:
  - System metrics visualization
  - Hardware temperature monitoring
  - Resource usage tracking
  - Host information display
- **Health Check**: Enabled

### Dozzle

- **Port**: 8081
- **Features**:
  - Real-time log viewing
  - Docker container log management
  - Search and filter capabilities
  - Log streaming

### Glances

- **Port**: 61208
- **Features**:
  - System resource monitoring
  - Process management
  - Network statistics
  - Web interface
- **Health Check**: Enabled

### Home Assistant

- **Port**: 8123
- **Features**:
  - Home automation control
  - Device integration
  - Automation rules
  - Custom dashboards
- **Network Mode**: Host (required for device discovery)
- **Health Check**: Enabled

### Homepage

- **Port**: 3001
- **Features**:
  - Customizable dashboard
  - Service status monitoring
  - Docker integration
  - Widget management
- **Health Check**: Enabled

### Homebox

- **Port**: 3100
- **Features**:
  - File sharing
  - User management
  - Access control
  - File organization
- **Health Check**: Enabled

### Homarr

- **Port**: 7575
- **Features**:
  - Service dashboard
  - Custom widgets
  - Docker integration
  - Theme customization
- **Health Check**: Enabled

### NetAlertX

- **Port**: 20211
- **Features**:
  - Network device monitoring
  - Device alerts
  - Device history
  - Custom notifications
- **Network Mode**: Host
- **Health Check**: Enabled

### WatchYourLAN

- **Port**: 8840
- **Features**:
  - Network device discovery
  - Device tracking
  - Custom notifications
  - Interface monitoring
- **Network Mode**: Host
- **Health Check**: Enabled

## Ports

- **Dashdot**
  - 3002:3001 (mapped): Web UI (external)
  - 3001 (exposed): Web UI (internal, for reverse proxy or internal access)
- **Dozzle**
  - 8081:8080 (mapped): Web UI (external)
  - 8080 (exposed): Web UI (internal, for reverse proxy or internal access)
- **Glances**
  - 61208:61208 (mapped): Web UI/API (external)
  - 61208 (exposed): Web UI/API (internal, for reverse proxy or internal access)
- **Home Assistant**
  - 8123:8123 (mapped): Web UI (external)
  - 8123 (exposed): Web UI (internal, for reverse proxy or internal access)
- **Homepage**
  - 3001:3000 (mapped): Web UI (external)
  - 3000 (exposed): Web UI (internal, for reverse proxy or internal access)
- **Homebox**
  - 3100:7745 (mapped): Web UI (external)
  - 7745 (exposed): Web UI (internal, for reverse proxy or internal access)
- **Homarr**
  - 7575:7575 (mapped): Web UI (external)
  - 7575 (exposed): Web UI (internal, for reverse proxy or internal access)
- **NetAlertX**
  - 20211:20211 (mapped): Web UI (external)
  - 20211 (exposed): Web UI (internal, for reverse proxy or internal access)
- **WatchYourLAN**
  - 8840:8840 (mapped): Web UI (external)
  - 8840 (exposed): Web UI (internal, for reverse proxy or internal access)

> **Note:** Both mapped and exposed ports are documented for clarity. The long-term plan is to reduce direct port exposure and use a reverse proxy for internal services.

## Usage

1. **Initial Setup**:

   ```bash
   # Create required directories
   mkdir -p ${DOCKER_DATA_BASEFOLDER}/{homeassistant,homepage,homebox,homarr,netalertx,watchyourlan,glances}
   ```

2. **Start the Stack**:

   ```bash
   docker compose up -d
   ```

3. **Configure Services**:
   - Access Dashdot at `http://localhost:3002`
   - Access Dozzle at `http://localhost:8081`
   - Access Glances at `http://localhost:61208`
   - Access Home Assistant at `http://localhost:8123`
   - Access Homepage at `http://localhost:3001`
   - Access Homebox at `http://localhost:3100`
   - Access Homarr at `http://localhost:7575`
   - Access NetAlertX at `http://localhost:20211`
   - Access WatchYourLAN at `http://localhost:8840`

## Network Configuration

Most services use a bridge network for internal communication. However, some services (Home Assistant, NetAlertX, WatchYourLAN) require host network mode for proper device discovery and monitoring.

## Security Notes

1. **Network Access**: Some services require host network mode for proper functionality
2. **Authentication**: Enable authentication on all services
3. **File Permissions**: Ensure proper permissions for mounted volumes
4. **Updates**: Keep all services updated to the latest versions

## Troubleshooting

1. **Service Not Starting**:
   - Check logs: `docker compose logs <service_name>`
   - Verify environment variables
   - Check port conflicts
   - Verify network mode requirements

2. **Device Discovery Issues**:
   - Verify host network mode for relevant services
   - Check interface permissions
   - Verify network connectivity

3. **Dashboard Access Issues**:
   - Check service health status
   - Verify port mappings
   - Check authentication settings

## Additional Resources

- [Dashdot Documentation](https://github.com/MauriceNino/dashdot)
- [Dozzle Documentation](https://github.com/amir20/dozzle)
- [Glances Documentation](https://glances.readthedocs.io/)
- [Home Assistant Documentation](https://www.home-assistant.io/docs/)
- [Homepage Documentation](https://github.com/gethomepage/homepage)
- [Homebox Documentation](https://github.com/sysadminsmedia/homebox)
- [Homarr Documentation](https://github.com/ajnart/homarr)
- [NetAlertX Documentation](https://github.com/jokobsk/NetAlertX)
- [WatchYourLAN Documentation](https://github.com/aceberg/WatchYourLAN)
