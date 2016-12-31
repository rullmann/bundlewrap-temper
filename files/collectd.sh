#!/bin/bash

HOSTNAME="${COLLECTD_HOSTNAME:-localhost}"
INTERVAL="${COLLECTD_INTERVAL:-10}"

while sleep "$INTERVAL"; do
  echo "PUTVAL \"$HOSTNAME/temper/temperature-temper\" interval=$INTERVAL N:$(/opt/usb-thermometer/pcsensor -n)"
done
