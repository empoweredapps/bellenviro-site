#!/bin/bash
# Pull latest from GitHub and copy the site into the bellenviro.au document root (run by cPanel cron)
export PATH=/usr/local/bin:/usr/bin:/bin:$PATH
REPO=$HOME/repositories/bellenviro-site
DEST=$HOME/public_html/bellenviro.au
LOG=$REPO/deploy.log
cd "$REPO" || { echo "$(date '+%F %T') ERROR cannot cd $REPO" >> "$LOG"; exit 1; }
BEFORE=$(git rev-parse HEAD)
git pull -q origin main 2>> "$LOG" || { echo "$(date '+%F %T') ERROR git pull failed" >> "$LOG"; exit 1; }
[ "$BEFORE" = "$(git rev-parse HEAD)" ] && exit 0
cp -R "$REPO/site/." "$DEST/"
echo "$(date '+%F %T') deployed $(git rev-parse --short HEAD)" >> "$LOG"
