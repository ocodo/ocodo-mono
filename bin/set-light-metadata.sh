#!/bin/bash

FONT_FILE="font/OcodoMono-Light.sfd"
METADATA_FILE="ocodo-mono-light.conf"

# Get initial metadata
fontforge -lang=py -script bin/font-metadata.py "$FONT_FILE" --read "$METADATA_FILE"