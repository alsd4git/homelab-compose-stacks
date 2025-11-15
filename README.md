# Dockerini - Docker Compose Stacks Collection

A comprehensive collection of Docker Compose stacks for various services and applications, designed for easy deployment and management using Portainer. **All stacks in this repository are fully standardized and documented.**

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Available Stacks](#available-stacks)
- [Standardization Status](#standardization-status)
- [Folder Structure](#folder-structure)
- [Usage](#usage)
- [Documentation](#documentation)

## Introduction

Dockerini provides a collection of Docker Compose stacks for various services and applications, making it easy to deploy and manage containers using Portainer. Each stack is carefully standardized with:

- Consistent formatting and structure
- Fallback values for environment variables
- Standardized network naming
- Comprehensive documentation
- Security best practices

## Getting Started

### Prerequisites

- Docker installed on your system
- Portainer installed and configured
- Basic understanding of Docker and Docker Compose

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/alsd4git/dockerini.git
   ```

2. Navigate to the repository:

   ```bash
   cd dockerini
   ```

3. For each stack you want to deploy, configure its environment variables:

   ```bash
   cd <stack-name>
   cp .env.example .env
   # Edit .env with your stack-specific configuration
   cd ..
   ```

   Each stack has its own `.env.example` file in its directory with the required and optional variables for that service.

## Available Stacks

- [Automation Stack](automation/README.md) - Docker event notifications, image monitoring, and container updates
- [Immich Stack](immich/README.md) - Photo management and backup
- [Infrastructure Stack](infrastructure/README.md) - Reverse proxy, DDNS, authentication, and identity management
- [KaraKeep Stack](karakeep/README.md) - Bookmarks and media organization
- [Media Stack](media/README.md) - Media servers, downloaders, and automation (Jellyfin, Sonarr, Radarr, etc.)
- [Monitoring Stack](monitoring/README.md) - System monitoring, dashboards, and observability
- [Paperless-ngx Stack](paperless-ngx/README.md) - Document management and archival
- [Pi-hole Stack](pihole/README.md) - DNS sinkhole and network ad blocker
- [RustDesk Relay Stack](rustdesk-relay/README.md) - Remote desktop relay server
- [Utilities Stack](utilities/README.md) - File management, document processing, and utility services

## Standardization Status

Each stack follows our standardization guidelines:

- ✅ Consistent formatting
- ✅ Environment variable fallbacks
- ✅ Standardized network naming
- ✅ Comprehensive documentation
- ✅ Security best practices

### Recommended Practices

1. **Critical Services** (pin specific versions):
   - Databases (PostgreSQL, Redis, InfluxDB)
   - DNS services (Pi-hole, AdGuard)
   - Reverse proxies (Nginx Proxy Manager, Step CA)
   - Authentication services (Pocket ID)

2. **Non-Critical Services** (use latest tag):
   - Media applications (Jellyfin, Immich)
   - Monitoring tools (Glances, Dozzle)
   - Utility services (File browsers, converters)
   - Automation services (Sonarr, Radarr)

3. **Update Strategy**:
   - Enable [Watchtower](automation/README.md) for automatic updates of latest-tagged services
   - Pin versions for critical infrastructure and manually test updates
   - Use a reverse proxy and monitoring to catch issues quickly

## Container Restart Policies

This repository uses two restart policies strategically:

### `restart: unless-stopped` (Default - 62% of services)

Used for services that can tolerate manual stops:

- **User-facing services**: Dashboards, media servers, web interfaces
- **Non-critical services**: Monitoring displays, file browsers, converters
- **Deployment tools**: Allows graceful shutdown without auto-restart

**Behavior**: Container restarts automatically unless manually stopped

### `restart: always` (Special Cases - 38% of services)

Used for critical background services that must stay running:

- **Automation services**: [Watchtower](automation/README.md) (automatic updates), DIUN (image monitoring)
- **Notification services**: Telegram notifiers and alert delivery
- **Core infrastructure**: Services critical for other containers to function
- **Monitoring agents**: Services providing essential observability

**Behavior**: Container always restarts, even if manually stopped

### Decision Matrix

| Service Type                         | Restart Policy   | Reason                          |
| ------------------------------------ | ---------------- | ------------------------------- |
| Watchtower, DIUN, Telegram notifiers | `always`         | Must stay running to function   |
| Databases, DNS, Reverse proxies      | `unless-stopped` | Allow graceful maintenance      |
| Media servers, dashboards            | `unless-stopped` | User-facing; allow manual stops |
| Monitoring displays                  | `unless-stopped` | Non-critical visualization      |
| Utility services                     | `unless-stopped` | Safe to stop manually           |

## Folder Structure

Each stack folder contains:

```bash
/stack-name
├── compose.yaml      # Docker Compose configuration
├── README.md         # Stack documentation
├── .env.example      # Example environment variables
└── /resources        # Additional resources
```

## Usage

1. Choose a stack from the [Available Stacks](#available-stacks) section
2. Review the stack's README.md for specific requirements
3. Configure the environment variables
4. Deploy using Docker Compose:

   ```bash
   docker compose up -d
   ```

## Documentation

- Individual stack READMEs for detailed documentation
