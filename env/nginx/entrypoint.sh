#!/bin/sh

cp /deploy/apps/lawyer_business/env/nginx/default /etc/nginx/sites-enabled/default

exec nginx -g 'daemon off;' "$@"
