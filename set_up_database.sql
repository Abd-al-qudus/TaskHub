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
CREATE table tasks(
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(80) NOT NULL,
    description VARCHAR(500) NOT NULL,
    team_id VARCHAR(80) NOT NULL,
    PRIMARY KEY (id)
);

-- insert some dummy task into the database
INSERT INTO tasks (title, description, team_id) VALUES ("ALX printf project", 
                        "Students are expected to build their printf",
                        "06a0e143-5baa-497c-96ee-f432fc66e7c6");

INSERT INTO tasks (title, description, team_id) VALUES ("ALX shell project", 
                        "Students are expected to build their simple shell",
                        "06a0e143-5baa-497c-96ee-f432fc66e7d4");