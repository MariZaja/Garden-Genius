CREATE TABLE vegetables (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    latin_name VARCHAR(255),
    description TEXT,
    flowers VARCHAR(255),
    cycle VARCHAR(80),  -- Increased to fit 67 characters
    maintenance TEXT,
    leaf_color VARCHAR(100),
    growth_rate VARCHAR(80),  -- Increased to fit 80 characters
    fruit VARCHAR(255),
    type VARCHAR(100),
    depth_water_requirement VARCHAR(80),  -- Increased to fit 80 characters
    volume_water_requirement VARCHAR(100),
    watering_period VARCHAR(100),
    watering_general_benchmark TEXT,
    wymiary VARCHAR(100),
    poisonous BOOLEAN,
    default_image TEXT,
    plant_type VARCHAR(100),
    sunlight VARCHAR(255),
    edible_parts VARCHAR(255)
);
