#!/usr/bin/python3
""" script that lists all cities of a state """

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state = sys.argv[4]

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = database.cursor()
    query = "SELECT cities.name FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s \
        ORDER BY cities.id ASC"
    cursor.execute(query, (state,))

    cities = cursor.fetchall()

    if cities:
        print(", ".join(city[0] for city in cities))
    else:
        print()

    cursor.close()
    database.close()
