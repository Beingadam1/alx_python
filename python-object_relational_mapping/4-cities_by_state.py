'''
A script that lists all cities from the database.
'''
# import moduled
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

    # create a cursor
    cursor = database.cursor()

    # create query
    query = '''SELECT cities.id, cities.name, states.name
        FROM cities, states
        WHERE states.id = state_id
        ORDER BY cities.id ASC'''

    # execute main task
    cursor.execute(query)

    # return results
    results = cursor.fetchall()

    for result in results:
        print(result)

    # close connections
    cursor.close()
    database.close()
