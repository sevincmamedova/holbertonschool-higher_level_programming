-- Creates the table force_name, whose name field can never be null
-- Creates the table only if it does not exist yet, so the script never fails
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
