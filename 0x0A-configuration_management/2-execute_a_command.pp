# 2-execute_a_command.pp

exec { 'pkill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
