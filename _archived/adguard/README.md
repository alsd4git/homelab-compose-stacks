# AdGuard Home Stack

A network-wide ad blocker and DNS filtering solution with a web interface for management and monitoring.

## Features
- Web-based UI for configuration and monitoring
- DNS filtering and ad blocking
- DHCP server and client support
- DNS-over-TLS, DNS-over-QUIC, DNSCrypt support
- Persistent configuration and data storage

## Configuration

### Required Environment Variables
Create a `.env` file with the following variables:
```env
DOCKER_DATA_BASEFOLDER=/opt/docker/data
```

## Ports

- 54:53/tcp (mapped): DNS (TCP, external)
- 54:53/udp (mapped): DNS (UDP, external)
- 67:67/udp (mapped): DHCP server (UDP, external)
- 68:68/udp (mapped, optional): DHCP client (UDP, external)
- 86:80/tcp (mapped): HTTP web interface (external)
- 443:443/tcp (mapped, optional): HTTPS web interface (external)
- 443:443/udp (mapped, optional): HTTPS web interface (UDP, external)
- 3000:3000/tcp (mapped): API (external)
- 853:853/tcp (mapped): DNS-over-TLS (DoT, external)
- 784:784/udp (mapped): DNS-over-QUIC (DoQ, external)
- 853:853/udp (mapped): DNS-over-DTLS (DoT, external)
- 8853:8853/udp (mapped): DNS-over-TLS (DoT, external)
- 5443:5443/tcp (mapped): DNSCrypt (TCP, external)
- 5443:5443/udp (mapped): DNSCrypt (UDP, external)
- 53/tcp (exposed): DNS (TCP, internal, for reverse proxy or internal access)
- 53/udp (exposed): DNS (UDP, internal, for reverse proxy or internal access)
- 67/udp (exposed): DHCP server (internal, for reverse proxy or internal access)
- 68/udp (exposed): DHCP client (internal, for reverse proxy or internal access)
- 80/tcp (exposed): HTTP web interface (internal, for reverse proxy or internal access)
- 443/tcp (exposed): HTTPS web interface (internal, for reverse proxy or internal access)
- 443/udp (exposed): HTTPS web interface (internal, for reverse proxy or internal access)
- 3000/tcp (exposed): API (internal, for reverse proxy or internal access)
- 853/tcp (exposed): DNS-over-TLS (DoT, internal, for reverse proxy or internal access)
- 784/udp (exposed): DNS-over-QUIC (DoQ, internal, for reverse proxy or internal access)
- 853/udp (exposed): DNS-over-DTLS (DoT, internal, for reverse proxy or internal access)
- 8853/udp (exposed): DNS-over-TLS (DoT, internal, for reverse proxy or internal access)
- 5443/tcp (exposed): DNSCrypt (TCP, internal, for reverse proxy or internal access)
- 5443/udp (exposed): DNSCrypt (UDP, internal, for reverse proxy or internal access)

> **Note:** Both mapped and exposed ports are documented for clarity. The long-term plan is to reduce direct port exposure and use a reverse proxy for internal services.

## Usage

1. Configure your environment variables
2. Deploy the stack:
   ```bash
   docker compose up -d
   ```
3. Access the web interface at `http://your-server:86`

## Security Notes
- Change the default admin credentials
- Only expose necessary ports to the internet
- Keep AdGuard Home updated
- Monitor logs for unusual activity

## Troubleshooting
- Check logs: `docker logs adguardhome`
- Port conflicts: Ensure no other services use the same ports
- DNS/DHCP issues: Verify volume permissions and free space

## Additional Resources
- [AdGuard Home Documentation](https://github.com/AdguardTeam/AdGuardHome/wiki)
- [AdGuard Home GitHub](https://github.com/AdguardTeam/AdGuardHome)
- [DNSCrypt Documentation](https://dnscrypt.info/)
- [DNS-over-TLS Documentation](https://tools.ietf.org/html/rfc7858)
- [DNS-over-QUIC Documentation](https://datatracker.ietf.org/doc/html/rfc9250)
- [Docker Compose Documentation](https://docs.docker.com/compose/) 