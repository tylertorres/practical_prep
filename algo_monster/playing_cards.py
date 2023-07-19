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
        self.hands: list[list[Card]] = []

    def add_card(self, suit: str, value: str) -> None:
        self.deck.append(PlayingCard(suit, value))

    def add_joker(self, color: str) -> None:
        self.deck.append(JokerCard(color))

    def card_string(self, card: int) -> str:
        return self.deck[card].describe()

    def card_beats(self, card_a: int, card_b: int) -> bool:
        return self.deck[card_a] > self.deck[card_b]

    def add_hand(self, card_indices: list[int]) -> None:
        current_hand = [self.deck[index] for index in card_indices]
        self.hands.append(current_hand)

    def hand_string(self, hand: int) -> str:
        card_descriptions = []
        for card in self.hands[hand]:
            card_descriptions.append(card.describe())
        return ", ".join(card_descriptions)

    def hand_beats(self, hand_a: int, hand_b: int) -> bool:
        cards_in_a = sorted(self.hands[hand_a], reverse=True)
        cards_in_b = sorted(self.hands[hand_b], reverse=True)

        a_pointer = b_pointer = 0
        n, m = len(cards_in_a), len(cards_in_b)

        while a_pointer < n and b_pointer < m:
            value_a = cards_in_a[a_pointer].card_value
            value_b = cards_in_b[b_pointer].card_value

            print(value_a)
            print(value_b)

            if value_a == value_b:
                a_pointer += 1
                b_pointer += 1
            elif value_a > value_b:
                return True
            else:
                return False


if __name__ == "__main__":
    game = Game()
    hand_a_list = []
    n_1 = int(input())
    for i in range(n_1):
        suit, value = input().split()
        game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
        hand_a_list.append(i)
    game.add_hand(hand_a_list)
    print(game.hand_string(0))
    hand_b_list = []
    n_2 = int(input())
    for i in range(n_1, n_1 + n_2):
        suit, value = input().split()
        game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
        hand_b_list.append(i)
    game.add_hand(hand_b_list)
    print(game.hand_string(1))
    print("true" if game.hand_beats(0, 1) else "false")
