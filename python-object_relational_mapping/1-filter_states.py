'''
Script that lists all states with a name starting with N.
'''
# import required modules
import MySQLdb
import sys

if __name__ == '__main__':
    # arguement supplied by user
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to MySQL
    database = MySQLdb.connect(
        host='localhost', port=3306, user=user, passwd=password, db=db_name
    )

    # create a cursor
    cur = database.cursor()

    # Create query
    query = 'SELECT * FROM states WHERE BINARY name LIKE "N%" ORDER BY id ASC'

    # select states that start with N
    cur.execute(query)

    # Return results
    result = cur.fetchall()

    for item in result:
        print(item)

    # close connections
    cur.close()
    database.close()
