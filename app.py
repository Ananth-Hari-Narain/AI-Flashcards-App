import database

def view_folder_contents(folderID):
    folders = database.folders.list_all_folders_in_folder(folderID)
    flashcardSets = database.flashcard_sets.list_all_flashcard_sets_in_folder(folderID)
    for folder in folders:
        print(f"Folder {folder[0]}: {folder[1]}")
    for flashcardSet in flashcardSets:
        print(f"Set {flashcardSet[0]}: {flashcardSet[1]}")

def view_flashcard_set_contents(flashcardSetID):
    flashcards = database.flashcards.list_flashcards_in_set(flashcardSetID)
    for card in flashcards:
        print(f"Card {card[0]}")
        print("Term: " + card[1])
        print("Definition: " + card[2] + "\n")

def app_loop():
    instruction: str = "VIEW FOLDER"
    current_folder_id = 0

    while True:
        instruction = input("What would you like to do: ").upper()
        if instruction == "VIEW FOLDER":
            view_folder_contents(current_folder_id)
        elif instruction == "VIEW SET":
            setID = int(input("Enter the id of the flashcard set you want to view: "))
            view_flashcard_set_contents(setID)
        elif instruction == "GO TO FOLDER":
            current_folder_id = int(input("Give the id of the folder you want to go to: "))
        elif instruction == "CREATE FOLDER":
            name = input("What will the name of the folder be: ")
            database.folders.make_new_folder(name, current_folder_id)
        elif instruction == "CREATE SET":
            name = input("What will the name of the new set be: ")
            database.flashcard_sets.make_new_flashcard_set(name, current_folder_id)
        elif instruction == "ADD FLASHCARD":
            setID = int(input("Enter the id of the flashcard set you want to add the card to: "))
            term = input("Enter the term: ")
            definition = input("Enter the definition: ")
            database.flashcards.add_flashcard(term, definition, setID)
        elif instruction == "DELETE FLASHCARD":
            flashcardID = int(input("Enter the id of the flashcard you want to delete: "))
            database.flashcards.delete_flashcard(flashcardID)
        elif instruction == "DELETE SET":
            setID = int(input("Enter the id of the flashcard set you want to delete: "))
            database.flashcard_sets.delete_flashcard_set(setID)
        elif instruction == "DELETE EMPTY FOLDER":
            folderID = int(input("Enter the id of the folder you want to delete: "))
            if not database.folders.delete_empty_folder(folderID):
                print("Folder must be empty before deleting!")
        elif instruction == "RENAME FOLDER":
            newFolderName = input("What will the name of the new folder be: ")
            database.folders.rename_folder(current_folder_id, newFolderName)
        elif instruction == "RENAME SET":
            newFlashcardSetName = input("What will the name of the new set be: ")
            setID = int(input("Enter the id of the set you want to rename: "))
            database.flashcard_sets.rename_flashcard_set(setID, newFlashcardSetName)
        elif instruction == "CHANGE TERM":
            flashcardID = int(input("Enter the id of the flashcard you want to change: "))
            newTerm = input("Enter the new term for the flashcard: ")
            database.flashcards.change_flashcard_term(flashcardID, newTerm)
        elif instruction == "CHANGE DEF":
            flashcardID = int(input("Enter the id of the flashcard you want to change: "))
            newDef = input("Enter the new definition for the flashcard: ")
            database.flashcards.change_flashcard_definition(flashcardID, newDef)
        elif instruction == "EXIT":
            break
        else:
            print("Invalid instruction!")


if __name__ == "__main__":
    app_loop()
