#!/bin/bash

# Get Panose values before setting metadata
before=$(fontforge -script bin/get_panose.py font/OcodoMono-Light.sfd)

# Write metadata to config file
fontforge -script bin/font-metadata.py font/OcodoMono-Light.sfd --write metadata.txt

# Read metadata from config file and set it
fontforge -script bin/font-metadata.py font/OcodoMono-Light.sfd --read metadata.txt

# Get Panose values after setting metadata
after=$(fontforge -script bin/get_panose.py font/OcodoMono-Light.sfd)

# Compare Panose values
echo "Before:"
echo "$before"
echo "After:"
echo "$after"