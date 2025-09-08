from .connection import get_connection
def clear_all_tables():
    mydb = get_connection()
    mycursor = mydb.cursor()
    query = "SHOW TABLES"
    mycursor.execute(query)
    lst = mycursor.fetchall()
    for x in lst:
        query = f"TRUNCATE TABLE {x[0]}"
        mycursor.execute(query)
        mydb.commit()

def destroy_table():
    mydb = get_connection()
    mycursor = mydb.cursor()
    query = "DROP TABLE FlashcardSet"
    mycursor.execute(query)
    mydb.commit()

def show_db_structure():
    mydb = get_connection()
    mycursor = mydb.cursor()
    query = "SHOW TABLES"
    mycursor.execute(query)
    lst = mycursor.fetchall()
    for x in lst:
        query = f"DESCRIBE {x[0]}"
        mycursor.execute(query)
        columns = mycursor.fetchall()
        print(x[0])
        for col in columns:
            print(col)
        print("\n")
