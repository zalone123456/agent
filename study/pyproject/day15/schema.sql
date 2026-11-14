CREATE DATABASE learning_db;
use learning_db
CREATE TABLE study_records(
 id INT PRIMARY KEY AUTO_INCREMENT,
 topic VARCHAR(100) not NULL,
 study_minutes INT not NULL,
 study_date  DATE not NULL,
 notes 	VARCHAR(255)

);