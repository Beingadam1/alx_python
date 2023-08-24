'''
Script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
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
    query = '''SELECT * FROM states WHERE BINARY name = '{}'
        ORDER BY id ASC'''.format(
        searched
    )
    cursor.execute(query)

    # Return results
    results = cursor.fetchall()

    for result in results:
        print(result)

    # close connections
    cursor.close()
    database.close()
