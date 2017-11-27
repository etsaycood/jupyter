#! /bin/bash
IDID=$1
MESSAGE=$2-$3-$4-$5
IPLIST=$(python ip.py $2)
TIME=$(date '+%D %T')
