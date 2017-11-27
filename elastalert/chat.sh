#! /bin/bash
IDID=$1
MESSAGE=$2-$3-$4-$5
IPLIST=$(python ip.py $2)
TIME=$(date '+%D %T')

curl -H "Content-Type: application/x-www-form-urlencoded" -X POST -d "&Receivers=[$IDID]&Content=$MESSAGE$IPLIST&LocalTime=$TIME" http://SendMsgRequest
