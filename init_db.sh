#!/bin/bash

SERVICE_NAME=${1:-db}

SQL_FILE="sql/init.sql"
if [ ! -f "$SQL_FILE" ]; then
  echo "$SQL_FILE not found"
  exit 1
fi

echo "SQL run in $SERVICE_NAME"

docker compose exec -T "$SERVICE_NAME" bash -c "psql
-U \$POSTGRES_USER
-d \$POSTGRES_DB
-f /docker-entrypoint-initdb.d/init.sql"

echo "Run successful"
