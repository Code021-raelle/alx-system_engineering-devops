# How to install and configure Nginx server with Puppet

exec { 'apt_update':
  command => '/usr/bin/apt-get update',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}

# Install Nginx package
package { 'nginx':
  ensure  => installed,
  require => Exec['apt_update'],
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  hasstatus  => true,
  require    => Package['nginx'],
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => file('/templates/nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Modify Nginx default configuration to make it listen on port 80 and return "Hello World!" on root GET request
file { '/etc/nginx/sites-available/default.erb'
  ensure  => file,
  content => "
    server {
        listen 80;
        server_name _;

        location / {
            return 200 'Hello World!';
        }

        location /redirect_me {
            return 301 https://www.example.com;
        }
    }",
}
