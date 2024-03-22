# 2-execute_a_command.pp

exec { 'pkill':
  command  => '/usr/bin/pkill -f killmenow',
  path     => ['/usr/bin', '/usr/sbin', '/bin']
}
