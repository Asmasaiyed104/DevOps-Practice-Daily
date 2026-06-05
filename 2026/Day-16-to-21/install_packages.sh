#!/bin/bash

PACKAGES="nginx curl wget"

for pkg in $PACKAGES
do
    if dpkg -s $pkg > /dev/null 2>&1
    then
        echo "$pkg is already installed"

    else
        echo "Installing $pkg..."
        sudo apt install -y $pkg
    fi
done
