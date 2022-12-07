#!/bin/bash

# https://unix.stackexchange.com/questions/56189/appending-timestamp-stamp-along-with-log-file-lines

# set -x

# LOG_DATE=$(date +"%Y-%m-%d_%H%M%S ")

LOGFILE=log_kc_top_$(date +"%Y-%m-%d_%H%M%S").log

while true; do 
  K_TOP_CMD=$(kubectl get pods -n kc -o=jsonpath='{range .items[*]}{"kubectl top pod --no-headers=true -n "}{.metadata.namespace}{" "}{.metadata.name}{" ;"}{end}')
  bash -c "$K_TOP_CMD" | grep -v "NAME.*CPU(cores)" | sed -e "s/^/$(date +"%Y-%m-%d_%H%M%S") /" | tee -a $LOGFILE
  sleep 1
done