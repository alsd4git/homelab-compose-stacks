# Paperless-ngx Stack

A document management system with a web interface for organizing, searching, and archiving digital documents.

## Features

- Web-based UI for document management
- OCR and full-text search
- Import/export folders
- Persistent configuration and media storage
- Optional Tika and Gotenberg integration for document conversion

## Configuration

### Environment Variables

This stack requires a `.env` file for configuration. A complete and recommended set of variables can be found in the `.env.example` file.

**To get started:**

1. Copy the `.env.example` file to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file and edit the `DOCKER_DATA_BASEFOLDER` variable to match your environment.

## Ports

- `8000` (exposed): Web UI/API (internal, for reverse proxy or internal access)

> **Note:** The stack is intended to be reached through the reverse proxy on `npm_network`.

## Container Images

| Service   | Image                                        |
| --------- | -------------------------------------------- |
| Webserver | `ghcr.io/paperless-ngx/paperless-ngx:latest` |
| Broker    | `docker.io/library/redis:7`                  |
| Gotenberg | `docker.io/gotenberg/gotenberg:8.7`          |
| Tika      | `docker.io/apache/tika:latest`               |

## Usage

1. **Setup Environment Variables**:
   - Copy the `.env.example` to `.env`.
   - Set the `DOCKER_DATA_BASEFOLDER` variable as described above.
2. Deploy the stack:

   ```bash
   docker compose up -d
   ```

3. Access the web interface through Nginx Proxy Manager at `http://paperless-ngx:8000`
4. Import documents by placing them in the `${DOCKER_DATA_BASEFOLDER}/paperless-ngx/consume` folder.
5. Exported documents will appear in the `${DOCKER_DATA_BASEFOLDER}/paperless-ngx/export` folder.

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
