from .connection import mydb
from .flashcard_sets import list_all_flashcard_sets_in_folder

def make_new_folder(name, parentFolder):
    mycursor = mydb.cursor()
    query = "INSERT INTO Folder (name, parentFolder) VALUES (%s, %s)"
    mycursor.execute(query, (name, parentFolder))
    mydb.commit()

def delete_empty_folder(folderID) -> bool:
    """
    This function will only delete an empty folder, so it first checks if a folder is not empty.
    :return: It will return False if the folder has flashcard sets in them and return True if it was able
    to successfully delete the set.
    """
    flashcard_sets_in_folder = list_all_flashcard_sets_in_folder(folderID)
    if len(flashcard_sets_in_folder) != 0:
        return False
    else:
        query = ("DELETE FROM Folder "
                 "WHERE Folder.id = %s;")
        mycursor = mydb.cursor()
        mycursor.execute(query, (folderID,))
        return True

def list_all_folders_in_folder(parent_folder_id):
    """
    :param parent_folder_id: When parent_folder_id = 0, all folders in root folder will be returned.
    :return: Returns the folder_id and folder name
    """
    mycursor = mydb.cursor()
    query = ("SELECT folder.id, folder.name "
             "FROM Folder "
             "WHERE folder.parentFolder = %s")
    mycursor.execute(query, (parent_folder_id, ))
    return mycursor.fetchall()

def list_all_folders():
    mycursor = mydb.cursor()
    query = ("SELECT folder.id, folder.name "
             "FROM Folder")
    mycursor.execute(query)
    return mycursor.fetchall()

def rename_folder(folderID, newName):
    mycursor = mydb.cursor()
    query = ("UPDATE Folder "
             "SET name = %s "
             "WHERE id = %s")
    mycursor.execute(query, (newName, folderID))
    mydb.commit()
