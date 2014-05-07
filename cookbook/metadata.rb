name             'shorewheel'
maintainer       'CirrusMio'
maintainer_email 'todd.willey@cirrusmio.com'
license          'All rights reserved'
description      'Installs/Configures ShoreWheel'
long_description IO.read(File.join(File.dirname(__FILE__), 'README.md'))
version          '0.0.1'

supports 'ubuntu'

depends 'cirrusmio'
depends 'nginx'
depends 'monit'
