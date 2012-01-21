# Vagrantfile for developing Django projects.

Vagrant::Config.run do |config|
  config.vm.box = "lucid64"
  # If the above doesn't exist then use the following, I assume almost
  # everyone is running 64 bit now days. It's silly not to.
  config.vm.box_url = "http://files.vagrantup.com/lucid64.box"

  # Since the default for django dev is 8000 stick with that this will
  # change once I get nginx puppet working.
  config.vm.forward_port "http", 8000, 8000

  # Update package lsits and install all our deps
  tasks = [ "sudo aptitude update",
            "sudo aptitude install -y python-pip git-core",
            "sudo pip install --upgrade pip",
            "sudo aptitude build-dep -y python-psycopg2 python-imaging",
            "cd /vagrant && sudo pip install -r requirements.txt"]

  for task in tasks
    config.vm.provision :shell, :inline => task
  end
end
