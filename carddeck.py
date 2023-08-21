from dataclasses import dataclass
import random
# in Java, 'self', would be 'this'

@dataclass
class Card:
    rank: str
    suit: str


class CardDeck:    # inherits from 'object'
    SUITS = "Clubs Diamonds Hearts Spades".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, dealer_name=None):
        """
        CardDeck constructor
        """
        if dealer_name is None:
            dealer_name = "NONE"
        self.dealer_name = dealer_name
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return tuple(self._cards)

    @property
    def dealer_name(self):  # getter property
        return self._dealer_name  # return private data

    @dealer_name.setter
    def dealer_name(self, name: str):  # setter property
        if isinstance(name, str):
            self._dealer_name = name
        else:
            raise TypeError("Dealer must be a str")

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"""{my_name}("{self.dealer_name}")"""