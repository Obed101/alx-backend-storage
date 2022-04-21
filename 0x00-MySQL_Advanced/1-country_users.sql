-- Creating a new table
-- This 'users' table contain primary key, unique, etc
-- This file adds a new column - country
CREATE TABLE IF NOT EXISTS users (
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255),
country ENUM('US', 'CO', 'TN') DEFAULT 'US'
)
