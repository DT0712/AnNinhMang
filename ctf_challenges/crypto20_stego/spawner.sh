#!/usr/bin/env bash
# spawn.sh <team_id> <flag>
TEAM=$1
FLAG=$2
IMAGE=crypto20_stego:latest
NAME=crypto20_${TEAM}
if [ -z "$TEAM" ] || [ -z "$FLAG" ]; then
  echo "Usage: $0 <team> <flag>"
  exit 2
fi
docker run -d --name ${NAME} \
  --network ctf_net \
  -e FLAG="${FLAG}" \
  --memory=200m --cpus=".25" \
  -p 0:8080 \
  ${IMAGE}
docker port ${NAME} 8080
