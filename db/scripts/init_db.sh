#!/bin/bash

# Wait for PostgreSQL to start
until psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

# Path to the JSON file
JSON_FILE="/docker-entrypoint-initdb.d/data.json"

# Loop through each vegetable entry in the JSON array
cat "$JSON_FILE" | jq -c '.vegetables[]' | while read vegetable; do
    Name=$(echo "$vegetable" | jq -r '.Name')
    Description=$(echo "$vegetable" | jq -r '.Description')
    Maintenance=$(echo "$vegetable" | jq -r '.Maintenance')
    Watering_period=$(echo "$vegetable" | jq -r '.Watering_period')
    Size=$(echo "$vegetable" | jq -r '.Size')
    Poisonous=$(echo "$vegetable" | jq -r '.Poisonous')
    Default_image=$(echo "$vegetable" | jq -r '.Default_image')
    Sunlight=$(echo "$vegetable" | jq -r '.Sunlight')
    Edible_parts=$(echo "$vegetable" | jq -r '.Edible_parts')

    # Insert the vegetable data into the PostgreSQL database
    psql -U gardenGenius -d gardenGeniusDb -c "
        INSERT INTO species (name, description, maintenance, watering_period, size, poisonous, default_image, sunlight, edible_parts)
        VALUES ('$Name', '$Description', '$Maintenance', '$Watering_period', '$Size', '$Poisonous', '$Default_image', '$Sunlight', '$Edible_parts');
    "
done

# Loop through each herb entry in the JSON array
cat "$JSON_FILE" | jq -c '.herbs[]' | while read herbs; do
    Name=$(echo "$herbs" | jq -r '.Name')
    Description=$(echo "$herbs" | jq -r '.Description')
    Maintenance=$(echo "$herbs" | jq -r '.Maintenance')
    Watering_period=$(echo "$herbs" | jq -r '.Watering_period')
    Size=$(echo "$herbs" | jq -r '.Size')
    Poisonous=$(echo "$herbs" | jq -r '.Poisonous')
    Default_image=$(echo "$herbs" | jq -r '.Default_image')
    Sunlight=$(echo "$herbs" | jq -r '.Sunlight')
    Edible_parts=$(echo "$herbs" | jq -r '.Edible_parts')

    # Insert the herbs data into the PostgreSQL database
    psql -U gardenGenius -d gardenGeniusDb -c "
        INSERT INTO species (name, description, maintenance, watering_period, size, poisonous, default_image, sunlight, edible_parts)
        VALUES ('$Name', '$Description', '$Maintenance', '$Watering_period', '$Size', '$Poisonous', '$Default_image', '$Sunlight', '$Edible_parts');
    "
done

# Loop through each users entry in the JSON array
cat "$JSON_FILE" | jq -c '.users[]' | while read users; do
    Username=$(echo "$users" | jq -r '.Username')
    Password=$(echo "$users" | jq -r '.Password')
    Email=$(echo "$users" | jq -r '.Email')
    
    # Insert the users data into the PostgreSQL database
    psql -U gardenGenius -d gardenGeniusDb -c "
        INSERT INTO users (username, password, email)
        VALUES ('$Username', '$Password', '$Email');
    "
done
