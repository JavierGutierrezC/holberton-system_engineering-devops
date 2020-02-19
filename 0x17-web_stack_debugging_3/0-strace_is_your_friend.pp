# change a error in php
exec { 'replace a line':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}
