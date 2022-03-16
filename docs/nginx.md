# nginx



## https: 443


### nginx config for 443


### cert

cd /www/server/panel/vhost/cert

sudo certbot --nginx certonly

sudo certbot renew --dry-run

```
server {
        server_name domain.com www.domain.com;
        listen 443 ssl;
        ssl on;
        ssl_certificate     /etc/letsencrypt/live/domain.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem;
        root /var/www/html;
        location / {
                proxy_pass http://127.0.0.1:3001;
                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
        }
location /ws {
proxy_buffering off;
      proxy_set_header Host $host;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  proxy_set_header X-Real-IP $remote_addr;
proxy_pass http://127.0.0.1:3001/ws;
                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
        }
}
```


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