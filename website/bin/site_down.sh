#!/bin/bash
echo "**********************************************************************"
echo "moving default apache config to sites-available..."
sudo a2ensite 000-default default-ssl
echo "**********************************************************************"
echo "disabling webiste sites..."
sudo a2dissite website
echo "**********************************************************************"
echo "restarting server..."
sudo service apache2 restart
echo "site down config deployed"
