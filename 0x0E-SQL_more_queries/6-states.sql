-- Create db 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table 'states' in db
-- id INT auto-generated primary key
-- name VARCHAR(256) not null
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
