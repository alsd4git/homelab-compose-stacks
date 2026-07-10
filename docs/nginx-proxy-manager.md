# Nginx Proxy Manager Policy

This repository keeps NPM advanced config short, purpose-driven, and stack-local.

## General rules

- Keep `ssl_forced`, `http2_support`, `hsts_enabled`, `hsts_subdomains`, and `allow_websocket_upgrade` enabled on normal web UIs.
- Keep `block_exploits` enabled everywhere except `tinyauth`.
- Keep `caching_enabled` off by default so dynamic dashboards and admin UIs stay fresh.
- Shared bridge networks are declared with `external: true` in consumer stacks only. In this repository `npm_network` is a pre-created shared bridge network referenced from every stack, while `pihole_network` is created by the Pi-hole stack and consumed by `media` for DNS attribution.

## Port exposure

Docker `ports` bindings listen on all host interfaces unless the host address is
specified. NPM access lists protect proxied hosts only; they do not restrict a
published host port. Enforce this intended exposure with the host firewall and
router rules:

- Internet-facing only when deliberately forwarded: NPM `80`/`443`, torrent peer
  port `6881`, and Forgejo SSH `2222`.
- LAN or VPN only: NPM admin `83`, Step CA `9001`, Home Assistant `8123`,
  WatchYourLAN `8840`, and Pi-hole DNS `53`.
- All other web UIs: keep them un-published and reach them through NPM on
  `npm_network`.

## Canonical LAN / Tailscale allow-list

Use the same allow-list whenever a host should remain reachable from the home LAN and Tailscale:

```nginx
allow 192.168.0.0/16;
allow 172.16.0.0/12;
allow 10.0.0.0/8;
allow 100.64.0.0/10;
deny all;
```

## Common advanced patterns

- `auth_request /tinyauth` plus `satisfy any` for LAN-or-auth access. Use `X-Forwarded-Host $host` in NPM so Tinyauth matches the real request host.
- Large uploads: increase `client_max_body_size`, `proxy_read_timeout`, and disable buffering.
- Redirect or deny-only hosts: keep the block minimal and document the intent in the stack README.

## Upload-heavy services

Use this block for web UIs that need large uploads or long-running requests:

```nginx
client_max_body_size 50000M;

proxy_set_header Host              $http_host;
proxy_set_header X-Real-IP         $remote_addr;
proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;

proxy_read_timeout 600s;
proxy_send_timeout 600s;
send_timeout       600s;
proxy_request_buffering off;
proxy_buffering off;
```

Good fits in this repository:

- `filebrowser-quantum`
- `convertx`
- `forgejo`

## Where the snippets live

- [`media/NPM-extraconf.conf`](../media/NPM-extraconf.conf) contains the TinyAuth-gated LAN template used for `animedl` and `homepage`.
- [`forgejo/NPM-extraconf.conf`](../forgejo/NPM-extraconf.conf) raises the upload limit for Git pushes and archives.
- [`immich/NPM-extraconf.md`](../immich/NPM-extraconf.md) covers large uploads and long-running media requests.
- [`pihole/NPM-extraconf.md`](../pihole/NPM-extraconf.md) contains the Pi-hole reverse-proxy template with the same LAN/Tailscale allow-list.
