from .connection import get_connection

def execute_database_change_safely(query, params=None):
    mydb = get_connection()
    try:
        with mydb.cursor() as cursor:
            cursor.execute(query, params)
        mydb.commit()
    finally:
        mydb.close()

def retrieve_from_database_safely(query, params=None):
    mydb = get_connection()
    try:
        with mydb.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    finally:
        mydb.close()
