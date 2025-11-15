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

This stack requires a `.env` file for configuration. A complete and recommended set of variables can be found in the `.env.example` file.

**To get started:**

1. Copy the `.env.example` file to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file and edit the `DOCKER_DATA_BASEFOLDER` variable to match your environment.

### Port Requirements

The stack uses host network mode and requires the following ports:

- **HBBS (ID/Relay Server)**:
  - TCP 21115: used for the NAT type test.
  - TCP 21116: used for TCP hole punching and connection service.
  - UDP 21116: used for the ID registration and heartbeat service.
  - TCP 21118: used to support web clients.

- **HBBR (Relay Server)**:
  - TCP 21117: used for the Relay services.
  - TCP 21119: used to support web clients.

## Container Images

| Service | Image                             |
| ------- | --------------------------------- |
| hbbs    | `rustdesk/rustdesk-server:latest` |
| hbbr    | `rustdesk/rustdesk-server:latest` |

## Usage

1. **Setup Environment Variables**:
   - Copy the `.env.example` to `.env`.
   - Set the `DOCKER_DATA_BASEFOLDER` variable as described above.
2. **Create Data Directory**:

   ```bash
   mkdir -p ${DOCKER_DATA_BASEFOLDER}/RustDesk
   ```

3. **Deployment**:

   ```bash
   docker compose up -d
   ```

4. **Client Configuration**:
   - Install the RustDesk client.
   - Configure the client to use your relay server by setting the **ID Server** to `your-server-ip`. The relay server will be automatically configured.
   - You can also specify the relay server manually by setting **Relay Server** to `your-server-ip:21117`.

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
