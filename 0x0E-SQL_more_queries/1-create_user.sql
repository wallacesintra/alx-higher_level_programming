-- creates the MySQL server user
-- should have all privileges
-- password set to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
