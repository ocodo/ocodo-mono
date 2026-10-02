#!/usr/bin/env bash
set -euo pipefail

REPO="ocodo/ocodo-mono"

rm -rf package
mkdir -p package/fonts

echo "Downloading latest GitHub release..."
gh release download \
  --repo "$REPO" --clobber \
  --pattern 'OcodoMono-*ttf' \
  --pattern 'OcodoMono-*woff2' \
  --dir package/fonts

echo "Preparing package..."
cp README.md package/
cp dotzero.package.json package/package.json
cp dotzero.font.css package/font.css

echo "Node: $(node --version)"
echo "npm:  $(npm --version)"

echo "Publishing..."
(
  cd package
  npm publish --access public
)

