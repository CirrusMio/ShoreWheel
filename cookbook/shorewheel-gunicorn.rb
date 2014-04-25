#
# Cookbook Name:: shorewheel
# Definition:: cirrusmio_postgres
#
# Copyright 2014, CirrusMio
# All rights reserved - Do Not Redistribute
#

define :shorewheel_gunicorn do
  app_name = params[:name]

  template ::File.join('/etc/init.d/', "#{app_name}-gunicorn") do
    source 'gunicorn-init.erb'
    owner 'root'
    group 'root'
    mode 0755
    variables({
      deploy_path: params[:deploy_path],
      environment: params[:environment]
    })
    action :create
  end

  service "#{app_name}-gunicorn" do
    init_command "/etc/init.d/#{app_name}-gunicorn"
    supports restart: true, reload: true
    action :enable
  end
end