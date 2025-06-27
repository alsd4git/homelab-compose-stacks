# WireGuard Easy Stack

This stack provides a simple WireGuard VPN solution using [wg-easy](https://github.com/wg-easy/wg-easy), a web-based WireGuard VPN management interface.

## Features

- Web-based UI for managing WireGuard VPN
- Automatic client configuration generation
- QR code support for mobile devices
- Integration with Pi-hole for DNS
- DDNS support for dynamic IP addresses
- Secure password protection

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Base directory for persistent data
DOCKER_DATA_BASEFOLDER=/opt/docker/data

# WireGuard configuration
DDNS=your.domain.com          # Your public domain or IP
PASSWORD_HASH=your_hash       # bcrypt hash of your admin password
PI-HOLE-IP=192.168.1.100     # Your Pi-hole IP address
```

### Generating Password Hash

To generate a bcrypt hash for the admin password:

1. Using Python:

   ```bash
   python3 -c 'import bcrypt; print(bcrypt.hashpw("your_password".encode(), bcrypt.gensalt()).decode())'
   ```

2. Using Node.js:

   ```bash
   node -e "const bcrypt = require('bcrypt'); bcrypt.hash('your_password', 10).then(hash => console.log(hash));"
   ```

### Ports

- **51820:51820/udp** (mapped): WireGuard VPN (external)
- **51821:51821/tcp** (mapped): Web interface (external)
- **51820/udp** (exposed): WireGuard VPN (internal, for reverse proxy or internal access)
- **51821/tcp** (exposed): Web interface (internal, for reverse proxy or internal access)

> **Note:** Both mapped and exposed ports are documented for clarity. The long-term plan is to reduce direct port exposure and use a reverse proxy for internal services.

## Usage

1. Configure your environment variables
2. Deploy the stack:

   ```bash
   docker compose up -d
   ```

3. Access the web interface at `http://your-server:51821`
4. Add clients through the web interface
5. Download or scan QR codes for client configuration

## Client Configuration

### Desktop Clients

1. Download the client configuration file
2. Import it into your WireGuard client
3. Connect to the VPN

### Mobile Clients

1. Scan the QR code with your WireGuard app
2. The configuration will be automatically imported
3. Connect to the VPN

## Network Configuration

### DNS Settings

- Default DNS is set to Pi-hole IP
- Clients can use Pi-hole for ad blocking
- DNS queries are routed through the VPN

### Routing

- All traffic is routed through the VPN by default
- Split tunneling can be configured per client
- Custom routes can be added in the web interface

## Security Notes

- Use a strong admin password
- Keep your WireGuard private keys secure
- Regularly update the server
- Monitor client connections
- Use Pi-hole for additional security
- Consider using a reverse proxy for the web interface

## Troubleshooting

1. Check logs:

   ```bash
   docker logs wg-easy
   ```

2. Common issues:
   - Connection failures: Check port forwarding
   - DNS issues: Verify Pi-hole configuration
   - Web interface access: Check port 51821
   - Client connection: Verify client configuration

3. Testing connection:

   ```bash
   # On the server
   wg show
   
   # On the client
   ping 10.0.0.1
   ```

## Additional Resources

- [wg-easy GitHub Repository](https://github.com/wg-easy/wg-easy)
- [WireGuard Documentation](https://www.wireguard.com/)
- [Pi-hole Integration Guide](https://docs.pi-hole.net/) 