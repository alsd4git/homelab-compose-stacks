# Dockerini

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
   git clone https://github.com/alsd4git/dockerini.git
   cd dockerini
   ```

2. For each stack you want to use, create a local `.env` file from the example:

   ```bash
   cd <stack-name>
   cp .env.example .env
   cd ..
   ```

3. Edit the stack-specific variables in `.env` before deployment.

## Public Stacks

| Stack | Purpose |
| --- | --- |
| Automation | Docker event notifications, image monitoring, and container updates |
| Immich | Photo and video management |
| Infrastructure | Reverse proxy, DDNS, authentication, and identity services |
| KaraKeep | Bookmarks and media organization |
| Media | Media servers, downloaders, and automation |
| Monitoring | System monitoring, dashboards, and observability |
| Paperless-ngx | Document management and archival |
| Pi-hole | DNS sinkhole and network ad blocking |
| RustDesk Relay | Remote desktop relay infrastructure |
| Tracearr | Traceability and media import stack |
| Utilities | File management, document processing, and utility services |

## Standardization

Each public stack follows the same core conventions:

- Consistent formatting and compose structure
- Environment variable fallbacks
- Standardized network naming
- Clear documentation for setup and usage
- Security-focused defaults for public or internal deployment

### Recommended Practices

1. Pin critical infrastructure where stability matters most:
   - Databases
   - DNS services
   - Reverse proxies
   - Identity and auth services

2. Allow faster-moving apps to track `latest` when appropriate:
   - Media applications
   - Monitoring tools
   - Utility services
   - Automation helpers

3. Keep the update strategy deliberate:
   - Use [automation](automation/README.md) for container event notifications and image tracking
   - Pin or test critical infrastructure updates before rollout
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

## Development

### Pre-commit Hooks

1. Install [uv](https://github.com/astral-sh/uv) if needed.
2. Install pre-commit with `uv tool install pre-commit`.
3. Install the repo hooks with `uv run pre-commit install`.
4. Optionally run the full check with `uv run pre-commit run --all-files`.

The pre-commit setup keeps YAML consistent with `yamllint`, enforces whitespace hygiene, and validates `.env` files with `dotenv-linter`.

## Additional Resources

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Portainer Documentation](https://docs.portainer.io/)
- Individual stack READMEs in each folder
