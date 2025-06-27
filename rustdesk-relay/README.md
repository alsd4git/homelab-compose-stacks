# RustDesk Relay Stack

A self-hosted relay server for RustDesk, a free and open-source remote desktop software. This stack provides the necessary components for running your own RustDesk relay server, ensuring secure and private remote desktop connections.

## Features

- **Self-hosted Relay**: Run your own relay server for RustDesk connections
- **Dual Components**:
  - HBBS (ID/Relay Server): Handles ID registration and relay connections
  - HBBR (Relay Server): Manages data relay between clients
- **Persistent Storage**: Maintains connection data and configurations
- **Automatic Restart**: Services automatically restart unless explicitly stopped
- **Host Network Mode**: Optimized for direct network access

## Configuration

### Environment Variables

Create a `.env` file in the stack directory with the following variables:

```env
DOCKER_DATA_BASEFOLDER=/path/to/your/data
```

### Port Requirements

The stack uses host network mode and requires the following ports:

- **HBBS (ID/Relay Server)**:
  - TCP 21115: ID registration
  - TCP 21116: Relay connections
  - TCP 21117: NAT traversal
  - TCP 21118: TCP hole punching
  - TCP 21119: TCP hole punching

- **HBBR (Relay Server)**:
  - TCP 21116: Relay connections
  - TCP 21117: NAT traversal
  - TCP 21118: TCP hole punching
  - TCP 21119: TCP hole punching

## Usage

1. **Setup**:

   ```bash
   # Create the data directory
   mkdir -p ${DOCKER_DATA_BASEFOLDER}/RustDesk
   ```

2. **Deployment**:

   ```bash
   docker compose up -d
   ```

3. **Client Configuration**:
   - Install RustDesk client
   - Configure the client to use your relay server:
     - ID Server: `your-server-ip:21116`
     - Relay Server: `your-server-ip:21117`
     - API Server: `your-server-ip:21114`

## Security Notes

1. **Network Security**:
   - The stack uses host network mode for optimal performance
   - Ensure your firewall allows the required ports
   - Consider implementing rate limiting for the relay ports

2. **Data Security**:
   - All relay data is stored in the configured data directory
   - Regular backups of the data directory are recommended

## Troubleshooting

1. **Connection Issues**:
   - Verify all required ports are open and accessible
   - Check if the services are running: `docker compose ps`
   - View service logs: `docker compose logs`

2. **Performance Issues**:
   - Monitor system resources during peak usage
   - Consider adjusting system limits if needed
   - Check network bandwidth and latency

## Additional Resources

- [RustDesk Official Documentation](https://rustdesk.com/docs/en/self-host/)
- [RustDesk GitHub Repository](https://github.com/rustdesk/rustdesk)
- [RustDesk Server Documentation](https://github.com/rustdesk/rustdesk-server)
