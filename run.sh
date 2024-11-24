#!/bin/bash

./configure-dbs.sh
sleep 2
./set-replication-with-main-copy.sh
sleep 2
./set-consolidation-replication.sh
sleep 2
./set-multi-master-replication.sh
sleep 2
./fill-data.sh