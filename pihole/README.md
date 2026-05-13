# Pi-hole Stack

This stack provides a network-wide ad blocking solution using [Pi-hole](https://pi-hole.net/), a DNS sinkhole that protects your devices from unwanted content.

## Features

- **Network-wide ad blocking**: DNS sinkhole protection for your devices.
- **DNS server**: customizable blocklists, local resolution, and encrypted upstream DNS via dnscrypt-proxy.
- **Web interface**: management UI for queries and settings.
- **Optional DHCP**: can run as a DHCP server if you enable it.
- **Custom DNS records**: supports local overrides and DNSmasq options.
- **Query logging**: built-in logs and statistics.

## Configuration

### Environment Variables

This stack requires a `.env` file for configuration. A complete and recommended set of variables can be found in the `.env.example` file.

The live stack also includes `dnscrypt-proxy` as an encrypted upstream resolver for Pi-hole.

**To get started:**

1. Copy the `.env.example` file to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file and edit the variables to match your environment.

**Key variables include:**

- `DOCKER_DATA_BASEFOLDER`: The absolute path on your host machine where Pi-hole will store its configuration.
- `PASSWORD`: The web interface password. This value is assigned to the `FTLCONF_webserver_api_password` variable in the `compose.yaml`.

### Services & Ports

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
- `/config` for `dnscrypt-proxy`: encrypted upstream resolver configuration and state

## Support Containers

Pi-hole runs with `dnscrypt-proxy` as an internal upstream resolver on the private `pihole_network`.

- `dnscrypt-proxy` is not published on a host port.
- The container only serves Pi-hole over the internal Docker network.
- Its persistent data lives under `${DOCKER_DATA_BASEFOLDER}/dnscrypt-proxy`.
- The Pi-hole container is pinned to `10.250.250.10` on `pihole_network`, with `dnscrypt-proxy` at `10.250.250.11`, so other containers can use that fixed IP as their DNS server when you want per-container query attribution.

> **Network note:** `pihole_network` is the owned bridge network for this stack; other stacks consume it as `external: true` when they need the fixed Pi-hole resolver IP for attribution or internal DNS.

> **Resolver note:** the Docker daemon keeps using its host resolver, while containers that should appear individually in Pi-hole must join `pihole_network` and point `dns` at the fixed Pi-hole IP. `dnscrypt-proxy` stays internal to Pi-hole and never needs a public endpoint.

## Container Images

| Service | Image                  |
| ------- | ---------------------- |
| Pi-hole | `pihole/pihole:latest` |

## Usage

1. **Setup Environment Variables**:
   - Copy the `.env.example` to `.env`.
   - Set the required environment variables as described above.
2. Deploy the stack:

   ```bash
   docker compose up -d
   ```

3. Access the web interface at `http://your-server:81` (or via your reverse proxy).
4. Set your devices' DNS server to your Pi-hole IP address.

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

## Blocklists and Allowlists

The current Pi-hole policy is based on two simple ideas:

- keep the allowlist small and explicit;
- use a compact, low-maintenance blocklist set instead of many overlapping lists.

### Allowlist

We currently use the Pi-hole whitelist sources from the "antigravity" allowlist set:

- <https://raw.githubusercontent.com/GoodnessJSON/PiHole-Whitelist/master/lists/whitelist.txt>
- <https://raw.githubusercontent.com/GoodnessJSON/PiHole-Whitelist/master/lists/referral-sites.txt>

### Blocklists

The blocklist set has been simplified to the Hagezi "Set and forget" combo:

- <https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/adblock/multi.txt>
- <https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/adblock/popupads.txt>
- <https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/adblock/tif.txt>
- <https://gitlab.com/hagezi/mirror/-/raw/main/dns-blocklists/adblock/fake.txt>

Older adlists are intentionally disabled rather than deleted, so they can be re-enabled quickly if a regression appears.

### Apply changes

After changing adlists or allowlists, rebuild gravity with:

```bash
pihole -g
```

## Database Maintenance

Pi-hole query history is kept intentionally short to avoid an oversized `pihole-FTL.db`.

- `maxDBdays` is set to `30` days.
- Periodic `VACUUM` keeps the SQLite database compact.
- This has already reclaimed roughly `1.4 GB` on the current installation.

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

- Change the default web interface password.
- Prefer a reverse proxy for the web interface.
- Keep Pi-hole updated.
- Regularly review and update blocklists.
- Monitor query logs for unusual activity.

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
- [Blocklist Collections](https://github.com/anudeepND/whitelist)
- [FireBog Blocklists](https://v.firebog.net/)
- [WaLLy3K Blocklist Repository](https://github.com/WaLLy3K/wally3k.github.io)
