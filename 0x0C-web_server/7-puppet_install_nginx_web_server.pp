# Install and configure Nginx server with puppet

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Modify Nginx default configuration to make it listen on port 80 and return "Hello World!" on root GET request
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  replace => true,
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
            try_files $uri $uri/ =404;
            echo 'Hello World!';
        }

        location /redirect_me {
            return 301 https://www.example.com/new-page;
        }
    }
  ",
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
