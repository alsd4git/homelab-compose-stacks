# Utilities Stack

File management, document processing, and utility services for your homelab. This stack provides tools for file browsing, document conversion, and format transformation.

## Included Tools

### 1. ConvertX

- **Purpose**: A versatile file conversion tool.
- **Features**: Supports batch processing, authentication, and auto-cleanup of converted files.

### 2. CUP (Container Update Puller)

- **Purpose**: A tool for managing Docker container updates.
- **Features**: Monitors for new container images and provides update notifications.

### 3. FileBrowser Quantum

- **Purpose**: A web-based file manager.
- **Features**: Allows you to browse, manage, and share files and folders.

### 4. Stirling PDF

- **Purpose**: A powerful tool for PDF manipulation.
- **Features**: Supports a wide range of operations, including merging, splitting, and converting PDFs.

### 5. Telegram Files

- **Purpose**: A file management tool for Telegram.
- **Features**: Helps organize and manage files stored in your Telegram account.

### 6. UpSnap

- **Purpose**: A network device monitoring tool.
- **Features**: Discovers devices on your network, monitors their status, and supports Wake-on-LAN.

## Configuration

### Environment Variables

This stack requires a `.env` file for configuration. A complete and recommended set of variables can be found in the `.env.example` file.

**To get started:**

1. Copy the `.env.example` file to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file and edit the variables to match your environment.

**Key variables include:**

- `DOCKER_DATA_BASEFOLDER`: The absolute path for storing persistent data.
- `DOCKER_MEDIA_BASEFOLDER`: The absolute path for media files.
- `TELEGRAM_API_ID` & `TELEGRAM_API_HASH`: Optional credentials for Telegram Files.
- `FILEBROWSER_ADMIN_PASSWORD`: An optional admin password for FileBrowser Quantum.

## Services & Ports

| Service                 | Internal Port | Access Pattern              | Description                               |
| ----------------------- | ------------- | --------------------------- | ----------------------------------------- |
| **ConvertX**            | `3000`        | `http://convertx:3000`      | File conversion service.                  |
| **CUP**                 | `8000`        | `http://cup:8000`           | Container update management.              |
| **FileBrowser Quantum** | `80`          | `http://filebrowser-quantum:80` | Web-based file management.             |
| **Stirling PDF**        | `8080`        | `http://stirling-pdf:8080`  | PDF processing and manipulation.          |
| **Telegram Files**      | `80`          | `http://telegram-files:80`  | Telegram file management.                 |
| **UpSnap**              | `5001`        | `http://<host-ip>:5001`     | Network device monitoring (host network). |

> **Note:** The services on `npm_network` are intended to be reached through Nginx Proxy Manager. Only the host-network service keeps a direct host endpoint.

## Container Images

| Service             | Image                                    |
| ------------------- | ---------------------------------------- |
| ConvertX            | `ghcr.io/c4illin/convertx`               |
| CUP                 | `ghcr.io/sergi0g/cup:latest`             |
| FileBrowser Quantum | `gtstef/filebrowser`                     |
| Stirling PDF        | `stirlingtools/stirling-pdf:latest`      |
| Telegram Files      | `ghcr.io/jarvis2f/telegram-files:latest` |
| UpSnap              | `ghcr.io/seriousm4x/upsnap:latest`       |

## Usage

1. **Setup Environment Variables**:
   - Copy the `.env.example` to `.env`.
   - Set the required environment variables as described above.

2. **Start the Stack**:

   ```bash
   docker compose up -d
   ```

3. **Access Services**:
   - Access ConvertX at `http://localhost:3003`
   - Access CUP at `http://localhost:8004`
   - Access FileBrowser Quantum at `http://localhost:8087`
   - Access Stirling PDF at `http://localhost:8082`
   - Access Telegram Files at `http://localhost:6543`
   - Access UpSnap at `http://localhost:5001`

## Security Considerations

**⚠️ Docker Socket Access**:

- The **CUP** service mounts `/var/run/docker.sock`, which grants full access to the Docker daemon. This is necessary for its function but is a significant security risk. Only run this stack in a trusted network environment.

**⚠️ Host Network Mode**:

- **UpSnap** uses `network_mode: host`, which exposes it directly on the host's network interface.

## Additional Resources

- [ConvertX Documentation](https://github.com/c4illin/convertx)
- [CUP Documentation](https://github.com/sergi0g/cup)
- [FileBrowser Documentation](https://filebrowser.org/)
- [Stirling PDF Documentation](https://github.com/Stirling-Tools/Stirling-PDF)
- [Telegram Files Documentation](https://github.com/jarvis2f/telegram-files)
- [UpSnap Documentation](https://github.com/seriousm4x/upsnap)
