-- Creates the database hbtn_0d_usa and the table states inside it
-- Creates the database only if it does not exist yet
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Selects the database the table has to be created in
USE hbtn_0d_usa;
-- Creates the table only if it does not exist yet, so the script never fails
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
