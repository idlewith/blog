# nginx


## combine proxy and static file


vi /etc/nginx/nginx.conf

```bash
http {
...
upstream idlepig {
    server 127.0.0.1:8081;
  }
...
}
```

vi /etc/nginx/conf.d/default.conf

```bash
server {
    listen 80;
    server_name _;
    location / {
        root /www/server/nginx/html;
        try_files $uri $uri/ @apachesite;
    }

location @apachesite {
    proxy_pass http://idlepig;
    }
}
```

simple version

```bash
server {
    listen 80;
    server_name _;
    location / {
        proxy_pass http://idlepig;
    }  
}
```