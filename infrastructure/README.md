# Infrastructure Stack

Core infrastructure services for your homelab, including reverse proxy, dynamic DNS, authentication, and certificate management.

## Included Services

- **Nginx Proxy Manager**: A user-friendly interface for managing Nginx reverse proxy hosts and SSL certificates.
- **DDNS Updater**: Automatically updates your dynamic DNS records with your public IP address.
- **Pocket ID**: A passkey-based OIDC provider for passwordless authentication.
- **TinyAuth**: A lightweight authentication middleware that integrates with Pocket ID to protect your services.
- **Step CA**: A private certificate authority for managing internal TLS/mTLS certificates.
- **VaultLS**: A service for securely storing and managing secrets.

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
- `YOUR_DOMAIN`: Your primary domain name.
- **DDNS Updater**: Credentials for your DNS provider (e.g., Cloudflare, DuckDNS).
- **Pocket ID & TinyAuth**: Client ID and secret for the OIDC integration.
- **Step CA**: Configuration for your private certificate authority.
- **VaultLS**: A secret key and URL for the VaultLS service.

## Services & Ports

| Service                 | External Port     | Internal Port     | Description                                            |
| ----------------------- | ----------------- | ----------------- | ------------------------------------------------------ |
| **Nginx Proxy Manager** | `80`, `443`, `83` | `80`, `443`, `81` | HTTP/S traffic and admin UI.                           |
| **DDNS Updater**        | `8001`            | `8000`            | Web UI for monitoring DDNS updates.                    |
| **Step CA**             | `9001`            | `9000`            | Private certificate authority API.                     |
| **Pocket ID**           | -                 | `1411`            | OIDC provider (exposed via reverse proxy).             |
| **TinyAuth**            | -                 | `3000`            | Authentication middleware (exposed via reverse proxy). |
| **VaultLS**             | -                 | `80`              | Secrets management (exposed via reverse proxy).        |

> **Note:** It is recommended to use a reverse proxy for external access rather than exposing ports directly.

## Container Images

| Service             | Image                              |
| ------------------- | ---------------------------------- |
| DDNS Updater        | `qmcgaw/ddns-updater`              |
| Nginx Proxy Manager | `jc21/nginx-proxy-manager:latest`  |
| Step CA             | `smallstep/step-ca`                |
| TinyAuth            | `ghcr.io/steveiliop56/tinyauth:v4` |
| Pocket ID           | `ghcr.io/pocket-id/pocket-id:v1`   |
| VaultLS             | `ghcr.io/7ritn/vaultls:latest`     |

## Usage

1. **Setup Environment Variables**:
   - Copy the `.env.example` to `.env`.
   - Configure the variables for each service as needed.

2. **Deploy the Stack**:

   ```bash
   docker compose up -d
   ```

3. **Access Services**:
   - **Nginx Proxy Manager**: `http://<your-server-ip>:83`
   - **DDNS Updater**: `http://<your-server-ip>:8001`
   - Other services should be accessed through the reverse proxy you configure in Nginx Proxy Manager.

## Security Considerations

- **Nginx Proxy Manager**: Change the default admin credentials (`admin@example.com` / `changeme`) immediately after deployment.
- **Secrets**: Securely store all secrets and API keys in your `.env` file and do not commit it to version control.
- **Network Exposure**: Only expose Nginx Proxy Manager's HTTP/S ports (`80`/`443`) to the internet. The admin panel and other services should be restricted to your local network or accessed via a VPN.

## Additional Resources

- [Nginx Proxy Manager Documentation](https://nginxproxymanager.com/)
- [DDNS Updater Documentation](https://github.com/qdm12/ddns-updater)
- [Pocket ID Documentation](https://pocket-id.org/)
- [TinyAuth Documentation](https://tinyauth.app/)
- [Step CA Documentation](https://smallstep.com/docs/step-ca)
- [VaultLS Documentation](https://github.com/7rit/vaultls)
