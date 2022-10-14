#!/usr/bin/python3
"""List states in database"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    data = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    a = data.cursor()
    a.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC;")
    x = a.fetchall()
    for i in x:
        print(i)
    a.close()
    data.close()
