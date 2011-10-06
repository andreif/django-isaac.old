# All current settings are for initial development only. These settings will
# change to a more production like environment as we go.

Vagrant::Config.run do |config|
  config.vm.box = "lucid"
  # If the above doesn't exist then:
  config.vm.box_url = "http://files.vagrantup.com/lucid64.box"

  # Since the default for django dev is 8000 stick with that.
  config.vm.forward_port "http", 8000, 8000

  # Installs required packages for using virtualenv.
  config.vm.provision :shell, :inline => "sudo aptitude -y install python-virtualenv && sudo aptitude -y build-dep psycopg2"
end
