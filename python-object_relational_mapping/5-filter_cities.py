'''
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database
'''
# import modules
import MySQLdb
import sys

if __name__ == "__main__":
    # arguement supplied by user
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # connect to MySQL
    database = MySQLdb.connect(
        host='localhost', port=3306, user=user, passwd=password, db=db_name
    )

    # create cursor
    cursor = database.cursor()

    # create query
    query = 'SELECT name\
        FROM cities\
        WHERE state_id = (SELECT id\
        FROM states WHERE name = %s)'
    cursor.execute(query, {'state_key': state_name})

    # return results
    result = cursor.fetchall()

    for index, item in enumerate(result):
        if index:
            print(', ', end="")
        print(item[0], end="")
    print()

    # close connections
    cursor.close()
    database.close()
