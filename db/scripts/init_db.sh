#!/bin/bash

# Function to check if PostgreSQL is running
wait_for_postgres() {
  until psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q' 2>/dev/null; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
  done
}

# Function to escape single quotes for SQL
escape_string() {
  echo "$1" | sed "s/'/''/g"
}

# Function to insert data into the species table
insert_species_data() {
  local categories=("vegetables" "herbs")
  
  for category in "${categories[@]}"; do
    cat "$JSON_FILE" | jq -c ".${category}[]" | while read -r item; do
      local Name=$(escape_string "$(echo "$item" | jq -r '.Name')")
      local Description=$(escape_string "$(echo "$item" | jq -r '.Description')")
      local Maintenance=$(escape_string "$(echo "$item" | jq -r '.Maintenance')")
      local Watering_period=$(escape_string "$(echo "$item" | jq -r '.Watering_period')")
      local Size=$(escape_string "$(echo "$item" | jq -r '.Size')")
      local Poisonous=$(escape_string "$(echo "$item" | jq -r '.Poisonous')")
      local Default_image=$(escape_string "$(echo "$item" | jq -r '.Default_image')")
      local Sunlight=$(escape_string "$(echo "$item" | jq -r '.Sunlight')")
      local Edible_parts=$(escape_string "$(echo "$item" | jq -r '.Edible_parts')")

      # Insert the data into the PostgreSQL database
      psql -U gardenGenius -d gardenGeniusDb -c "
        INSERT INTO species (name, description, maintenance, watering_period, size, poisonous, default_image, sunlight, edible_parts)
        VALUES ('$Name', '$Description', '$Maintenance', '$Watering_period', '$Size', '$Poisonous', '$Default_image', '$Sunlight', '$Edible_parts');
      "
    done
  done
}

# Function to insert data into the users table
insert_users_data() {
  cat "$JSON_FILE" | jq -c '.users[]' | while read -r user; do
    local Username=$(escape_string "$(echo "$user" | jq -r '.Username')")
    local Password=$(escape_string "$(echo "$user" | jq -r '.Password')")
    local Email=$(escape_string "$(echo "$user" | jq -r '.Email')")

    # Insert the data into the PostgreSQL database
    psql -U gardenGenius -d gardenGeniusDb -c "
      INSERT INTO users (username, password, email)
      VALUES ('$Username', '$Password', '$Email');
    "
  done
}

# Main script execution
JSON_FILE="/docker-entrypoint-initdb.d/data.json"

# Wait for PostgreSQL to start
wait_for_postgres

# Insert species data (vegetables and herbs)
insert_species_data

# Insert users data
insert_users_data
