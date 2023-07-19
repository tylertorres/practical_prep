from enum import Enum, auto


class Suit(Enum):
    HEARTS = auto()
    SPADES = auto()
    CLUBS = auto()
    DIAMONDS = auto()
    JOKER = auto()

    def __str__(self) -> str:
        return f"{self.name.capitalize()}"


class Card:
    @property
    def card_value(self) -> int:
        raise NotImplementedError()

    def __lt__(self, other):
        return self.card_value < other.card_value


class PlayingCard(Card):
    SUITS = {
        "Spades": Suit.SPADES,
        "Hearts": Suit.HEARTS,
        "Clubs": Suit.CLUBS,
        "Diamonds": Suit.DIAMONDS,
        "Joker": Suit.JOKER,
    }
    SUIT_NAMES = {enum: name for name, enum in SUITS.items()}
    VALUES = {
        "A": 1,
        "J": 11,
        "Q": 12,
        "K": 13,
        **{str(number): number for number in range(2, 11)},
    }
    VALUE_NAMES = {enum: name for name, enum in VALUES.items()}

    def __init__(self, suit: str, value: str):
        self.suit = self.SUITS[suit]
        self.value = self.VALUES[value]

    @property
    def card_value(self) -> int:
        return self.value

    def describe(self):
        return f"{self.VALUE_NAMES[self.card_value]} of {self.suit}"


class JokerCard(Card):
    def __init__(self, color: str):
        self.suit = Suit.JOKER
        self.color = color

    @property
    def card_value(self) -> int:
        return 14

    def describe(self):
        return f"{self.color} Joker"


class Game:
    def __init__(self):
        self.deck: list[Card] = []

    def add_card(self, suit: str, value: str) -> None:
        self.deck.append(PlayingCard(suit, value))

    def add_joker(self, color: str) -> None:
        self.deck.append(JokerCard(color))

    def card_string(self, card: int) -> str:
        return self.deck[card].describe()

    def card_beats(self, card_a: int, card_b: int) -> bool:
        return self.deck[card_a] > self.deck[card_b]


""" 
- Enums for Suits (class)
- keep track of cards being created (var)
- string representation of each card ( like a description ) func()
-  

 """

if __name__ == "__main__":
    game = Game()
    suit, value = input().split()
    game.add_card(suit, value)
    print(game.card_string(0))
    suit, value = input().split()
    game.add_card(suit, value)
    print(game.card_string(1))
    print("true" if game.card_beats(0, 1) else "false")
