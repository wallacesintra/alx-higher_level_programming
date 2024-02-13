# SQL
**SQL** - Structured Query Language

## **Database**
a structured collection of data

**Relational Database**
It is a database that organizes data into tables with rows & columns, where each row represents a record and each column represents a specific attribute or field of that record.

**xtics of relational databases**
1. tables - each table representing a specific entity.
2. Rows and Columns - rows rep individual instances of data, columns rep attributes of those instances.
3. Keys - they establish relationships between tables. Primary keys uniquely identify each record within a table, while foreign keys establish relationships between tables by referencing the primary key of another table.
4. Normalization - designed to minimize redundancy &  improve data intergrity.
5. ACID properties - (Atomicity, Consistency, Isolation, Durability) 


## MySQL
MySQL is an open-source relational database management system (RDBMS) that is widely used for managing and manipulating structured data.

**create a database in MySQL**
1. Open the MySQL Command-Line Client
   ` mysql -u username -p`
2. create a new database
    `CREATE DATABASE database_name;`
3. verify that the database has been created
    `SHOW DATABASES;`

**DML** 
Data Definition Language - deals with the definition of database structure and schema.
Common DDL commands include CREATE, ALTER, and DROP.

**DML**
Data Manipulation Language - deals with the manipulation of data stored in the database.
Common DML commands include INSERT, UPDATE, DELETE, and SELECT.


**Creating Table**
`CREATE TABLE table_name (
    column1 datatype [constraints],
    column2 datatype [constraints],
    ...
);`

`CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);`

**Altering Table**
You can use ALTER TABLE to add a new column to an existing table.

`ALTER TABLE table_name
ADD column_name datatype [constraints];`

`ALTER TABLE users
ADD age INT;`

**selecting data from a table**

`SELECT column1, column2, ...
FROM table_name;`

`-- Selecting specific columns
SELECT username, email
FROM users;`

*select all*
`SELECT *
FROM table_name`;

`-- Selecting all columns
SELECT *
FROM users;`

*WHERE* - Used to filter rows based on specified conditions

`SELECT * 
FROM users 
WHERE age > 25;`

*ORDER BY* - Used to sort the result set based on one or more columns.

`SELECT * 
FROM users 
ORDER BY username ASC;`

query selects all columns from the users table and orders the result set in ascending order based on the username column.

*GROUP BY* - Used to group rows that have the same values into summary rows.

`SELECT department, COUNT(*) as num_employees
FROM employees
GROUP BY department;`

*HAVING* - Used to filter group rows that have specified conditions.

`SELECT department, COUNT(*) as num_employees
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;`

*JOIN* - Used to combine rows from two or more tables based on a related column between them.

`SELECT orders.order_id, customers.customer_name
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;`


**insert into a table**

`INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);`

`INSERT INTO users (username, email, age)
VALUES ('john_doe', 'john@example.com', 30);`


**update existing records**

`UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;`

`UPDATE users
SET age = 31
WHERE username = 'john_doe';`


**delete existing records**

`DELETE FROM table_name
WHERE condition;`

`DELETE FROM users
WHERE username = 'john_doe';`


### Subquery
Subqueries, also known as nested queries or inner queries, are SQL queries that are embedded within another SQL query.


## MySQL Functions
MySQL provides a wide range of built-in functions that you can use to perform various operations on data stored in your database. These functions can be categorized into several types, including string functions, numeric functions, date and time functions, aggregate functions, and more.