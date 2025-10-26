#!/usr/bin/env bash
set -e
docker-compose down --remove-orphans
docker-compose build --no-cache
docker-compose up -d
# wait for service to come up
sleep 3
echo "Reset complete. Run tests with ./tests/web30_test.sh"
