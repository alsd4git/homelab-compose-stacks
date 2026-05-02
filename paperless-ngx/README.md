# Paperless-ngx Stack

A document management system with a web interface for organizing, searching, and archiving digital documents.

## Features

- **Web UI**: document management in the browser.
- **OCR and search**: full-text indexing and OCR.
- **Import/export folders**: simple document ingestion and export.
- **Document conversion**: optional Tika and Gotenberg support.
- **Persistent storage**: data, media, consume, and export directories.

## Configuration

### Environment Variables

This stack requires a `.env` file for configuration. A complete and recommended set of variables can be found in the `.env.example` file.

**To get started:**

1. Copy the `.env.example` file to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file and edit the `DOCKER_DATA_BASEFOLDER` variable to match your environment.

## Services & Ports

| Service | Internal Port | Access Pattern | Notes |
| --- | --- | --- | --- |
| Paperless-ngx | `8000` | `http://paperless-ngx:8000` | Web UI/API on `npm_network`. |
| Redis broker | internal only | internal only | Queue and caching backend. |
| Gotenberg | internal only | internal only | Conversion backend. |
| Tika | internal only | internal only | OCR and text extraction backend. |

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

3. Publish the web interface through Nginx Proxy Manager using the host you assign for Paperless-ngx.
4. Import documents by placing them in the `${DOCKER_DATA_BASEFOLDER}/paperless-ngx/consume` folder.
5. Exported documents will appear in the `${DOCKER_DATA_BASEFOLDER}/paperless-ngx/export` folder.

## Security Notes

- Change the default admin credentials.
- Keep the web UI behind a reverse proxy or VPN.
- Keep Paperless-ngx updated.
- Monitor logs for unusual activity.

## Troubleshooting

- Check logs: `docker logs paperless-ngx`
- Port conflicts: Ensure no other services use the same ports
- Import/export issues: Verify volume permissions and free space

## Additional Resources

- [Paperless-ngx Documentation](https://docs.paperless-ngx.com/)
- [Gotenberg Documentation](https://gotenberg.dev/)
- [Tika Documentation](https://tika.apache.org/)
