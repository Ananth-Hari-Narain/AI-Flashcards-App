import datetime
import mysql.connector
from os import getenv
from dotenv import load_dotenv

load_dotenv("file.env")

mydb = mysql.connector.connect(
    host="localhost",
    user=getenv("DB_USERNAME"),
    password=getenv("DB_PASSWORD"),
    database="flashcardsdb"
)

def make_new_folder(name, parentFolder):
    mycursor = mydb.cursor()
    query = "INSERT INTO Folder (name, parentFolder) VALUES (%s, %s)"
    mycursor.execute(query, (name, parentFolder))
    mydb.commit()

def make_new_flashcard_set(name, folderID):
    mycursor = mydb.cursor()
    current_time = datetime.datetime.now()
    query = "INSERT INTO FlashcardSet (name, whenCreated, lastModified, folderID) VALUES (%s, %s, %s, %s)"
    mycursor.execute(query, (name, current_time, current_time, folderID))
    mydb.commit()

def add_flashcard(term, definition, flashcardSetID):
    # Adds flashcards to a particular set. The term and definition are entered by the user.
    # The flashcardSetID will be determined by the program
    mycursor = mydb.cursor()
    query = "INSERT INTO Flashcard (term, definition, setID) VALUES (%s, %s, %s)"
    mycursor.execute(query, (term, definition, flashcardSetID))
    mydb.commit()

def delete_flashcard(flashcardID):
    mycursor = mydb.cursor()
    query = """DELETE FROM Flashcard
WHERE id = %s"""
    mycursor.execute(query, (flashcardID,))
    mydb.commit()

def delete_flashcard_set(flashcardSetID):
    mycursor = mydb.cursor()
    query = """DELETE FROM FlashcardSet
    WHERE id = %s"""
    mycursor.execute(query, (flashcardSetID,))
    mydb.commit()

def delete_empty_folder(folderID) -> bool:
    """
    This function will only delete an empty folder, so it first checks if a folder is not empty.
    :return: It will return False if the folder has flashcard sets in them and return True if it was able
    to successfully delete the set.
    """
    flashcard_sets_in_folder = list_all_flashcard_sets_in_folder(folderID)
    if len(flashcard_sets_in_folder) == 0:
        return False
    else:
        query = ("DELETE FROM Folder "
                 "WHERE Folder.id = %s;")
        mycursor = mydb.cursor()
        mycursor.execute(query, (folderID,))
        return True

def list_flashcards_in_set(flashcardSetID):
    mycursor = mydb.cursor()
    query = ("SELECT Flashcard.id, term, definition "
             "FROM Flashcard "
             "INNER JOIN FlashcardSet ON Flashcard.setID = FlashcardSet.id "
             "WHERE FlashcardSet.id = %s;")
    mycursor.execute(query, (flashcardSetID, ))
    return mycursor.fetchall()

def list_all_flashcard_sets_in_folder(folder_id):
    """
    :param folder_id: When folder_id = -1, it will list all flashcard sets in all folders
    """
    mycursor = mydb.cursor()
    if folder_id == -1:
        query = ("SELECT name "
                 "FROM FlashcardSet;")
    else:
        query = ("SELECT name "
                 "FROM FlashcardSet "
                 "INNER JOIN Folder ON Folder.id = FlashcardSet.folderID "
                 "WHERE Folder.id = %s")

    mycursor.execute(query, (folder_id, ))
    return mycursor.fetchall()

def list_all_folders_in_folder(parent_folder_id):
    """
    :param parent_folder_id: When parent_folder_id = 0, all folders in root folder will be returned.
    When parent_folder_id = -1, all folders in the database will be returned to the user.
    :return: Returns the folder_id and folder name
    """
    mycursor = mydb.cursor()
    query = ("SELECT folder.id, folder.name"
             "FROM Folder"
             "WHERE folder.parentFolder = %s")
    mycursor.execute(query, (parent_folder_id, ))
    return mycursor.fetchall()

def list_all_folders():
    mycursor = mydb.cursor()
    query = ("SELECT folder.id, folder.name"
             "FROM Folder")
    mycursor.execute(query)
    return mycursor.fetchall()

## Testing functions below: to be deleted ##

def add_test():
    make_new_flashcard_set("CS_TEST", 1)
    add_flashcard("What is a virus?", "A type of pathogen.", 2)
    add_flashcard("What does MBR stand for?", "Memory Buffer Register", 2)

def add_test_2():
    make_new_flashcard_set("BIO_TEST", 1)
    add_flashcard("What is a fish?", "Water animal", 1)
    add_flashcard("What type of animal is a koala?", "Marsupial", 1)

def list_test(j=0):
    lst = list_flashcards_in_set(j)
    for x in lst:
        print(x)

def test_clear_tables():
    mycursor = mydb.cursor()
    query = """TRUNCATE TABLE Flashcard"""
    mycursor.execute(query)
    mycursor.execute("TRUNCATE TABLE FlashcardSet")
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


