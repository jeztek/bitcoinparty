#!/usr/bin/env bash

# This script auto-restarts bfgminer if it dies while running
# Set the USER variable to the payout bitcoin wallet

USER=""

while true
do
    if pidof -s bfgminer > /dev/null; then
	echo "bfgminer is running..."
                sleep 2
		else
	echo "About to restart bfgminer, CTRL+C to cancel"
	sleep 2
	bfgminer --url http://stratum.mining.eligius.st:3334 --user $USER --pass 1
fi  
done
