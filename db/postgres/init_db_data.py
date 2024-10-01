import psycopg2
import json

# Load data from a JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="gardenGeniusDb",
    user="gardenGenius",
    password="pass123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insert data into the table
for vegetable in data["vegetables"]:
    cur.execute(
        """
        INSERT INTO vegetables 
        (name, description, maintenance, watering_period, size, poisonous, default_image, sunlight, edible_parts)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            vegetable["Name"],
            vegetable["Description"],
            vegetable["Maintenance"],
            vegetable["Watering_period"],
            vegetable["Size"],
            vegetable["Poisonous"],
            vegetable["Default_image"],
            vegetable["Sunlight"],
            vegetable["Edible_parts"]
        )
    )

# Commit the transaction
conn.commit()

# Close the connection
cur.close()
conn.close()
