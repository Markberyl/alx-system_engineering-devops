# Define package resource for Flask installation
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Refresh the package list after installation
exec { 'update_package_list':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin:/usr/sbin:/bin',
  require => Package['flask'],
}

