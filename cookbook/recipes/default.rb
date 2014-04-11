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
