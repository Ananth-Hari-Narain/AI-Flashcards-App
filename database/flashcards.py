from .connection import mydb

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

def list_flashcards_in_set(flashcardSetID):
    """
    :return: id, term, definition
    """
    mycursor = mydb.cursor()
    query = ("SELECT Flashcard.id, term, definition "
             "FROM Flashcard "
             "INNER JOIN FlashcardSet ON Flashcard.setID = FlashcardSet.id "
             "WHERE FlashcardSet.id = %s;")
    mycursor.execute(query, (flashcardSetID, ))
    return mycursor.fetchall()

def change_flashcard_term(flashcardID, newTerm):
    mycursor = mydb.cursor()
    query = ("UPDATE Flashcard "
             "SET term = %s "
             "WHERE id = %s")
    mycursor.execute(query, (newTerm, flashcardID))
    mydb.commit()

def change_flashcard_definition(flashcardID, newDefinition):
    mycursor = mydb.cursor()
    query = ("UPDATE Flashcard "
             "SET definition = %s "
             "WHERE id = %s")
    mycursor.execute(query, (newDefinition, flashcardID))
    mydb.commit()
