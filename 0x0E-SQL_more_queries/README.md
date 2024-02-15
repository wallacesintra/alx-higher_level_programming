## creating a new user
root user has all priviledges
it’s best to avoid using this account outside of administrative functions.

1. `sudo mysql`
    `mysql -u root -p` - If your root MySQL user is configured to authenticate with a password, you will need to use a different command to access the MySQL shell. The following will run your MySQL client with regular user privileges, and you will only gain administrator privileges within the database by authenticating with the correct password

2. Once you have access to the MySQL prompt, you can create a new user with a CREATE USER statement. These follow this general syntax:
 `CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';`