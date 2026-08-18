-- Creates the table unique_id, whose id field defaults to 1 and is unique
-- Creates the table only if it does not exist yet, so the script never fails
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
