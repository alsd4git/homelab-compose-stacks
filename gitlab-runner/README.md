# GitLab Runner Stack

Self-hosted GitLab Runner configured to use the host Docker daemon for Docker-executor jobs.

## Features

- **Docker executor ready**: job containers are created through the host Docker daemon.
- **No inbound ports**: the runner connects outbound to GitLab, so no reverse proxy or port forwarding is required.
- **Persistent configuration**: runner registration data and `config.toml` live under the configured data root.
- **Pinned runner image**: the default image is version-pinned so upgrades remain deliberate.

## Configuration

### Environment Variables

Copy the example file to `.env`:

```bash
cp .env.example .env
```

Key variables:

- `DOCKER_DATA_BASEFOLDER`: base path for persistent Docker data.
- `GITLAB_RUNNER_IMAGE`: runner image/tag to deploy.
- `TZ`: container timezone.

The generated GitLab Runner configuration is stored at:

```text
${DOCKER_DATA_BASEFOLDER}/gitlab-runner/config.toml
```

Do not commit this file: it contains runner authentication data.

## Usage

1. Create the persistent data directory:

   ```bash
   mkdir -p ${DOCKER_DATA_BASEFOLDER}/gitlab-runner
   ```

2. Start the stack:

   ```bash
   docker compose up -d
   ```

3. In GitLab, create a project or group runner and copy the runner authentication token (`glrt-...`).

4. Register the runner from the running container:

   ```bash
   docker compose exec gitlab-runner gitlab-runner register
   ```

5. When prompted, use:

   - GitLab URL: `https://gitlab.com/` for GitLab.com
   - Token: the `glrt-...` authentication token created in GitLab
   - Executor: `docker`
   - Default Docker image: for example `debian:stable-slim`

6. Verify the registration:

   ```bash
   docker compose exec gitlab-runner gitlab-runner verify
   ```

GitLab writes the resulting runner configuration into the persistent `config.toml` file. Further executor settings, such as concurrency, pull policy, resource limits, and the default image, can be adjusted there.

## Portainer

This stack can be deployed from Portainer like the other stacks in this repository. The runner does not publish any ports; it only requires outbound access to GitLab and access to the host Docker socket.

Registration is still a one-time operation after the first deployment. In Portainer, open the `gitlab-runner` container console and run:

```bash
gitlab-runner register
```

## Security Notes

- Mounting `/var/run/docker.sock` gives the runner container high-level control over the host Docker daemon.
- Use this runner only for repositories and pipelines you trust.
- Keep the Docker executor non-privileged unless a workflow has a specific, reviewed requirement for privileged containers.
- Do not add `/var/run/docker.sock` to the job container volumes in `config.toml` unless jobs explicitly need host Docker access.
- Be cautious with untrusted merge requests or pipelines from forks, especially on a machine that also hosts unrelated services.

## Updating

The image is pinned by default. To upgrade, change `GITLAB_RUNNER_IMAGE` in your local `.env`, review the GitLab Runner release notes, then redeploy the stack.

## Additional Resources

- [Install GitLab Runner in a container](https://docs.gitlab.com/runner/install/docker/)
- [Docker executor](https://docs.gitlab.com/runner/executors/docker/)
- [Runner security](https://docs.gitlab.com/runner/security/)
- [Registering runners](https://docs.gitlab.com/runner/register/)
