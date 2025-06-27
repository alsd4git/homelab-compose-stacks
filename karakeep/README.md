# KaraKeep Stack

A modern bookmarks/media organization and management platform that helps you keep track of your digital content. This stack provides a web interface, Chrome-based browser automation, and a powerful search engine for efficient media management.

## Features

- **Web Interface**: Modern UI for managing and organizing media
- **Chrome Automation**: Headless Chrome for web scraping and automation
- **MeiliSearch Integration**: Fast and powerful search capabilities
- **Data Persistence**: Automatic data backup and recovery
- **Containerized Services**: Easy deployment and management
- **OpenAI Integration**: Optional AI-powered features (requires API key)

## Configuration

### Environment Variables

Create a `.env` file in the stack directory with the following variables:

```env
# Required
DOCKER_DATA_BASEFOLDER=/path/to/your/data

# Optional
KARAKEEP_VERSION=release  # Default: release
OPENAI_API_KEY=your-key   # Optional: For AI features
```

### Port Mappings

- **Web Interface**: 3005:3000
- **Chrome Debug**: 9222 (internal)
- **MeiliSearch**: 7700 (internal)

## Ports

- **Web Service**
  - 3005:3000 (mapped): Web UI (external)
  - 3000 (exposed): Web UI (internal, for reverse proxy or internal access)
- **Chrome Service**
  - 9222 (exposed): Chrome remote debugging (internal, for reverse proxy or internal access)
- **MeiliSearch Service**
  - 7700 (exposed): MeiliSearch API (internal, for reverse proxy or internal access)

## Usage

1. **Setup**:

   ```bash
   # Create the data directory
   mkdir -p ${DOCKER_DATA_BASEFOLDER}/karakeep
   ```

2. **Deployment**:

   ```bash
   docker compose up -d
   ```

3. **Access**:
   - Web Interface: `http://your-server:3005`
   - MeiliSearch: `http://meilisearch:7700` (internal)

## Components

### Web Service

- **Image**: `ghcr.io/karakeep-app/karakeep`
- **Purpose**: Main web interface for media management
- **Features**:
  - User interface
  - Media organization
  - Search integration
  - API endpoints

### Chrome Service

- **Image**: `gcr.io/zenika-hub/alpine-chrome`
- **Purpose**: Headless Chrome for web automation
- **Features**:
  - Web scraping
  - Screenshot capture
  - PDF generation
  - Remote debugging

### MeiliSearch Service

- **Image**: `getmeili/meilisearch`
- **Purpose**: Search engine for media content
- **Features**:
  - Fast search
  - Typo tolerance
  - Relevance scoring
  - Analytics disabled

## Security Notes

1. **Data Protection**:
   - All data is stored in Docker volumes
   - Regular backups recommended
   - Sensitive data should be encrypted

2. **Network Security**:
   - Internal services are not exposed to the internet
   - Web interface should be behind a reverse proxy
   - Consider implementing authentication

3. **API Security**:
   - OpenAI API key should be kept secure
   - Use environment variables for sensitive data
   - Implement rate limiting if needed

## Troubleshooting

1. **Web Interface Issues**:
   - Check if all services are running: `docker compose ps`
   - View web service logs: `docker compose logs web`
   - Verify port availability

2. **Chrome Service Issues**:
   - Check Chrome logs: `docker compose logs chrome`
   - Verify memory allocation
   - Check for GPU-related issues

3. **Search Issues**:
   - Check MeiliSearch logs: `docker compose logs meilisearch`
   - Verify data persistence
   - Check search index status

## Additional Resources

- [KaraKeep Documentation](https://docs.karakeep.app/)
- [MeiliSearch Documentation](https://docs.meilisearch.com/)
- [Alpine Chrome Documentation](https://github.com/Zenika/alpine-chrome)
