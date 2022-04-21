-- Creating a new table
-- This 'users' table contain primary key, unique, etc
CREATE TABLE IF NOT EXISTS users (
id INT NOT NULL AUTO_INCREMENT,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255),
PRIMARY KEY (id)
)
