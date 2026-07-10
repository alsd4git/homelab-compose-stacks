# Forgejo Stack

Git hosting for personal repositories, with a rootless Forgejo server and a Postgres backend.

## Features

- **Web UI**: repository browsing, pull requests, issues, and package registry.
- **Rootless runtime**: Forgejo runs as `1000:1000` and stores data under dedicated bind mounts.
- **Postgres backend**: persistent database separated from the application container.
- **Reverse-proxy friendly**: the web service joins `npm_network` for Nginx Proxy Manager.
- **SSH git access**: embedded Forgejo SSH server published on host port `2222`.

## Configuration

### Environment Variables

Copy the example file to `.env`, then set the domain and database secret:

```bash
cp .env.example .env
```

Key variables:

- `YOUR_DOMAIN`
- `FORGEJO_VERSION`
- `POSTGRES_VERSION`
- `FORGEJO_DB_NAME`
- `FORGEJO_DB_USER`
- `FORGEJO_DB_PASSWORD`
- `FORGEJO_DISABLE_REGISTRATION`
- `FORGEJO_REQUIRE_SIGNIN_VIEW`
- `FORGEJO_SSH_PORT`
- `FORGEJO_ALLOWED_USER_VISIBILITY_MODES`
- `FORGEJO_DEFAULT_USER_VISIBILITY`
- `FORGEJO_DEFAULT_ORG_VISIBILITY`
- `FORGEJO_FORCE_PRIVATE`
- `FORGEJO_DEFAULT_PRIVATE`
- `FORGEJO_DEFAULT_PUSH_CREATE_PRIVATE`
- `FORGEJO_ENABLE_PUSH_CREATE_USER`
- `FORGEJO_ENABLE_PUSH_CREATE_ORG`
- `FORGEJO_DISABLE_REGULAR_ORG_CREATION`

For a homelab-first setup, the stack defaults to a private posture: registration is disabled, sign-in is required to view pages, user and organization visibility default to private, push-to-create is enabled, and new repositories are private by default.

### Storage

| Path or Volume | Purpose |
| --- | --- |
| `${DOCKER_DATA_BASEFOLDER}/forgejo/data` | Forgejo repositories, attachments, actions data, and LFS. |
| `forgejo_postgres_data` | Postgres database data. |

## Services & Ports

| Service | Internal Port | Access Pattern | Notes |
| --- | --- | --- | --- |
| Forgejo | `3000` | `https://forgejo.${YOUR_DOMAIN}` | Web UI published through Nginx Proxy Manager. |
| Forgejo SSH | `2222` | `ssh://git@forgejo.${YOUR_DOMAIN}:2222` | SSH clone endpoint published on the host. |
| Postgres | `5432` | internal only | Database stays on the private `forgejo_network`. |

## Container Images

| Service | Image |
| --- | --- |
| Forgejo | `codeberg.org/forgejo/forgejo:${FORGEJO_VERSION:-15-rootless}` |
| Postgres | `postgres:${POSTGRES_VERSION:-17-alpine}` |

## Usage

1. Copy `.env.example` to `.env`.
2. Create the data directories:

   ```bash
   mkdir -p ${DOCKER_DATA_BASEFOLDER:-/opt/docker/data}/forgejo/data
   ```

   If the directories already exist, make sure they are writable by UID/GID `1000:1000`.

3. Start the stack:

   ```bash
   docker compose up -d
   ```

4. Open the web UI through Nginx Proxy Manager and complete the initial onboarding.
5. Create the first user during onboarding; that account becomes the initial admin.

With the current defaults, anonymous users cannot view anything and new repositories are created private unless you explicitly change the policy later.

## Nginx Proxy Manager Notes

- Use the reverse-proxy host `forgejo.${YOUR_DOMAIN}` for the web UI.
- Apply the upload-safe NPM snippet in [`forgejo/NPM-extraconf.conf`](./NPM-extraconf.conf) so pushes and archive uploads are not blocked by the default request size.
- Keep the SSH port published on `2222`; NPM only handles the HTTP(S) side.
- Use the `git` host if you want a brand-neutral URL; `forgejo` remains available as a second hostname, both protected by the same local-only access list.

## Security Notes

- Keep `FORGEJO_DB_PASSWORD` in `.env` and do not commit it.
- Leave registration disabled unless you explicitly want public signups.
- Keep `FORGEJO__service__REQUIRE_SIGNIN_VIEW=true` if you want the site invisible to anonymous visitors.
- Keep `FORGEJO____DEFAULT_USER_VISIBILITY=private`, `FORGEJO____DEFAULT_ORG_VISIBILITY=private`, and `FORGEJO____ALLOWED_USER_VISIBILITY_MODES=private` to avoid accidentally exposing profiles or organizations later.
- Keep `FORGEJO__repository__FORCE_PRIVATE=true` and `FORGEJO__repository__DEFAULT_PUSH_CREATE_PRIVATE=true` to avoid accidental public repositories.
- Use the SSH endpoint only if you need SSH clones; otherwise the web UI is enough.
- The Postgres database is private on `forgejo_network` and has no published host port.

## Additional Resources

- [Forgejo Installation with Docker](https://forgejo.org/docs/next/admin/installation/docker/)
- [Forgejo Reverse Proxy Guide](https://forgejo.org/docs/latest/admin/reverse-proxy/)
- [Forgejo Configuration Cheat Sheet](https://forgejo.org/docs/latest/admin/config-cheat-sheet/)
- [Forgejo API Usage](https://forgejo.org/docs/v10.0/user/api-usage/)
