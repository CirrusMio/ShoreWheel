#
# Cookbook Name:: shorewheel
# Recipe:: run
#
# Copyright (C) 2014 CirrusMio
#
# All rights reserved - Do Not Redistribute
#

bash 'start' do
  cwd '/home/ubuntu/shorewheel'
  code <<-EOH
  foreman start
  EOH
end

bash 'seed-project' do
  cwd '/home/ubuntu/shorewheel'
  code <<-EOH
  make seed
  EOH
end
