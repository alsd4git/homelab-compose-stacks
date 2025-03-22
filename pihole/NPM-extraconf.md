# This is a configuration for Node Proxy Manager
# It is needed for /admin and /api endpoints
# to work properly with Pi-hole

```

location / {
        rewrite ^/$ /admin permanent;
}

location /admin/ {
        proxy_pass http://192.168.0.14:81/admin/ ;
}
location /api/ {
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://192.168.0.14:81/api/;
}
```