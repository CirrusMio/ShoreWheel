#
# Cookbook Name:: shorewheel
# Recipe:: run
#
# Copyright (C) 2014 CirrusMio
#
# All rights reserved - Do Not Redistribute
#

# bash 'start' do
#   cwd '/home/ubuntu/shorewheel'
#   code <<-EOH
#   foreman start
#   EOH
# end

bash 'seed-project' do
  cwd '/home/ubuntu/shorewheel'
  code <<-EOH
  make seed
  EOH
end

define :run do
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
