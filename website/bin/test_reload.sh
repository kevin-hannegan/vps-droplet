#!/bin/bash
echo "**********************************************************************"
echo "copying apache configuration to sites-avialable..."
sudo cp /home/khannegan/website/apache2/testsite.conf /etc/apache2/sites-available/testsite.conf
echo "**********************************************************************"
echo "enabling test configuration..."
sudo a2ensite testsite
echo "**********************************************************************"
echo "restarting server..."
sudo service apache2 restart
if ! pidof apache2
then 
    echo "ERROR: apache2 server restart FAILED!!!"
else
    echo "website deployed"
fi
echo "**********************************************************************"
echo "lauching error log for tracking. Ctrl-C to resume..."
sudo tail -f /var/log/apache2/error.log -n 40
