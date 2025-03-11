#!/bin/bash
set -e # Exit on error

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <container_name> <db_user> <db_name>"
    exit 1
fi

CONTAINER_NAME=$1
DB_USER=$2
DB_NAME=$3
#SQL_SCRIPTS_DIR="$(dirname "$0")/../sql/tables"
SQL_SCRIPTS_DIR="$(realpath "$(dirname "$0")/../sql/create")"  # Auto-detect directory
SQL_FILES=(
    "init_timescale.sql"
    "create_exchange_table.sql"
    "create_data_vendor_table.sql"
    "create_sec_symbol_table.sql"
    "create_sec_minute_price_table.sql"
    "create_sec_daily_price_table.sql"
)

for SQL_FILE in "${SQL_FILES[@]}"; do
    echo "Creating table from $SQL_FILE..."
    docker exec -i $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME < $SQL_SCRIPTS_DIR/$SQL_FILE
    if [ $? -ne 0 ]; then
        echo "❌ Error occurred while executing $SQL_FILE. Exiting."
        exit 1
    fi
    echo "✅ $SQL_FILE executed successfully."
done

echo "All operations completed successfully"