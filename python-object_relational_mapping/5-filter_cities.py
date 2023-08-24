'''
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database
'''
# import modules
import MySQLdb
import sys

if __name__ == '__main__':
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
    cur = database.cursor()

    # create query
    cur.execute(
        'SELECT cities.name FROM cities JOIN states ON \
        cities.state_id = states.id WHERE states.name LIKE %s \
        ORDER BY cities.id',
        (state_name,),
    )

    results = cur.fetchall()
    list = []
    for result in results:
        list.append(result[0])
    print(", ".join(list))
    cur.close()
    database.close()
