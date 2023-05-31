-- Creates database taskhub_db
CREATE DATABASE IF NOT EXISTS taskhub_db;
USE taskhub_db;
CREATE USER IF NOT EXISTS 'taskhub_user'@'localhost';
SET PASSWORD FOR 'taskhub_user'@'localhost' = 'taskhub_user_pwd';
GRANT ALL PRIVILEGES ON taskhub_db.* TO 'taskhub_user'@'localhost';
GRANT SELECT ON performance_schema.* TO 'taskhub_user'@'localhost';
FLUSH PRIVILEGES;
