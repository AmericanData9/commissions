import psycopg2

def push_query(qry):
    connect = psycopg2.connect(
        host = '172.20.5.9',
        user = 'american',
        password = 'HX4d2lPH*&lhl1$d7r6>RD7',
        database = 'commissions',
        port = '5432'
    )

    connect.autocommit = True
    cursor = connect.cursor()
    cursor.execute(qry)


def get_query(qry):
    connect = psycopg2.connect(
        host = '172.20.5.9',
        user = 'american',
        password = 'HX4d2lPH*&lhl1$d7r6>RD7',
        database = 'commissions',
        port = '5432'
    )
    
    cursor = connect.cursor()
    cursor.execute(qry)
    data = cursor.fetchall()
    return data