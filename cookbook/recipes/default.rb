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

%w{flask flask-sqlalchemy gunicorn}.each do |p|
  easy_install_package p do
    action :install
  end
end

gem_package "foreman" do
  action :install
end

bash 'make-project' do
  cwd '/home/ubuntu/shorewheel'
  code <<-EOH
  make
  EOH
end
