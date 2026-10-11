#!/usr/bin/env bash
# Deploy de site naar Vercel.
#
# Eerste keer:
#   - npx vercel --yes        → login via browser-flow + nieuw project aanmaken
#   - bevestigt vercel.json (cleanUrls + redirects)
# Volgende keren:
#   - npx vercel --prod       → push naar productie
set -e

cd "$(dirname "$0")"

echo "==> Deploy naar Vercel"
echo "    Bestandsmap: $(pwd)"
echo

if [ ! -d ".vercel" ]; then
  echo "==> Eerste deploy — link de map aan een Vercel-project"
  npx vercel --yes
  echo
  echo "==> Eerste preview-deploy gemaakt."
  echo "    Run nu nogmaals voor productie:  ./deploy.sh"
else
  echo "==> Push naar productie"
  npx vercel --prod
fi
