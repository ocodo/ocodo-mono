#!/bin/bash

long_version=$(grep "version =" "$1" | awk '{print $3}' | cut -d ';' -f 1)
short_version=$(grep "version =" "$1" | awk '{print $3}' | cut -d ';' -f 2 | grep -oP 'v\K[0-9]+\.[0-9]+')

if [ -n "$long_version" ] && [ -n "$short_version" ]; then
  echo "Long version: $long_version"
  echo "Short version: $short_version"
else
  echo "No version information found"
fi