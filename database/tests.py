from connection import mydb

def test_clear_tables():
    mycursor = mydb.cursor()
    query = """TRUNCATE TABLE Flashcard"""
    mycursor.execute(query)
    mycursor.execute("TRUNCATE TABLE FlashcardSet")
    mycursor.execute("TRUNCATE TABLE Folder")
    mydb.commit()

def destroy_table():
    mycursor = mydb.cursor()
    query = "DROP TABLE FlashcardSet"
    mycursor.execute(query)
    mydb.commit()

def show_db_structure():
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
