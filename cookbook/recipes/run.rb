#
# Cookbook Name:: shorewheel
# Recipe:: run
#
# Copyright (C) 2014 CirrusMio
#
# All rights reserved - Do Not Redistribute
#

include_recipe 'monit'

bash 'seed-project' do
  cwd '/home/ubuntu/shorewheel'
  code <<-EOH
  make seed
  EOH
end

app_name = params[:name]

cookbook_file 'gunicorn config' do
  source 'gunicorn-config'
  path '/home/ubuntu/shorewheel/gunicorn.config'
  owner 'root'
  group 'root'
  mode 0755
  action :create
end

cookbook_file 'gunicorn init' do
  source 'gunicorn-init'
  path '/etc/init.d/shorewheel-gunicorn'
  owner 'root'
  group 'root'
  mode 0755
  action :create
end

service "shorewheel-gunicorn" do
  init_command "/etc/init.d/shorewheel-gunicorn"
  supports restart: true, reload: true
  action :enable
end

service "shorewheel-gunicorn" do
  supports restart: true, reload: true
  action :start
end

monitrc "shorewheel-monit" do
  template_cookbook 'shorewheel'
  template_source 'gunicorn-monit.erb'
  variables({
    app_name: node['shorewheel']['app_name'],
    deploy_path: node['shorewheel']['deploy_path'],
    user: 'root',
    group: 'root'
  })
end
