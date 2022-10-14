#!/usr/bin/python3
"""Delete records"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    data = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    a = data.cursor()
    check = (argv[4], )
    a.execute("SELECT * FROM states WHERE name=%s\
    ORDER BY states.id ASC", check)
    x = a.fetchall()
    for i in x:
        print(i)
    a.close()
    data.close()
