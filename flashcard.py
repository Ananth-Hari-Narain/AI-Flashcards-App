import datetime

class Flashcard:
    def __init__(self, term="", definition=""):
        self.term = term
        self.definition = definition
        self.datetime_last_reviewed = datetime.datetime.now()
        self.number_of_times_reviewed = 0

    def review(self):
        self.datetime_last_reviewed = datetime.datetime.now()
        self.number_of_times_reviewed += 1

class FlashcardSet:
    def __init__(self, name, numberOfCards=4):
        """
        Defines a new flash card set with a number of blank cards as specified by numberOfCards.
        """
        self.name = name
        self.cards: list = []
        for i in range(numberOfCards):
            self.cards.append(Flashcard())

    def sort_flashcards_by(self, category, inAscendingOrder=True) -> None:
        """
        Sorts the flashcards by a particular category
        :param inAscendingOrder: If true, it will sort the set in ascending order
        :param category: For now, only "date reviewed" and "number of times reviewed" are the only valid categories.
        """
        if category == "date reviewed":
            self.cards.sort(key=lambda x: x.datetime_last_reviewed, reverse=inAscendingOrder)
        elif category == "number of times reviewed":
            self.cards.sort(key=lambda x: x.number_of_times_reviewed, reverse=inAscendingOrder)
        else:
            raise Exception("Invalid category entered for sorting flashcard set!")

    def add_flashcard(self, term="", definition=""):
        card = Flashcard(term, definition)
        self.cards.append(card)

    def delete_flashcard_at(self, cardIndex):
        self.cards.pop(cardIndex)

    def last_reviewed(self) -> datetime.time:
        most_recent_date = self.cards[0].datetime_last_reviewed
        for i in range(1, len(self.cards)):
            if self.cards[i].datetime_last_reviewed > most_recent_date:
                most_recent_date = self.cards[i].datetime_last_reviewed

        return most_recent_date
