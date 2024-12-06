#!/bin/bash

master="pg_master"
replica1="pg_replica_1"
replica2="pg_replica_2"

docker exec -i "$master" psql -U postgres -d postgres -c "DROP PUBLICATION IF EXISTS ${master}_multi_publication;"
docker exec -i "$master" psql -U postgres -d postgres -c "CREATE PUBLICATION ${master}_multi_publication FOR TABLE drivers, clients, drivers_states, unsatisfactory_rides;"
docker exec -i "$replica1" psql -U postgres -d postgres -c "DROP SUBSCRIPTION IF EXISTS ${replica1}_${master}_multi_subscription;"
docker exec -i "$replica1" psql -U postgres -d postgres -c "CREATE SUBSCRIPTION ${replica1}_${master}_multi_subscription CONNECTION 'dbname=postgres host=$master user=postgres password=postgres' PUBLICATION ${master}_multi_publication;"
docker exec -i "$replica2" psql -U postgres -d postgres -c "DROP SUBSCRIPTION IF EXISTS ${replica2}_${master}_multi_subscription;"
docker exec -i "$replica2" psql -U postgres -d postgres -c "CREATE SUBSCRIPTION ${replica2}_${master}_multi_subscription CONNECTION 'dbname=postgres host=$master user=postgres password=postgres' PUBLICATION ${master}_multi_publication;"

docker exec -i "$replica1" psql -U postgres -d postgres -c "DROP PUBLICATION IF EXISTS ${replica1}_multi_publication;"
docker exec -i "$replica1" psql -U postgres -d postgres -c "CREATE PUBLICATION ${replica1}_multi_publication FOR TABLE drivers, clients, drivers_states, unsatisfactory_rides;"
docker exec -i "$master" psql -U postgres -d postgres -c "DROP SUBSCRIPTION IF EXISTS ${master}_${replica1}_multi_subscription;"
docker exec -i "$master" psql -U postgres -d postgres -c "CREATE SUBSCRIPTION ${master}_${replica1}_multi_subscription CONNECTION 'dbname=postgres host=$replica1 user=postgres password=postgres' PUBLICATION ${replica1}_multi_publication;"
docker exec -i "$replica2" psql -U postgres -d postgres -c "DROP SUBSCRIPTION IF EXISTS ${replica2}_${replica1}_multi_subscription;"
docker exec -i "$replica2" psql -U postgres -d postgres -c "CREATE SUBSCRIPTION ${replica2}_${replica1}_multi_subscription CONNECTION 'dbname=postgres host=$replica1 user=postgres password=postgres' PUBLICATION ${replica1}_multi_publication;"

docker exec -i "$replica2" psql -U postgres -d postgres -c "DROP PUBLICATION IF EXISTS ${replica2}_multi_publication;"
docker exec -i "$replica2" psql -U postgres -d postgres -c "CREATE PUBLICATION ${replica2}_multi_publication FOR TABLE drivers, clients, drivers_states, unsatisfactory_rides;"
docker exec -i "$master" psql -U postgres -d postgres -c "DROP SUBSCRIPTION IF EXISTS ${master}_${replica2}_multi_subscription;"
docker exec -i "$master" psql -U postgres -d postgres -c "CREATE SUBSCRIPTION ${master}_${replica2}_multi_subscription CONNECTION 'dbname=postgres host=$replica2 user=postgres password=postgres' PUBLICATION ${replica2}_multi_publication;"
docker exec -i "$replica1" psql -U postgres -d postgres -c "DROP SUBSCRIPTION IF EXISTS ${replica1}_${replica2}_multi_subscription;"
docker exec -i "$replica1" psql -U postgres -d postgres -c "CREATE SUBSCRIPTION ${replica1}_${replica2}_multi_subscription CONNECTION 'dbname=postgres host=$replica2 user=postgres password=postgres' PUBLICATION ${replica2}_multi_publication;"
