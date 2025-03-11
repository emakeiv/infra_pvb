#!/bin/bash

# Ensure script stops if any command fails
set -e

# Validate input arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <container_name> <db_user> <db_name>"
    exit 1
fi

# Define variables
CONTAINER_NAME="$1"
DB_USER="$2"
DB_NAME="$3"
SQL_SCRIPTS_DIR="$(realpath "$(dirname "$0")/../sql/drop")"  # Auto-detect directory

# List of SQL files to execute in order
SQL_FILES=(
    "drop_security_daily_price_table.sqll"
    "drop_security_minute_price_table.sql"
    "drop_security_symbol_table.sql"
    "drop_data_vendor_table.sql"
    "drop_exchange_table.sql"
    "drop_timescale.sql"
)

# Check if SQL scripts directory exists
if [ ! -d "$SQL_SCRIPTS_DIR" ]; then
    echo "Error: SQL scripts directory '$SQL_SCRIPTS_DIR' does not exist."
    exit 1
fi

# Iterate over each SQL file and execute in TimescaleDB container
for SQL_FILE in "${SQL_FILES[@]}"; do
    FILE_PATH="$SQL_SCRIPTS_DIR/$SQL_FILE"

    if [ ! -f "$FILE_PATH" ]; then
        echo "Warning: $SQL_FILE not found. Skipping..."
        continue
    fi

    echo "Dropping: $SQL_FILE..."
    docker exec -i "$CONTAINER_NAME" psql -U "$DB_USER" -d "$DB_NAME" < "$FILE_PATH"

    if [ $? -ne 0 ]; then
        echo "❌ Error occurred while executing $SQL_FILE. Exiting."
        exit 1
    fi

    echo "✅ $SQL_FILE executed successfully."
done

echo "All tables dropped successfully."
