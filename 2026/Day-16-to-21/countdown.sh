#!/bin/bash

read -p "Enter a number: " NUM

while [ $NUM -ge 0 ]
do
    echo "Countdown: $NUM"
    NUM=$((NUM-1))
done

echo "Done!"
