#!/bin/bash

long_version=$(grep "version =" "$1" | awk '{print $3}' | cut -d ';' -f 1)
short_version=$(grep "version =" "$1" | awk '{print $3}' | cut -d ';' -f 2 | grep -oP 'v\K[0-9]+\.[0-9]+')

major=$(echo "$short_version" | cut -d '.' -f 1)
minor=$(echo "$short_version" | cut -d '.' -f 2)

((minor++))

new_short_version="$major.$minor"
new_long_version="$major.$minor"0
new_version_line="version = $new_long_version;info.ocodo.fonts.ocodomono.v$new_short_version"

sed -i "s|^version = .*|$new_version_line|" "$1"
sed -i "s|^version-string = .*|version-string = $new_long_version;info.ocodo.fonts.ocodomono.v$new_short_version|" "$1"

echo "Version updated to $new_short_version ($new_long_version)"