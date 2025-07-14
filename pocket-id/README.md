# Pocket ID

Pocket ID is a simple, self-hosted OpenID Connect (OIDC) provider that allows users to authenticate with their passkeys to your services. It's a lightweight alternative to more complex identity providers like Keycloak or Authentik.

## Features

-   **Passkey-based Authentication**: Passwordless authentication using FIDO2/WebAuthn standards (passkeys).
-   **OpenID Connect Provider**: Standard OIDC interface to integrate with your services.
-   **Lightweight and Simple**: Designed to be easy to set up and manage for simple use cases.
-   **Self-Hosted**: Full control over your identity data.

## Configuration

1.  **Environment Variables**: Create a `.env` file in the `pocket-id` directory by copying the `.env.example` file:
    ```bash
    cp .env.example .env
    ```
    Then, edit the `.env` file and set the following variables:
    -   `APP_URL`: The public URL of your Pocket ID instance (e.g., `https://pocketid.yourdomain.com`).
    -   `TRUST_PROXY`: Set to `true` if you are running Pocket ID behind a reverse proxy.
    -   `PUID`/`PGID`: User and group ID for file permissions. Defaults to `1000`.

2.  **Docker Compose**: The `compose.yaml` file is configured to use the environment variables from the `.env` file.

## Usage

1.  **Start the stack**:
    ```bash
    docker compose up -d
    ```
2.  **Initial Setup**: Navigate to `http://<your-server-ip>:1411` (or the URL you configured with your reverse proxy) to perform the initial setup and create an admin account.
3.  **Reverse Proxy**: It is recommended to run Pocket ID behind a reverse proxy like Nginx Proxy Manager. An example configuration snippet for NPM is provided in `NPM-extraconf.md`.

## Security Notes

-   The service is exposed on port `1411`. It is recommended to not expose this port directly to the internet, but rather use a reverse proxy with SSL enabled.
-   Ensure you have a strong passkey for your admin account.

## Troubleshooting

-   **File Permissions**: If you encounter permission issues with the data volume, ensure the `PUID` and `PGID` in your `.env` file match the user and group that own the docker data directory on your host.

## Additional Resources

-   [Official Pocket ID GitHub Repository](https://github.com/pocket-id/pocket-id)
-   [Official Pocket ID Documentation](https://pocket-id.org/docs/) 