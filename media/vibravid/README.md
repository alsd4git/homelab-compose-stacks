# VibraVid policy

VibraVid is a manual, targeted fallback for titles unavailable through the
normal Arr/indexer path. It shares the same `/media` tree as Sonarr and Radarr,
and both Arr clients may be configured for metadata/import support while ARR
polling and webhooks remain deliberately disabled: adding an unrelated title
cannot cause an automatic download.

Its web UI is published only through Nginx Proxy Manager, using the same
LAN/Tailscale-or-TinyAuth policy as AW Downloader. Set `VIBRAVID_PUBLIC_HOST`
in the ignored deployment environment; Compose derives the allowed host and
CSRF trusted origin from it. There is no direct host-port binding.

Do not mount the Docker socket. The upstream one-click updater would otherwise
grant the application control over the host Docker daemon.

When using a provider for a specific title, tag that title in Sonarr or Radarr
as `provider-<site>` (for example `provider-animeunity`). Enable the ARR
integration only after separately reviewing the provider, source legality,
webhook secret, and an explicit scope for polling. AW Downloader remains the
dedicated AnimeWorld integration; its experimental Radarr support is not
enabled, so the two tools cannot compete for the same missing movies.

## First safe test

1. Open the UI through the proxy host and confirm that TinyAuth/LAN access
   works.
2. Review configuration and run a title search only; do not start a download.
3. For the first download, use a disposable title and a dedicated temporary
   output mapping before enabling any Arr integration.
