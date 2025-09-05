from .helpers import *
from .flashcard_sets import list_all_flashcard_sets_in_folder

def make_new_folder(name, parentFolder):
    """Create a new folder under a parent. Returns the id of the folder."""
    query = "INSERT INTO Folder (name, parentFolder) VALUES (%s, %s)"
    return execute_database_insert_safely(query, (name, parentFolder))


def delete_empty_folder(folderID) -> bool:
    """
    Delete a folder only if it has no flashcard sets nor folders inside.
    :return: True if deleted, False if not empty
    """
    flashcard_sets_in_folder = list_all_flashcard_sets_in_folder(folderID)
    folders_in_folder = list_all_folders_in_folder(folderID)
    if len(flashcard_sets_in_folder) + len(folders_in_folder) != 0:
        return False
    else:
        query = "DELETE FROM Folder WHERE Folder.id = %s;"
        execute_database_delete_safely(query, (folderID,))
        return True


def list_all_folders_in_folder(parent_folder_id):
    """
    :param parent_folder_id: When = 0, returns all folders in the root.
    :return: list of (folder_id, folder name)
    """
    query = "SELECT Folder.id, Folder.name FROM Folder WHERE Folder.parentFolder = %s"
    return retrieve_from_database_safely(query, (parent_folder_id,))


def list_all_folders():
    """List all folders in the database."""
    query = "SELECT Folder.id, Folder.name FROM Folder"
    return retrieve_from_database_safely(query)


def rename_folder(folderID, newName):
    """Rename a folder."""
    query = "UPDATE Folder SET name = %s WHERE id = %s"
    execute_database_update_safely(query, (newName, folderID))


def get_parent_folder(folderID):
    """
    Get the parent folder of a folder.
    Root folders (id=0) return 0.
    """
    if folderID == 0:
        return 0
    query = "SELECT parentFolder FROM Folder WHERE id = %s"
    result = retrieve_from_database_safely(query, (folderID,))
    return result[0][0]
