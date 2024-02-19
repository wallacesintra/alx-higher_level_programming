-- create a database(hbtn_0d_usa)
-- create a table(states)
-- declare an id and name for the table

CREATE IF NOT EXISTS DATABASE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
)
