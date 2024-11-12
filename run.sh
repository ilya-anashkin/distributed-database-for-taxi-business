#!/bin/bash

./configure-dbs.sh
sleep 2
./set-primary-replica-replication.sh
sleep 2
./set-consolidation-replication.sh
sleep 2
./set-multi-master-replication