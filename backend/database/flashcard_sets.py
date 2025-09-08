from .helpers import *
from datetime import datetime

def make_new_flashcard_set(name, folderID):
    """Create a new flashcard set inside a folder. Returns id of new flashcard set"""
    current_time = datetime.now()
    query = """
        INSERT INTO FlashcardSet (name, whenCreated, lastModified, folderID)
        VALUES (%s, %s, %s, %s)
    """
    return execute_database_insert_safely(query, (name, current_time, current_time, folderID))


def delete_flashcard_set(flashcardSetID):
    """Delete a flashcard set by ID."""
    query = "DELETE FROM FlashcardSet WHERE id = %s"
    execute_database_delete_safely(query, (flashcardSetID,))


def list_all_flashcard_sets_in_folder(folder_id):
    """
    :return: list of (set id, set name)
    """
    query = """
        SELECT FlashcardSet.id, FlashcardSet.name
        FROM FlashcardSet
        INNER JOIN Folder ON Folder.id = FlashcardSet.folderID
        WHERE Folder.id = %s
    """
    return retrieve_from_database_safely(query, (folder_id,))


def list_all_flashcard_sets():
    """Shortcut for listing all sets."""
    query = "SELECT id, name FROM FlashcardSet;"
    return retrieve_from_database_safely(query)


def rename_flashcard_set(flashcardSetID, newName):
    """Rename a flashcard set."""
    query = ("UPDATE FlashcardSet "
             "SET name = %s "
             "WHERE id = %s")
    execute_database_update_safely(query, (newName, flashcardSetID))

def move_flashcard_set(flashcardSetID, newFolderID):
    """Move a flashcard set to a new folder"""
    query = ("UPDATE FlashcardSet "
             "SET folderID = %s "
             "WHERE id = %s")
    execute_database_update_safely(query, (newFolderID, flashcardSetID))