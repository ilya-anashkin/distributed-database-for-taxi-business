#!/bin/bash

echo "All PostgreSQL instances configured successfully for logical replication."

# Define the master database and the replicas
master_db="pg_master"
replicas=("pg_replica_1" "pg_replica_2")

# Configure the master database
echo "Configuring $master_db as master..."
docker exec -i "$master_db" psql -U postgres -d postgres -c "DROP PUBLICATION IF EXISTS publication_with_main_copy;"
docker exec -i "$master_db" psql -U postgres -d postgres -c "CREATE PUBLICATION publication_with_main_copy FOR TABLE regions, taxi_pools, car_colors, car_models, car_models_rbi, car_classes, cars, employment_statuses, drivers_statuses;"

# Configure each replica to follow the master
for replica in "${replicas[@]}"; do
    echo
    echo "Configuring $replica to replicate from $master_db..."

    # Construct the connection string
    conninfo="host=$master_db port=5432 user=postgres password=postgres dbname=postgres"

    # Configure the subscription on the replica
    docker exec -i "$replica" psql -U postgres -d postgres -c "DROP SUBSCRIPTION IF EXISTS ${replica}_subscription;"
    docker exec -i "$replica" psql -U postgres -d postgres -c "CREATE SUBSCRIPTION ${replica}_subscription CONNECTION 'dbname=postgres host=$master_db user=postgres password=postgres' PUBLICATION publication_with_main_copy;"

    echo "$replica configured to replicate from $master_db."
    echo
done

echo "Master and replicas configured successfully for logical replication."