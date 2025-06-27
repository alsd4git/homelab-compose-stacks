# Pi-hole Stack

This stack provides a network-wide ad blocking solution using [Pi-hole](https://pi-hole.net/), a DNS sinkhole that protects your devices from unwanted content.

## Features

- Network-wide ad blocking
- DNS server with customizable blocklists
- Web interface for management
- Optional DHCP server
- Custom DNS records support
- Query logging and statistics

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Base directory for persistent data
DOCKER_DATA_BASEFOLDER=/opt/docker/data

# Pi-hole web interface password
PASSWORD=your_secure_password
```

### Ports

- **53:53/tcp** (mapped): DNS (TCP, external)
- **53:53/udp** (mapped): DNS (UDP, external)
- **81:80/tcp** (mapped, optional): Web interface (external, recommended to use reverse proxy instead)
- **443:443/tcp** (mapped, optional): HTTPS (self-signed cert, external, recommended to use reverse proxy instead)
- **67:67/udp** (mapped, optional): DHCP server (external, optional)
- **80** (exposed): Web interface (internal, for reverse proxy or internal access)
- **443** (exposed): HTTPS (self-signed cert, internal, for reverse proxy or internal access)
- **53** (exposed): DNS (internal, for internal container communication)
- **67** (exposed): DHCP (internal, for internal container communication)

> **Note:** Both mapped and exposed ports are documented for clarity. The long-term plan is to reduce direct port exposure and use a reverse proxy for internal services.

### Volumes

- `/etc/pihole`: Pi-hole configuration
- `/etc/dnsmasq.d`: DNS configuration

## Usage

1. Configure your environment variables
2. Deploy the stack:

   ```bash
   docker compose up -d
   ```

3. Access the web interface at `http://your-server:81`
4. Set your devices' DNS server to your Pi-hole IP address

## Custom DNS Configuration

### Adding Custom Domain Records

To add custom domain records (e.g., `*.yourdomain.com`), create a file in the dnsmasq.d directory:

1. Create a file named `02-custom.conf` in `${DOCKER_DATA_BASEFOLDER}/pihole/etc-dnsmasq.d/`:

   ```bash
   touch ${DOCKER_DATA_BASEFOLDER}/pihole/etc-dnsmasq.d/02-custom.conf
   ```

2. Add your custom domain configuration:

   ```conf
   # Add custom domain records
   address=/yourdomain.com/192.168.1.100
   address=/*.yourdomain.com/192.168.1.100
   
   # Add CNAME records
   cname=subdomain.yourdomain.com,host.yourdomain.com
   
   # Add PTR records (reverse DNS)
   ptr-record=1.1.168.192.in-addr.arpa,host.yourdomain.com
   ```

3. Restart Pi-hole to apply changes:

   ```bash
   docker restart pihole
   ```

### Common dnsmasq Options

```conf
# Cache size (number of DNS entries)
cache-size=10000

# Minimum TTL for cached entries
min-cache-ttl=3600

# Maximum TTL for cached entries
max-cache-ttl=86400

# Enable DNSSEC
dnssec

# Enable EDNS0
edns-packet-max=1232

# Enable query logging
log-queries

# Enable DHCP (if using Pi-hole as DHCP server)
dhcp-range=192.168.1.100,192.168.1.200,12h
```

## Security Notes

- Change the default web interface password
- Consider using a reverse proxy for the web interface
- Keep Pi-hole updated
- Regularly review and update blocklists
- Monitor query logs for unusual activity

## Troubleshooting

1. Check logs:

   ```bash
   docker logs pihole
   ```

2. Common issues:
   - DNS resolution failures: Check network configuration
   - Web interface access: Verify port forwarding
   - Custom domains not working: Check dnsmasq configuration
   - Blocking not working: Verify DNS settings on devices

3. Testing DNS resolution:

   ```bash
   dig @your-pihole-ip example.com
   nslookup example.com your-pihole-ip
   ```

## Additional Resources

- [Pi-hole Documentation](https://docs.pi-hole.net/)
- [dnsmasq Documentation](https://thekelleys.org.uk/dnsmasq/docs/dnsmasq-man.html)
- [Pi-hole GitHub Repository](https://github.com/pi-hole/docker-pi-hole/)


TODO: add sections about: https://github.com/anudeepND/whitelist -- https://v.firebog.net/ -- https://github.com/WaLLy3K/wally3k.github.io