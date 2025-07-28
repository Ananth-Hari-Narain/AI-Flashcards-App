class Flashcard:
    term = ""
    definition = ""

    def __init__(self, term="", definition=""):
        self.term = term
        self.definition = definition

class FlashcardSet:
    name = None
    tags = None
    cards: list = None
    difficulty = None

    def __init__(self):
        pass

    def sort_flashcards(self, sorter):
        pass

    def add_flashcard(self, card):
        assert isinstance(card, Flashcard)
        self.cards.append(card)

    def delete_flashcard_at(self, cardIndex):
        self.cards.pop(cardIndex)


