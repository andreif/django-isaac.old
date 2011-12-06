class virtualenv {
  # python packages
  # virtualenv not used in vagrant, only in production due to performance issues
  package { "python-virtualenv": ensure => present }

  # build deps for python-psycopg2
  package { "autoconf": ensure => present }
  package { "debhelper": ensure => present }
  package { "libpq-dev": ensure => present }
  package { "python-all-dbg": ensure => present }
  package { "python-all-dev": ensure => present }
  package { "python-egenix-mx-base-dev": ensure => present }
}


include virtualenv
