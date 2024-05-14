# This Puppet manifest configures Nginx to handle high concurrency loads.

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx server
file { '/etc/nginx/nginx.conf':
  ensure  => 'file',
  content => "
    # Nginx configuration here
    # Example:
    worker_processes auto;
    events {
      worker_connections 1000;
    }
    http {
      include mime.types;
      default_type application/octet-stream;

      sendfile on;
      keepalive_timeout 65;

      server {
        listen 80;
        server_name localhost;

        location / {
          root /path/to/your/web/root;
          index index.html;
          keepalive_requests 100;
        }
      }
    }
  ",
  notify => Service['nginx'],
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/nginx.conf'],
}
