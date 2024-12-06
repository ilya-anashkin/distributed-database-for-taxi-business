#!/bin/bash

# Common
export DB_USERNAME=postgres
export DB_PASSWORD=postgres
export DB_NAME=postgres
export DB_HOST=localhost

# Create tables with schemas
for DB_PORT in 5432 5433 5434; do
    export DB_PORT
    echo
    echo "Create table on $DB_PORT..."
    echo
    python3 -m helpers.create_tables
done

max_number_of_replicas=20
max_wal_senders=10
max_logical_replication_workers=10

databases=("pg_master" "pg_replica_1" "pg_replica_2")
for db in "${databases[@]}"; do
    echo
    echo "Configuring PostgreSQL instance $db for logical replication..."
    docker exec -i "$db" bash -c "sed -i 's/^#*wal_level .*$/wal_level = logical/' /var/lib/postgresql/data/postgresql.conf"
    docker exec -i "$db" bash -c "sed -i 's/^#*max_replication_slots .*$/max_replication_slots = $max_number_of_replicas/' /var/lib/postgresql/data/postgresql.conf"
    docker exec -i "$db" bash -c "sed -i 's/^#*max_wal_senders .*$/max_wal_senders = $max_wal_senders/' /var/lib/postgresql/data/postgresql.conf"
    docker exec -i "$db" bash -c "sed -i 's/^#*max_logical_replication_workers .*$/max_logical_replication_workers = $max_logical_replication_workers/' /var/lib/postgresql/data/postgresql.conf"
    docker exec -i "$db" bash -c "grep -qxF 'host replication all all md5' /var/lib/postgresql/data/pg_hba.conf || echo 'host replication all all md5' >> /var/lib/postgresql/data/pg_hba.conf"

    echo "Restarting PostgreSQL instance $db to apply configuration changes..."
    echo
    docker restart "$db"
done