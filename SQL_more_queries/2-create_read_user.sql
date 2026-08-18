-- Creates the database hbtn_0d_2 and the read only user user_0d_2
-- Creates the database only if it does not exist yet
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates the user only if it does not exist yet, so the script never fails
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grants the SELECT privilege on the hbtn_0d_2 database only
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
