#!/bin/bash

FONT_FILE="font/OcodoMono-Thin.sfd"
METADATA_FILE="ocodo-mono-thin.conf"

# Get initial metadata
fontforge -lang=py -script bin/font-metadata.py "$FONT_FILE" --read "$METADATA_FILE"