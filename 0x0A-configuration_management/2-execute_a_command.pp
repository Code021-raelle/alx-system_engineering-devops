# 2-execute_a_command.pp

exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
  onlyif  => 'pgrep -f killmenow',
}
