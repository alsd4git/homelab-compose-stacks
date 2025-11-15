# Archived Stacks

This directory contains stacks that have been consolidated into larger infrastructure stacks or are no longer actively maintained.

## No Longer Used Stacks

### AdGuard (archived Nov 2025)
- **Reason**: No longer actively used in homelab
- **Alternative**: Pi-hole Stack for DNS filtering
- **Original service**: AdGuard Home DNS ad blocker

### Menu Gucci (archived Nov 2025)
- **Reason**: No longer actively used in homelab
- **Original service**: Telegram bot service menu

### WG-Easy (archived Nov 2025)
- **Reason**: No longer actively used in homelab
- **Original service**: WireGuard VPN management UI

## Stack Consolidation

### DDNS (archived Nov 2025)
- **Merged into**: [NPM Infrastructure Stack](../npm-reverse-proxy/README.md)
- **Reason**: DDNS is foundational infrastructure; consolidated with reverse proxy
- **Original service**: qmcgaw/ddns-updater
- **Configuration moved to**: npm-reverse-proxy/compose.yaml

### Pocket ID (archived Nov 2025)
- **Merged into**: [NPM Infrastructure Stack](../npm-reverse-proxy/README.md)
- **Reason**: Authentication provider needed by TinyAuth; part of core infrastructure
- **Original service**: ghcr.io/pocket-id/pocket-id
- **Configuration moved to**: npm-reverse-proxy/compose.yaml

### Beszel (archived Nov 2025)
- **Merged into**: [Home Dashboard & Monitoring Stack](../home-dashboard-monitoring/README.md)
- **Reason**: Server monitoring complements other monitoring dashboards
- **Original services**: henrygd/beszel + henrygd/beszel-agent
- **Configuration moved to**: home-dashboard-monitoring/compose.yaml

## Migration Notes

- Original README and environment variable documentation can still be found in this archived folder for reference
- All services are now managed from their parent stacks
- Environment variables have been consolidated in parent stack documentation
- See parent stack READMEs for deployment instructions
