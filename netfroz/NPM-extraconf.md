# This is a configuration for Node Proxy Manager (advanced tab)

```nginx

# Root location
location / {
  # Pass the request to the app
  proxy_pass          $forward_scheme://$server:$port;

  # Add other app specific config here

  # Tinyauth auth request
  auth_request /tinyauth;
  error_page 401 = @tinyauth_login;
}

# Tinyauth auth request
location /tinyauth {
  # Pass request to Tinyauth
  proxy_pass http://tinyauth:3000/api/auth/nginx;

  # Pass the request headers
  proxy_set_header x-forwarded-proto $scheme;
  proxy_set_header x-forwarded-host $http_host;
  proxy_set_header x-forwarded-uri $request_uri;
}

# Tinyauth login redirect
location @tinyauth_login {
  return 302 http://tinyauth.alsd.duckdns.org/login?redirect_uri=$scheme://$http_host$request_uri; # Make sure to replace the http://tinyauth.example.com with your own app URL
}

```
