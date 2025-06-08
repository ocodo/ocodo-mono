#!/bin/bash

FONT_FILE="font/OcodoMono-Light.sfd"
METADATA_FILE="metadata.txt"

# Get initial metadata
fontforge -lang=py -script bin/font-metadata.py "$FONT_FILE" --write "$METADATA_FILE"

# Set metadata from file
fontforge -lang=py -script bin/font-metadata.py "$FONT_FILE" --read "$METADATA_FILE"

# Get metadata again
fontforge -lang=py -script bin/font-metadata.py "$FONT_FILE" --write "${METADATA_FILE}_2"

# Diff metadata files
echo "Metadata diff:"
diff "$METADATA_FILE" "${METADATA_FILE}_2"

# Check diff result
if [ $? -eq 0 ]; then
  echo "Metadata test passed!"
else
  echo "Metadata test failed!"
fi