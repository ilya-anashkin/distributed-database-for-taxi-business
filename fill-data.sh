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
    echo "Fill data on $DB_PORT..."
    echo
    python -m helpers.add_records
done
