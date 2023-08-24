'''
Write a script that lists all states from the database hbtn_0e_0_usa:
Your script should take 3 arguments: mysql username, mysql password
and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
'''

# Import modules needed
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # arguement supplied by user
    HOST = 'localhost'
    PORT = '3306'
    MY_USER = argv[1]
    MY_PSWD = argv[2]
    MY_DB = argv[3]

    # connect to mysqldb
    database = MySQLdb.connect(
        host=HOST, user=MY_USER, password=MY_PSWD, db=MY_DB, port=PORT
    )

    # Create cursor
    cur = database.cursor()

    # Tackle task
    # create query
    query = 'SELECT * FROM state ORDER BY id ASC'

    # execute query with cursor
    cur.execute(query)

    # fetch results
    results = cur.fetchall()

    for result in results:
        print(result)

    # close connection
    cur.close()
    database.close()
