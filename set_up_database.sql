-- Creates database taskhub_db
CREATE DATABASE IF NOT EXISTS taskhub_db;
USE taskhub_db;
CREATE USER IF NOT EXISTS 'taskhub_user'@'localhost';
SET PASSWORD FOR 'taskhub_user'@'localhost' = 'taskhub_user_pwd';
GRANT ALL PRIVILEGES ON taskhub_db.* TO 'taskhub_user'@'localhost';
GRANT SELECT ON performance_schema.* TO 'taskhub_user'@'localhost';
FLUSH PRIVILEGES;

-- Create a dummy task table for display
USE taskhub_db;
CREATE table task(
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(80) NOT NULL,
    description VARCHAR(500) NOT NULL,
    team_name VARCHAR(80) NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE table user(
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(80) NOT NULL,
    password_hash VARCHAR(120) NOT NULL,
    PRIMARY KEY(id)
);

CREATE table team_member(
    id NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    task_id INT,
    team_name VARCHAR(120) NOT NULL,
    task_name VARCHAR(120) NOT NULL,
    FOREIGN KEY (task_id) REFERENCES task(task_id)
)

-- insert some dummy task into the database