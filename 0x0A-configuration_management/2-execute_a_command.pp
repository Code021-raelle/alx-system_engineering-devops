# 2-execute_a_command.pp

exec { 'pkill':
  command  => 'pkill killmenow',
  path     => ['/usr/bin', '/usr/sbin', '/bin']
}
