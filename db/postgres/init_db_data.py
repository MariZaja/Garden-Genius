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
        (name, latin_name, description, flowers, cycle, maintenance, leaf_color, growth_rate, fruit, type, depth_water_requirement, volume_water_requirement, watering_period, watering_general_benchmark, wymiary, poisonous, default_image, plant_type, sunlight, edible_parts)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            vegetable["Name"],
            vegetable["Latin_name"],
            vegetable["Description"],
            vegetable["Flowers"],
            vegetable["Cycle"],
            vegetable["Maintenance"],
            vegetable["Leaf_color"],
            vegetable["Growth_rate"],
            vegetable["Fruit"],
            vegetable["Type"],
            vegetable["Depth_water_requirement"],
            vegetable["Volume_water_requirement"],
            vegetable["Watering_period"],
            vegetable["Watering_general_benchmark"],
            vegetable["Wymiary"],
            vegetable["Poisonous"],
            vegetable["Default_image"],
            vegetable["Plant_type"],
            vegetable["Sunlight"],
            vegetable["Edible_parts"]
        )
    )

# Commit the transaction
conn.commit()

# Close the connection
cur.close()
conn.close()
