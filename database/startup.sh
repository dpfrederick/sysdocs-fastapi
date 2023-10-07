#!/bin/bash
set -e

export PGUSER="$POSTGRES_USER"

echo "creating sysdocz database"
"${psql[@]}" --dbname="$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE sysdocz;
EOSQL

echo "running sql init files"
echo "creating tables..."
"${psql[@]}" --dbname="sysdocz" -f /sqlscripts/create_tables.sql

echo "tables in sysdocz -->"
"${psql[@]}" --dbname="sysdocz" <<-EOSQL 
    \dt; 
EOSQL

echo "seeding data..."
"${psql[@]}" --dbname="sysdocz" -f /sqlscripts/seed.sql

echo "creating sysdocz user..."
"${psql[@]}" --dbname="sysdocz" -f /sqlscripts/create_users.sql

# this will enable logging to a file instead of stdout

# echo "enable logging..."
# "${psql[@]}" --dbname="vectordb" -c "ALTER SYSTEM SET logging_collector = 'on';"
# "${psql[@]}" --dbname="vectordb" -c "ALTER SYSTEM SET log_destination = 'stderr';"
# "${psql[@]}" --dbname="vectordb" -c "ALTER SYSTEM SET log_directory = '/var/log/postgresql';"
# "${psql[@]}" --dbname="vectordb" -c "SELECT pg_reload_conf();"
