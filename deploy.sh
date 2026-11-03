#!/bin/bash
# Pull latest from GitHub and copy the site into the bellenviro.au document root (run by cPanel cron)
REPO=$HOME/repositories/bellenviro-site
DEST=$HOME/public_html/bellenviro.au
cd "$REPO" || exit 1
BEFORE=$(git rev-parse HEAD); git pull -q origin main; [ "$BEFORE" = "$(git rev-parse HEAD)" ] && exit 0
cp -R "$REPO/site/." "$DEST/"
echo "$(date '+%F %T') deployed $(git rev-parse --short HEAD)" >> "$REPO/deploy.log"
