# Paperless-ngx Stack

A document management system with a web interface for organizing, searching, and archiving digital documents.

## Features
- Web-based UI for document management
- OCR and full-text search
- Import/export folders
- Persistent configuration and media storage
- Optional Tika and Gotenberg integration for document conversion

## Configuration

### Required Environment Variables
Create a `.env` file with the following variables:
```env
DOCKER_DATA_BASEFOLDER=/opt/docker/data
```

## Ports

- 8002:8000 (mapped): Web UI/API (external)
- 8000 (exposed): Web UI/API (internal, for reverse proxy or internal access)

> **Note:** Both mapped and exposed ports are documented for clarity. The long-term plan is to reduce direct port exposure and use a reverse proxy for internal services.

## Usage

1. Configure your environment variables
2. Deploy the stack:
   ```bash
   docker compose up -d
   ```
3. Access the web interface at `http://your-server:8002`
4. Import documents by placing them in the `consume` folder
5. Export documents from the `export` folder

## Security Notes
- Change the default admin credentials
- Only expose necessary ports to the internet
- Keep Paperless-ngx updated
- Monitor logs for unusual activity

## Troubleshooting
- Check logs: `docker logs paperless-ngx`
- Port conflicts: Ensure no other services use the same ports
- Import/export issues: Verify volume permissions and free space

## Additional Resources
- [Paperless-ngx Documentation](https://docs.paperless-ngx.com/)
- [Gotenberg Documentation](https://gotenberg.dev/)
- [Tika Documentation](https://tika.apache.org/) 