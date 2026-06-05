#!/bin/bash

read -p "Enter a number: " NUM

if [ $NUM -gt 0 ]
then
	echo "Positive number"
elif [ $NUM -lt 0 ]
then
	echo "Negative number"
else
	echo "Zero"
fi
