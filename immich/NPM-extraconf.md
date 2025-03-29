# This is a configuration for Node Proxy Manager

```nginx

# Allow large file uploads
client_max_body_size 50000M;

# Proxy headers
proxy_set_header Host              $http_host;
proxy_set_header X-Real-IP         $remote_addr;
proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;

# Timeouts for large/slow uploads
proxy_read_timeout 600s;
proxy_send_timeout 600s;
send_timeout       600s;

# Disable buffering (faster large uploads)
proxy_buffering off;

# mTLS - client certificate auth (if exposed)
# ssl_client_certificate /etc/nginx/ssl/homelab/root_ca.crt;
# ssl_verify_client on;

# Security headers (browser hardening)
add_header X-Content-Type-Options nosniff;
add_header X-Frame-Options DENY;
add_header X-XSS-Protection "1; mode=block";
add_header Referrer-Policy "no-referrer";
add_header Content-Security-Policy "frame-ancestors 'none';";

```
