#!/bin/bash
echo "moving webiste to sites-available..."
sudo a2ensite testsite
echo "**********************************************************************"
echo "restarting server..."
sudo service apache2 restart
echo "website deployed"
echo "**********************************************************************"
echo "lauching error log for tracking. Ctrl-C to resume..."
sudo tail -f /var/log/apache2/error.log -n 40
