from .connection import get_connection

def execute_database_delete_safely(query, params=None):
    mydb = get_connection()
    try:
        with mydb.cursor() as cursor:
            cursor.execute(query, params)
        mydb.commit()
    finally:
        mydb.close()

# For now, this is exactly the same as the above function.
def execute_database_update_safely(query, params=None):
    mydb = get_connection()
    try:
        with mydb.cursor() as cursor:
            cursor.execute(query, params)
        mydb.commit()
    finally:
        mydb.close()

# This version returns the id of the new record that was inserted.
def execute_database_insert_safely(query, params=None):
    mydb = get_connection()
    try:
        with mydb.cursor() as cursor:
            cursor.execute(query, params)
        mydb.commit()
    except Exception:
        mydb.rollback()
        return None
    finally:
        mydb.close()
        # If an exception has not occurred
        if cursor:
            return cursor.lastrowid

def retrieve_from_database_safely(query, params=None):
    mydb = get_connection()
    try:
        with mydb.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    finally:
        mydb.close()
