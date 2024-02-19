-- create database(hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create table(cities) in db
-- description: 
-- id INT auto-generated primary key, 
-- state_id INT not null,
-- name VARCHAR(256) not null
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
