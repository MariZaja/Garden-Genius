CREATE TABLE species (
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

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE gardens (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    creation_date DATE,
    surrounding VARCHAR(255)
);


CREATE TABLE plants (
    id SERIAL PRIMARY KEY,
    species_id INTEGER REFERENCES species(id) ON DELETE SET NULL,
    garden_id INTEGER REFERENCES gardens(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    notes TEXT
);


