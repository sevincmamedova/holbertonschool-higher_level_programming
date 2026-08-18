-- Creates the database hbtn_0d_usa and the table cities inside it
-- Creates the database only if it does not exist yet
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Selects the database the table has to be created in
USE hbtn_0d_usa;
-- Creates the table only if it does not exist yet, so the script never fails
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
