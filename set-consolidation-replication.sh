#!/bin/bash

master_db="pg_master"
replicas=("pg_replica_1" "pg_replica_2")

for replica in "${replicas[@]}"; do
    echo "Create consolidation publication for $replica"
    docker exec -i "$replica" psql -U postgres -d postgres -c "DROP PUBLICATION IF EXISTS ${replica}_consolidation_publication;"
    docker exec -i "$replica" psql -U postgres -d postgres -c "CREATE PUBLICATION ${replica}_consolidation_publication FOR TABLE car_rents, rides;"

    echo "Create subscription on ${replica}_consolidation_publication for $master_db"
    docker exec -i "$master_db" psql -U postgres -d postgres -c "DROP SUBSCRIPTION IF EXISTS ${replica}_consolidation_subscription;"
    docker exec -i "$master_db" psql -U postgres -d postgres -c "CREATE SUBSCRIPTION ${replica}_consolidation_subscription CONNECTION 'dbname=postgres host=$replica user=postgres password=postgres' PUBLICATION ${replica}_consolidation_publication;"
done
