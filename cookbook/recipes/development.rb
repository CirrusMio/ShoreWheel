#
# Cookbook Name:: shorewheel
# Recipe:: development
#
# Copyright (C) 2014 CirrusMio
#
# All rights reserved - Do Not Redistribute
#

database_attr = node['shorewheel']['database']

bash 'seed-project' do
  cwd '/home/ubuntu/shorewheel'
  code <<-EOH
  make seed
  EOH
end

template '/home/ubuntu/shorewheel/app/app.py' do
  source 'app.py.erb'
  mode 0644
  variables({
    name: database_attr['name'],
    username: database_attr['username'],
    password: database_attr['password'],
    host: database_attr['host']
  })
  action :create
end
