# Homelab Compose Stacks

[![CI](https://github.com/alsd4git/homelab-compose-stacks/actions/workflows/ci.yml/badge.svg)](https://github.com/alsd4git/homelab-compose-stacks/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

> Formerly **Dockerini**. This is the same repository, with a name that better
> describes its purpose.

Curated public Docker Compose stacks for a homelab, designed to stay consistent, documented, and easy to deploy through Portainer or Docker Compose.

## Features

- **Standardized stacks**: consistent naming, structure, and environment handling across the repo.
- **Reverse-proxy friendly**: services are organized to work cleanly with Nginx Proxy Manager.
- **Public-repo safe**: live hostnames and secrets stay out of the repository.
- **Maintainable defaults**: each stack ships with an `.env.example` file and clear usage notes.

## Configuration

### Prerequisites

- Docker installed and working
- Portainer if you want to deploy through a UI
- Basic familiarity with Docker Compose

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/alsd4git/homelab-compose-stacks.git
   cd homelab-compose-stacks
   ```

2. For each stack you want to use, create a local `.env` file from the example:

   ```bash
   cd <stack-name>
   cp .env.example .env
   cd ..
   ```

3. Edit the stack-specific variables in `.env` before deployment.

> Immich and Infrastructure also consume `stack.env` at runtime. Their stack READMEs
> document the local symlink that keeps it tied to the same untracked `.env` file.

## Public Stacks

| Stack | Purpose |
| --- | --- |
| [Automation](automation/README.md) | Docker event notifications, image monitoring, and container updates |
| [Forgejo](forgejo/README.md) | Private Git hosting with Postgres and SSH access |
| [GitLab Runner](gitlab-runner/README.md) | Self-hosted GitLab CI runner using the Docker executor |
| [Immich](immich/README.md) | Photo and video management |
| [Infrastructure](infrastructure/README.md) | Reverse proxy, DDNS, authentication, and identity services |
| [KaraKeep](karakeep/README.md) | Bookmarks and media organization |
| [LAN frontends](lan-frontends/README.md) | Frontends exposed only on the local network |
| [Media](media/README.md) | Media servers, downloaders, and automation |
| [Monitoring](monitoring/README.md) | System monitoring, dashboards, and observability |
| [Paperless-ngx](paperless-ngx/README.md) | Document management and archival |
| [Pi-hole](pihole/README.md) | DNS sinkhole and network ad blocking |
| [RomM](romm/README.md) | Game library management |
| [RustDesk Relay](rustdesk-relay/README.md) | Remote desktop relay infrastructure |
| [Tracearr](tracearr/README.md) | Traceability and media import stack |
| [Utilities](utilities/README.md) | File management, document processing, and utility services |

## Standardization

Each public stack follows the same core conventions:

- Consistent formatting and compose structure
- Environment variable fallbacks
- Standardized network naming
- Clear documentation for setup and usage
- Security-focused defaults for public or internal deployment

### Recommended Practices

1. Pin critical infrastructure where compatibility matters most:
   - Databases
   - DNS services
   - Reverse proxies
   - Identity and auth services

   Use a floating tag only when the stack README documents why it follows the
   upstream reference and backups or rollback are available.

2. Allow faster-moving apps to track `latest` when appropriate:
   - Media applications
   - Monitoring tools
   - Utility services
   - Automation helpers

3. Keep the update strategy deliberate:
   - Use [automation](automation/README.md) for container event notifications and image tracking
   - Pin or test critical infrastructure updates before rollout
   - Record any intentional floating tag in its stack README, especially for stateful services
   - Keep a reverse proxy and monitoring in place for public services

## Folder Structure

Each stack folder follows the same basic shape:

```bash
/stack-name
├── compose.yaml
├── README.md
├── .env.example
└── /resources
```

## Usage

1. Choose a stack from the table above.
2. Read the stack README for its specific requirements.
3. Copy `.env.example` to `.env` and fill in the local values.
4. Deploy the stack:

   ```bash
   docker compose up -d
   ```

Before updating a stateful stack, back up its database and persistent volumes, record the currently deployed image versions, and read the upstream migration notes. Validate the rendered configuration with `docker compose config` before deployment. A rollback requires both the previous images and data compatible with those versions.

## Development

### Pre-commit hooks

1. Install [uv](https://github.com/astral-sh/uv) if needed.
2. Install pre-commit with `uv tool install pre-commit`.
3. Install the repo hooks with `uv run pre-commit install`.
4. Optionally run the full check with `uv run pre-commit run --all-files`.

The pre-commit setup keeps YAML consistent with `yamllint`, enforces whitespace hygiene, and validates `.env` files with `dotenv-linter`. GitHub Actions also validates the Compose configuration for public stacks that have complete example environments.

## Additional Resources

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Portainer Documentation](https://docs.portainer.io/)
- Individual stack READMEs in each folder
