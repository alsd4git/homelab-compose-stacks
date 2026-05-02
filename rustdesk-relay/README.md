# RustDesk Relay Stack

Self-hosted relay server for RustDesk remote desktop connections.

## Features

- **HBBS**: handles ID registration, NAT test, and connection coordination.
- **HBBR**: relays traffic between RustDesk clients.
- **Host networking**: provides the direct access model required by RustDesk relay.
- **Persistent storage**: connection data and state live under the configured data root.

## Configuration

### Environment Variables

Copy the example file to `.env`, then set the data root:

```bash
cp .env.example .env
```

Key variables:

- `DOCKER_DATA_BASEFOLDER`

### Port Requirements

This stack uses host networking and requires these ports:

| Component | Port | Protocol | Purpose |
| --- | --- | --- | --- |
| HBBS | `21115` | TCP | NAT type test |
| HBBS | `21116` | TCP | TCP hole punching and connection service |
| HBBS | `21116` | UDP | ID registration and heartbeat service |
| HBBS | `21118` | TCP | Web client support |
| HBBR | `21117` | TCP | Relay service |
| HBBR | `21119` | TCP | Web client support |

## Services & Ports

| Service | Access Pattern | Notes |
| --- | --- | --- |
| `hbbs` | host network | ID/relay server. |
| `hbbr` | host network | Relay server. |

## Container Images

| Service | Image |
| --- | --- |
| hbbs | `rustdesk/rustdesk-server:latest` |
| hbbr | `rustdesk/rustdesk-server:latest` |

## Usage

1. Copy `.env.example` to `.env`.
2. Create the data directory:

   ```bash
   mkdir -p ${DOCKER_DATA_BASEFOLDER}/RustDesk
   ```

3. Start the stack:

   ```bash
   docker compose up -d
   ```

4. Configure RustDesk clients to use your server IP and the relay port `21117` when needed.

## Security Notes

- The relay must be reachable on the required ports, so keep firewall rules explicit.
- Host networking is required here; deploy only on trusted infrastructure.
- Back up the data directory regularly.

## Additional Resources

- [RustDesk Self-Hosting Guide](https://rustdesk.com/docs/en/self-host/)
- [RustDesk Server GitHub](https://github.com/rustdesk/rustdesk-server)
