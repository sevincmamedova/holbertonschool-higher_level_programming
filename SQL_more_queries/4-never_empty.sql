-- Creates the table id_not_null, whose id field defaults to 1
-- Creates the table only if it does not exist yet, so the script never fails
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
