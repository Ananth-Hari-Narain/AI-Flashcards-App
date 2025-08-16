from connection import mydb
from datetime import datetime

def make_new_flashcard_set(name, folderID):
    mycursor = mydb.cursor()
    current_time = datetime.now()
    query = "INSERT INTO FlashcardSet (name, whenCreated, lastModified, folderID) VALUES (%s, %s, %s, %s)"
    mycursor.execute(query, (name, current_time, current_time, folderID))
    mydb.commit()


def delete_flashcard_set(flashcardSetID):
    mycursor = mydb.cursor()
    query = """DELETE FROM FlashcardSet
    WHERE id = %s"""
    mycursor.execute(query, (flashcardSetID,))
    mydb.commit()

def list_all_flashcard_sets_in_folder(folder_id):
    """
    :param folder_id: When folder_id = -1, it will list all flashcard sets in all folders
    """
    mycursor = mydb.cursor()
    if folder_id == -1:
        query = ("SELECT name "
                 "FROM FlashcardSet;")
        mycursor.execute(query)
    else:
        query = ("SELECT name "
                 "FROM FlashcardSet "
                 "INNER JOIN Folder ON Folder.id = FlashcardSet.folderID "
                 "WHERE Folder.id = %s")
        mycursor.execute(query, (folder_id,))


    return mycursor.fetchall()

def list_all_flashcard_sets():
    return list_all_flashcard_sets_in_folder(-1)

def rename_flashcard_set(flashcardSetID, newName):
    mycursor = mydb.cursor()
    query = ("UPDATE FlashcardSet "
             "SET name = %s "
             "WHERE id = %s")
    mycursor.execute(query, (newName, flashcardSetID))
    mydb.commit()
