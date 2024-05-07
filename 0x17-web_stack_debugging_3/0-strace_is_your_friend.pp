# Strace is your friend
exec { 'wordpress typo error':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/usr/bin:/usr/sbin:/bin',
}
