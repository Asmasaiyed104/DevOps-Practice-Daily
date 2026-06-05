#!/bin/bash

SERVICE="ssh"

read -p "Do you want to check the service status? (y/n): " CHOICE

if [ "$CHOICE" = "y" ]
then
    systemctl is-active $SERVICE

else
    echo "Skipped"
fi
