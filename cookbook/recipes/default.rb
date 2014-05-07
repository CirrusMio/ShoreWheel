#
# Cookbook Name:: shorewheel
# Recipe:: default
#
# Copyright (C) 2014 CirrusMio
#
# All rights reserved - Do Not Redistribute
#

package 'python-setuptools' do
  action :install
end

package 'python-dev' do
  action :install
end

%w{flask flask-sqlalchemy gunicorn psycopg2}.each do |p|
  easy_install_package p do
    action :install
  end
end

gem_package "foreman" do
  action :install
end

bash 'make-project' do
  cwd node['shorewheel']['deploy_path']
  code <<-EOH
  make clean
  make
  EOH
end
