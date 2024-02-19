# **Creating a new user**
root user has all priviledges
it’s best to avoid using this account outside of administrative functions.

1. `sudo mysql`
    `mysql -u root -p` - If your root MySQL user is configured to authenticate with a password, you will need to use a different command to access the MySQL shell. The following will run your MySQL client with regular user privileges, and you will only gain administrator privileges within the database by authenticating with the correct password

2. Once you have access to the MySQL prompt, you can create a new user with a CREATE USER statement. These follow this general syntax:
    `CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';`

    For example, to create a user named 'newuser' with password 'password123' who can connect from 'localhost', you would run:
    `CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password123';`

3. Grant Permissions, grant the user permissions to access databases and perform operations. 
    `GRANT privileges ON database_name.* TO 'username'@'hostname';`
    Replace 'privileges' with the specific privileges you want to grant (e.g., SELECT, INSERT, UPDATE, DELETE, ALL PRIVILEGES),

    to grant all privileges on a database named 'exampledb' to the 'newuser' from 'localhost', you would run:
    `GRANT ALL PRIVILEGES ON exampledb.* TO 'newuser'@'localhost';`

4. Flush Privileges: After granting permissions, you need to flush the privileges to ensure that the changes take effect immediately:
    `FLUSH PRIVILEGES;`

5. Exit MySQL Shell
    `EXIT;`




# **Granting Priviledges**

Priviledges: SELECT, INSERT, UPDATE, DELETE, ALL PRIVILEDGES

**granting all priviledges on a database**
`GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'hostname';`

**granting specific priviledges on a database**
`GRANT SELECT, INSERT, UPDATE ON database_name.table_name TO 'username'@'hostname';`

# **Revoking priviledges**

**revoking all priviledges on a database**
`REVOKE ALL PRIVILEGES ON database_name.* FROM 'username'@'hostname';`

**revoking specific priviledges on a database**
`REVOKE SELECT, INSERT, UPDATE ON database_name.* FROM 'username'@'hostname';`

**revoking all priviledges on a table**
`REVOKE ALL PRIVILEGES ON database_name.table_name FROM 'username'@'hostname';`

**revoking specific priviledges on a table**
`REVOKE SELECT, INSERT, UPDATE ON database_name.table_name FROM 'username'@'hostname';`


Make sure to use FLUSH PRIVILEGES; after granting or revoking privileges to ensure that the changes take effect immediately.
`FLUSH PRIVILEGES;`





# **MySQL Constraints**
Constraints are placed on columns or tables, they limit the data that can be inserted into the tables.

**NOT NULL constraint**
can not have NULL values
 `CREATE TABLE People(Id INTEGER, LastName TEXT NOT NULL, FirstName TEXT NOT NULL, City VARCHAR(55))`
column FirstName and LastName can not have null values.

**UNIQUE constraints**
it ensures all values in a column are unique.
`CREATE TABLE Brands(Id INTEGER, BrandName VARCHAR(30) UNIQUE)`
BrandName is set to UNIQUE, there cannot be two brands with same name.

PRIMARY KEY constraint automatically has a UNIQUE constraint defined on it.

**PRIMARY KEY**
it uniquely identifies each record in a database table. 
Only one primary name in a table.
Primary keys can be used as a foreign keys in other tables, when there is relation among tables.
`CREATE TABLE Brands (Id INTEGER PRIMARY KEY, BrandName VARCHAR(30))`

**FOREIGN KEY**
A foreign key in one table points to a primary key in another table.
it is a referential constraint between two tables.

**ENUM constraint**
ENUM - string object with a value chosen from a list of a permitted values.
they are enumerated explicitly in the column specification at table creation time.
`CREATE TABLE Shops(Id INTEGER, Name VARCHAR(55), Quality ENUM('High', 'Average', 'Low'));`
`INSERT INTO Shops VALUES(1, 'Boneys', 'High');`
`INSERT INTO Shops VALUES(2, 'AC River', 'Average');`

**SET constraint**
SET can have zero/more values, each of the values must be chosen from a list of permitted values.
`CREATE TABLE Students(Id INTEGER, Name VARCHAR(55), Certificates SET('A1', 'A2', 'A3', 'C1'))`
`INSERT INTO Students VALUES(2, 'Jane', 'A1,B1,A2');`
`INSERT INTO Students VALUES(3, 'Mark', 'A1,A2,D1,D2');`



# **SQL subqueries**
Subquery - allows using result of a query as part of another query.

`        SELECT cFirstName, cLastName, cZipCode
        FROM customers
        WHERE cZipCode =        
          (SELECT cZipCode
           FROM customers
           WHERE cFirstName = 'Wayne' AND cLastName = 'Dick');`


