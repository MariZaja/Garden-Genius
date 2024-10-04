CREATE TABLE vegetables (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    maintenance TEXT,
    watering_period VARCHAR(100),
    size VARCHAR(100),
    poisonous BOOLEAN,
    default_image TEXT,
    sunlight VARCHAR(255),
    edible_parts VARCHAR(255)
);
