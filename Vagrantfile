# vi: set ft=ruby :

Vagrant.configure('2') do |config|
  config.vm.define('shorewheel') do |cm|
    cm.vm.hostname = 'shorewheel'
    cm.vm.box = 'saucy-virtualbox-sysruby'
    cm.vm.box_url = 'http://boxes.cirrusmio.com/ubuntu/' +
                         'saucy-virtualbox-sysruby.box'

    cm.vm.provider 'virtualbox' do |v|
      v.customize ['modifyvm', :id, '--memory', 512]
      v.customize ['modifyvm', :id, '--name', 'shorewheel']
    end

    cm.vm.network :forwarded_port, guest: 80, host: 8080
    cm.vm.synced_folder './', '/home/ubuntu/shorewheel'

    cm.ssh.forward_agent = true
    cm.ssh.username = 'ubuntu'

    cm.berkshelf.enbaled = true
    cm.vm.provision :chef_solo do |chef|
      chef.log_level = :debug
      chef.roles_path = '../cirrusmio-chef/roles'
      chef.run_list = [
                        'role[base]',
                        'recipe[cirrusmio::postgres]',
                        'recipe[cirrusmio::sysruby]',
                        'recipe[shorewheel::default]',
                        'recipe[shorewheel::development]',
                        'recipe[shorewheel::run]',
                        'recipe[shorewheel::nginx]'
                      ]
      chef.json = {
        shorewheel: {
          database: {
            name: 'shorewheel_development',
            host: 'localhost',
            username: 'shorewheel',
            password: 'shorewheel'
          }
        },
        postgresql: {
          version: '9.3',
          password: {postgres: 'password'},
          pg_hba: [{type: 'host', db: 'all',
                    user: 'postgres', addr: '127.0.0.1/32',
                    method: 'trust'},
                   {type: 'local', db: 'all',
                    user: 'postgres', addr: nil,
                    method: 'trust'},
                   {type: 'host', db: 'all',
                    user: 'shorewheel', addr: '127.0.0.1/32',
                    method: 'password'},
                   {type: 'local', db: 'all',
                    user: 'shorewheel', addr: nil,
                    method: 'password'}]
        },
        postgresql_databases: {
          shorewheel_development: {
            users: {shorewheel: 'shorewheel'},
            owner: 'shorewheel',
            postgis: true
          },
          shorewheel_test: {
            users: {shorewheel: 'shorewheel'},
            owner: 'shorewheel',
            postgis: true
          }
        }
      }
    end
  end
end
