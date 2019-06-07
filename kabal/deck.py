from itertools import product
from random import shuffle

SUITS = ["Hearts", "Spades", "Clubs", "Diamonds"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"Card({self.rank} of {self.suit})"


class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit, rank in product(SUITS, RANKS)]

    def shuffle(self):
        shuffle(self.deck)

    def __iter__(self):
        return iter(self.deck)


if __name__ == "__main__":
    deck = Deck()
    for card in deck:
        print(card)

    print("\n== Ev'ry day I'm shufflin' ==\n")
    deck.shuffle()
    for card in deck:
        print(card)
