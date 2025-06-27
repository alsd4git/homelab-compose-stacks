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

3. Configure your environment variables:

   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Available Stacks

- [DDNS Stack](ddns/README.md) - Dynamic DNS updater
- [NPM Stack](npm-reverse-proxy/README.md) - Nginx Proxy Manager
- [Pi-hole Stack](pihole/README.md) - DNS sinkhole and ad blocker
- [WG-Easy Stack](wg-easy/README.md) - WireGuard VPN management
- [Tools Stack](tools/README.md) - Collection of utility tools
- [Netfroz Stack](netfroz/README.md) - Media management and automation
- [Home Dashboard & Monitoring Stack](home-dashboard-monitoring/README.md) - System monitoring and dashboards
- [RustDesk Relay Stack](rustdesk-relay/README.md) - Remote desktop relay
- [KaraKeep Stack](karakeep/README.md) - Media/bookmark organization
- [Transmission Stack](transmission/README.md) - Torrent client
- [Paperless-ngx Stack](paperless-ngx/README.md) - Document management
- [NPM Plus Stack](npmplus/README.md) - Enhanced Nginx Proxy Manager
- [Menu Gucci Stack](menu-gucci/README.md) - Service menu Telegram bot
- [Immich Stack](immich/README.md) - Photo management
- [AdGuard Stack](adguard/README.md) - DNS ad blocker

## Standardization Status

Each stack follows our standardization guidelines:

- ✅ Consistent formatting
- ✅ Environment variable fallbacks
- ✅ Standardized network naming
- ✅ Comprehensive documentation
- ✅ Security best practices

For detailed status of each stack, see [recap.md](recap.md).

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

- [recap.md](recap.md) - Comprehensive service overview
- [TODO.md](TODO.md) - Project roadmap and tasks
- Individual stack READMEs for detailed documentation
