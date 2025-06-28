# KaraKeep Stack

A modern bookmarks/media organization and management platform that helps you keep track of your digital content. This stack provides a web interface, Chrome-based browser automation, and a powerful search engine for efficient media management.

## Features

- **Web Interface**: Modern UI for managing and organizing media
- **Chrome Automation**: Headless Chrome for web scraping and automation
- **MeiliSearch Integration**: Fast and powerful search capabilities
- **Data Persistence**: Automatic data backup and recovery
- **Containerized Services**: Easy deployment and management
- **OpenAI Integration**: Optional AI-powered features (requires API key)
- **Authentication**: NextAuth integration for secure access

## Configuration

### Environment Variables

This stack uses named Docker volumes for data persistence and requires a `stack.env` file for environment variables.

Create a `stack.env` file in the stack directory with the following variables:

```env
# Required
KARAKEEP_VERSION=release
NEXTAUTH_SECRET=GENERATE_A_RANDOM_STRING # Use: openssl rand -base64 36
MEILI_MASTER_KEY=GENERATE_A_RANDOM_STRING # Use: openssl rand -base64 36
NEXTAUTH_URL=http://localhost:3000 # Set to your public URL if using a reverse proxy

# Optional: OpenAI integration (uncomment if needed)
# OPENAI_API_KEY=your-openai-api-key
```

### Volumes

The stack uses the following named volumes for data persistence:
- `data`: KaraKeep application data
- `meilisearch`: MeiliSearch database and configuration

## Port Documentation

### External Ports (Mapped to Host)
- `3005`: Web interface (external mapping)

### Internal Ports (Exposed for Reverse Proxy)
- `3000`: Web interface (internal, for reverse proxy or internal access)
- `9222`: Chrome remote debugging (internal, for reverse proxy or internal access)
- `7700`: MeiliSearch API (internal, for reverse proxy or internal access)

## Usage

1. **Setup Environment Variables**:
   - Create a `stack.env` file in the stack directory
   - Set the required environment variables as shown above
   - Generate random strings for `NEXTAUTH_SECRET` and `MEILI_MASTER_KEY`
   - Set `NEXTAUTH_URL` to your public URL if using a reverse proxy

2. **Start the Stack**:
   ```bash
   docker-compose up -d
   ```

3. **Access Web Interface**:
   - Navigate to `http://your-server:3005`
   - Complete the initial setup process

## Components

### Web Service (KaraKeep)

- **Image**: `ghcr.io/karakeep-app/karakeep:${KARAKEEP_VERSION:-release}`
- **Purpose**: Main web interface for media management
- **Features**:
  - User interface and authentication
  - Media organization and bookmarks
  - Search integration with MeiliSearch
  - Chrome automation integration
  - API endpoints

### Chrome Service

- **Image**: `gcr.io/zenika-hub/alpine-chrome:123`
- **Purpose**: Headless Chrome for web automation
- **Features**:
  - Web scraping and automation
  - Screenshot capture
  - PDF generation
  - Remote debugging capabilities

### MeiliSearch Service

- **Image**: `getmeili/meilisearch:v1.13.3`
- **Purpose**: Search engine for media content
- **Features**:
  - Fast and typo-tolerant search
  - Relevance scoring
  - Analytics disabled for privacy
  - Persistent data storage

## Security Considerations

- **Authentication**: Uses NextAuth for secure user authentication
- **Data Protection**: All data is stored in Docker named volumes
- **Network Security**: Internal services are not directly exposed
- **API Security**: Use environment variables for sensitive data
- **Regular Backups**: Recommended for data persistence

## Troubleshooting

### Common Issues

1. **Authentication Problems**:
   - Verify `NEXTAUTH_SECRET` is properly set in `stack.env`
   - Check `NEXTAUTH_URL` matches your setup
   - Ensure `MEILI_MASTER_KEY` is correctly configured

2. **Web Interface Issues**:
   - Check if all services are running: `docker-compose ps`
   - View web service logs: `docker-compose logs web`
   - Verify port availability and firewall settings

3. **Chrome Service Issues**:
   - Check Chrome logs: `docker-compose logs chrome`
   - Verify memory allocation for Chrome
   - Check for GPU-related issues (Chrome runs in headless mode)

4. **Search Issues**:
   - Check MeiliSearch logs: `docker-compose logs meilisearch`
   - Verify data persistence in volumes
   - Check search index status and configuration

### Verification Steps

1. Check container status:
   ```bash
   docker-compose ps
   ```

2. View service logs:
   ```bash
   docker-compose logs web
   docker-compose logs chrome
   docker-compose logs meilisearch
   ```

3. Test web interface accessibility:
   ```bash
   curl http://localhost:3005
   ```

## Additional Resources

- [KaraKeep Documentation](https://docs.karakeep.app/)
- [MeiliSearch Documentation](https://docs.meilisearch.com/)
- [Alpine Chrome Documentation](https://github.com/Zenika/alpine-chrome)
- [NextAuth Documentation](https://next-auth.js.org/)

## Maintenance

- **Updates**: Pull the latest images regularly for security updates
- **Backups**: Backup the Docker volumes for data persistence
- **Monitoring**: Monitor container logs for any issues or errors
- **Version Management**: Update `KARAKEEP_VERSION` as needed
