# Nginx Proxy Manager Extra Configuration for Pi-hole

## Purpose

Ensures `/admin` and `/api` endpoints work correctly when reverse proxying Pi-hole.

## Usage

Add this configuration as an advanced/custom location block in Nginx Proxy Manager for your Pi-hole proxy host.

## Endpoints

- `/` : Redirects to `/admin` (Pi-hole web UI)
- `/admin/` : Proxies requests to Pi-hole admin interface
- `/api/` : Proxies API requests with proper headers

## References

- [Pi-hole Documentation](https://github.com/pi-hole/pi-hole)
- [Nginx Proxy Manager](https://nginxproxymanager.com/)

```nginx
# Redirect root URL to Pi-hole web admin interface
location / {
  rewrite ^/$ /admin permanent;
}

# Proxy Pi-hole admin interface
location /admin/ {
  # Access Control List (ACL): Allow only local/private networks
  allow 192.168.0.0/16;   # Private range (commonly home LAN)
  allow 172.16.0.0/12;    # Private range
  allow 10.0.0.0/8;       # Private range
  allow 100.64.0.0/10;    # Carrier-grade NAT (e.g., Tailscale)
  deny all;               # Deny all other sources
  proxy_pass http://pihole:80/admin/;
}

# Proxy Pi-hole API with required headers
location /api/ {
  proxy_set_header Host $host;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  # Access Control List (ACL): Same as above for security
  allow 192.168.0.0/16;   # Private range (commonly home LAN)
  allow 172.16.0.0/12;    # Private range
  allow 10.0.0.0/8;       # Private range
  allow 100.64.0.0/10;    # Carrier-grade NAT (e.g., Tailscale)
  deny all;               # Deny all other sources
  proxy_pass http://pihole:80/api/;
}

# Custom 403 page
error_page 403 /403.html;
location = /403.html {
    root   /data/nginx/default_www;
    allow all;
}
location = /favicon.png {
    root   /data/nginx/default_www;
    allow all;
}
```
