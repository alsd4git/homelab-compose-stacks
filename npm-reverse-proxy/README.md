# Nginx Proxy Manager Stack

This stack provides a reverse proxy solution using [Nginx Proxy Manager](https://nginxproxymanager.com/) with optional mTLS support through [Step CA](https://smallstep.com/docs/step-ca).

## Features

- Web-based UI for managing Nginx reverse proxy
- Automatic SSL certificate management with Let's Encrypt
- Optional mTLS support with Step CA
- Custom CA certificate support
- IPv6 support (configurable)

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Base directory for persistent data
DOCKER_DATA_BASEFOLDER=/opt/docker/data

# Step CA configuration (if using mTLS)
STEP_CA_NAME=your_ca_name
STEP_CA_DNS_NAMES=your_dns_names
STEP_CA_PASSWORD=your_password
```

### Ports

- **80:80** (mapped): Public HTTP traffic (external)
- **443:443** (mapped): Public HTTPS traffic (external)
- **83:81** (mapped): Admin Web UI (external)
- **80** (exposed): Internal HTTP port for reverse proxy or internal access
- **443** (exposed): Internal HTTPS port for reverse proxy or internal access
- **81** (exposed): Internal Admin Web port for reverse proxy or internal access
- **9001:9000** (mapped, step-ca): Step CA API (external)
- **9000** (exposed, step-ca): Internal Step CA API port for reverse proxy or internal access

> **Note:** Both mapped and exposed ports are documented for clarity. The long-term plan is to reduce direct port exposure and use a reverse proxy for internal services.

### Volumes

- `/data`: NPM data and configuration
- `/etc/letsencrypt`: SSL certificates
- `/etc/nginx/ssl/homelab`: Custom CA certificates (optional)

## Usage

1. Configure your environment variables
2. Deploy the stack:

   ```bash
   docker compose up -d
   ```

3. Access the admin UI at `http://your-server:83`
   - Default login: `admin@example.com`
   - Default password: `changeme`

## mTLS Configuration

If you're using mTLS with Step CA:

1. Ensure your custom CA certificate is mounted at `/etc/nginx/ssl/homelab/root_ca.crt`
2. In the NPM UI, for each proxy host:
   - Go to the SSL tab
   - Add the following lines:

     ```bash
     ssl_client_certificate /etc/nginx/ssl/homelab/root_ca.crt;
     ssl_verify_client on;
     ```

For more information on mTLS setup, see [mtls-cli](https://github.com/alsd4git/mtls-cli).

## Security Notes

- Change the default admin credentials immediately
- Keep your Step CA password secure
- Regularly update SSL certificates
- Consider using a firewall to restrict access to the admin UI
- Keep your custom CA certificates secure

## Troubleshooting

1. Check logs:

   ```bash
   docker logs nginx-proxy-manager
   docker logs step-ca  # if using mTLS
   ```

2. Common issues:
   - SSL certificate errors: Check Let's Encrypt configuration
   - mTLS failures: Verify client certificates
   - Port conflicts: Ensure no other services use the same ports 