#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
take 3 arguments: mysql username, mysql password and database name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
