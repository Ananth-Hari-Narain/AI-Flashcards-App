from . import retrieve_from_database_safely, execute_database_change_safely

def add_flashcard(term, definition, flashcardSetID):
    """Adds a flashcard to a particular set."""
    query = "INSERT INTO Flashcard (term, definition, setID) VALUES (%s, %s, %s)"
    execute_database_change_safely(query, (term, definition, flashcardSetID))


def delete_flashcard(flashcardID):
    """Deletes a flashcard by ID."""
    query = "DELETE FROM Flashcard WHERE id = %s"
    execute_database_change_safely(query, (flashcardID,))


def list_flashcards_in_set(flashcardSetID):
    """
    Lists all flashcards in a set.
    :return: id, term, definition
    """
    query = (
        "SELECT Flashcard.id, term, definition "
        "FROM Flashcard "
        "INNER JOIN FlashcardSet ON Flashcard.setID = FlashcardSet.id "
        "WHERE FlashcardSet.id = %s;"
    )
    return retrieve_from_database_safely(query, (flashcardSetID,))


def change_flashcard_term(flashcardID, newTerm):
    """Updates the term of a flashcard."""
    query = "UPDATE Flashcard SET term = %s WHERE id = %s"
    execute_database_change_safely(query, (newTerm, flashcardID))


def change_flashcard_definition(flashcardID, newDefinition):
    """Updates the definition of a flashcard."""
    query = "UPDATE Flashcard SET definition = %s WHERE id = %s"
    execute_database_change_safely(query, (newDefinition, flashcardID))
