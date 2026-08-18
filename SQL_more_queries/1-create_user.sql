-- Creates the MySQL server user user_0d_1 with all privileges
-- Creates the user only if it does not exist yet, so the script never fails
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grants every privilege on every database of the server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
