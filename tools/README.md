# Tools Stack

This stack provides a collection of useful tools and utilities for your homelab environment.

## Included Tools

### 1. ConvertX
- **Purpose**: File conversion service
- **Port**: 3003
- **Features**:
  - File format conversion
  - Batch processing
  - Authentication support
  - Auto-cleanup

### 2. CUP (Container Update Puller)
- **Purpose**: Docker container update management
- **Port**: 8004
- **Features**:
  - Container update monitoring
  - Automatic updates
  - Update notifications

### 3. FileBrowser
- **Purpose**: Web-based file management
- **Port**: 8085
- **Features**:
  - File browsing
  - File sharing
  - User management
  - Multiple storage locations

### 4. Scrutiny
- **Purpose**: Hard drive health monitoring
- **Ports**: 8083 (Web UI), 8086 (InfluxDB)
- **Features**:
  - SMART monitoring
  - Health reporting
  - Historical data
  - Alert system

### 5. Speedtest Tracker
- **Purpose**: Internet speed monitoring
- **Port**: 8084
- **Features**:
  - Regular speed tests
  - Historical data
  - Custom schedules
  - Multiple server support

### 6. Stirling PDF
- **Purpose**: PDF processing and manipulation
- **Port**: 8082
- **Features**:
  - PDF conversion
  - OCR capabilities
  - PDF manipulation
  - Custom workflows

### 7. Telegram Files
- **Purpose**: Telegram file management
- **Port**: 6543
- **Features**:
  - File organization
  - Media management
  - Telegram integration
  - Health monitoring

### 8. UpSnap
- **Purpose**: Network device monitoring
- **Port**: 5001
- **Features**:
  - Device discovery
  - Status monitoring
  - Wake-on-LAN
  - Custom schedules

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Base directories
DOCKER_DATA_BASEFOLDER=/opt/docker/data
DOCKER_MEDIA_BASEFOLDER=/opt/docker/media

# Telegram configuration (for telegram-files)
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
```

### Port Configuration

Each tool uses specific ports:

- ConvertX: 3003
- CUP: 8004
- FileBrowser: 8085
- Scrutiny: 8083, 8086
- Speedtest Tracker: 8084
- Stirling PDF: 8082
- Telegram Files: 6543
- UpSnap: 5001

## Ports

- **ConvertX**
  - 3003:3000 (mapped): Web UI (external)
  - 3000 (exposed): Web UI (internal, for reverse proxy or internal access)
- **CUP**
  - 8004:8000 (mapped): Web UI (external)
  - 8000 (exposed): Web UI (internal, for reverse proxy or internal access)
- **FileBrowser**
  - 8085:80 (mapped): Web UI (external)
  - 80 (exposed): Web UI (internal, for reverse proxy or internal access)
- **Scrutiny**
  - 8083:8080 (mapped): Web UI (external)
  - 8086:8086 (mapped): InfluxDB (external)
  - 8080 (exposed): Web UI (internal, for reverse proxy or internal access)
  - 8086 (exposed): InfluxDB (internal, for reverse proxy or internal access)
- **Speedtest Tracker**
  - 8084:80 (mapped): Web UI (external)
  - 80 (exposed): Web UI (internal, for reverse proxy or internal access)
- **Stirling PDF**
  - 8082:8080 (mapped): Web UI (external)
  - 8080 (exposed): Web UI (internal, for reverse proxy or internal access)
- **Telegram Files**
  - 6543:80 (mapped): Web UI (external)
  - 80 (exposed): Web UI (internal, for reverse proxy or internal access)
- **UpSnap**
  - 5001 (host): Web UI (host networking, exposed directly on the host)

> **Note:** Both mapped and exposed ports are documented for clarity. The long-term plan is to reduce direct port exposure and use a reverse proxy for internal services.

## Usage

1. Configure your environment variables
2. Deploy the stack:

   ```bash
   docker compose up -d
   ```

3. Access each tool through its respective port

## Security Notes

- Most tools are exposed to the network
- Consider using a reverse proxy
- Set up authentication where available
- Keep tools updated
- Monitor access logs

## Troubleshooting

1. Check logs for specific tools:

   ```bash
   docker logs <container_name>
   ```

2. Common issues:
   - Port conflicts: Check for other services using the same ports
   - Permission issues: Verify volume permissions
   - Network issues: Check network configuration
   - Storage issues: Verify volume mounts

## Additional Resources

- [ConvertX Documentation](https://github.com/c4illin/convertx)
- [CUP Documentation](https://github.com/sergi0g/cup)
- [FileBrowser Documentation](https://filebrowser.org/)
- [Scrutiny Documentation](https://github.com/AnalogJ/scrutiny)
- [Speedtest Tracker Documentation](https://github.com/alexjustesen/speedtest-tracker)
- [Stirling PDF Documentation](https://github.com/Stirling-Tools/Stirling-PDF)
- [Telegram Files Documentation](https://github.com/jarvis2f/telegram-files)
- [UpSnap Documentation](https://github.com/seriousm4x/upsnap)
