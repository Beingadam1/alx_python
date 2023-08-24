'''
Script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
But this time safe from MySQL injections.
'''
# import modules
import MySQLdb
import sys

if __name__ == "__main__":
    # arguement supplied by user
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    searched = sys.argv[4]

    # connect to database
    database = MySQLdb.connect(
        host='localhost', port=3306, user=user, passwd=password, db=db_name
    )

    # create a cursor
    cursor = database.cursor()

    # create query
    query = 'SELECT * FROM states WHERE name = %(state_key)s ORDER BY id ASC'
    cursor.execute(query, {'state_key': searched})

    # Return results
    results = cursor.fetchall()

    for result in results:
        print(result)

    # close connections
    cursor.close()
    database.close()
