#!/bin/bash
echo "**********************************************************************"
echo "copying apache configuration to sites-avialable..."
sudo cp /home/khannegan/apps/website/apache2/website.conf /etc/apache2/sites-available/website.conf
echo "**********************************************************************"
echo "disabling defualt configuration..."
sudo a2dissite 000-default default-ssl
echo "**********************************************************************"
echo "moving webiste to sites-available..."
sudo a2ensite website
echo "**********************************************************************"
echo "restarting server..."
sudo service apache2 restart
echo "website deployed"
echo "**********************************************************************"
echo "lauching error log for tracking. Ctrl-C to resume..."
sudo tail -f /var/log/apache2/error.log -n 40
