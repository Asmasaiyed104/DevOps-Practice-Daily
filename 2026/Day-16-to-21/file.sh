#!/bin/bash

read -p "Enter filename: " FILE

if [ -f "$FILE" ]
then
	echo "File exist"
else
	echo " File does not exist"
fi
