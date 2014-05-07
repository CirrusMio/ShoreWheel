#
# Cookbook Name:: shorewheel
# Recipe:: nginx
#
# Copyright (C) 2014 CirrusMio
#
# All rights reserved - Do Not Redistribute
#

include_recipe 'nginx'

cookbook_file 'nginx config' do 
  source 'nginx-config'
  path '/etc/nginx/sites-available/shorewheel'
  owner 'root'
  group 'root'
  mode 0755
  action :create
end

nginx_site 'shorewheel' do
  enable true
end

nginx_site 'default' do
  enable false
end
