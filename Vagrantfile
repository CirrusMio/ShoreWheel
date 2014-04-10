# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.synced_folder "./" , "/src/"
  config.vm.synced_folder "./app" , "/src/app"
  config.vm.synced_folder "./db" , "/src/db"
  config.vm.synced_folder "./templates" , "/src/templates"
  config.vm.box = 'opscode-ubuntu-12.04'
  config.vm.box_url = 'https://opscode-vm.s3.amazonaws.com/vagrant/boxes/opscode-ubuntu-12.04.box'
end
