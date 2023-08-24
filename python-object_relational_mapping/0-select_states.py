'''
Script that list all states from a database.
'''
# import needed modules
import MySQLdb
import sys

if __name__ == "__main__":
    # arguement supplied by user
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to MySQL
    database = MySQLdb.connect(
        host='localhost', port=3306, user=user, passwd=password, db=db_name
    )

    # Create cursor
    cur = database.cursor()

    # Create query
    query = 'SELECT * FROM states ORDER BY id ASC'

    # Time to execute our main task
    cur.execute(query)

    # fetch results
    results = cur.fetchall()

    for result in results:
        print(result)

    # close connections
    cur.close()
    database.close()
