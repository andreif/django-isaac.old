# Vagrantfile for developing Django projects.

Vagrant::Config.run do |config|
  config.vm.box = "lucid64"
  # If the above doesn't exist then use the following, I assume almost
  # everyone is running 64 bit now days. It's silly not to.
  config.vm.box_url = "http://files.vagrantup.com/lucid64.box"

  # Since the default for django dev is 8000 stick with that this will
  # change once I get nginx puppet working.
  config.vm.forward_port "http", 8000, 8000

  # Make sure our repos are up to date
  config.vm.provision :shell, :inline => "sudo aptitude update"

  # Run our puppet provsioning.
  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "manifests"
    puppet.manifest_file = "virtualenv.pp"
  end
end

