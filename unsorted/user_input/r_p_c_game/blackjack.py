from __future__ import annotations

import itertools
from dataclasses import dataclass, field
from enum import Enum, auto
import random


class Face(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Suit(Enum):
    DIAMONDS = "Diamonds"
    HEARTS = "Hearts"
    SPADES = "Spades"
    CLUBS = "Clubs"


@dataclass
class Card:
    face: Face
    suit: Suit

    def __lt__(self, other: Card):
        return self.face == Face.ACE or self.face.value < other.face.value


@dataclass
class Hand:
    cards: list[Card] = field(default_factory=list)
    _BLACKJACK = 21

    def __setattr__(self, key, value):
        if key == '_BLACKJACK':
            raise AttributeError(f"Can't reassign constant '{key}'")
        self.__dict__[key] = value

    def add_card(self, card: Card):
        self.cards.append(card)

    def calculate_score(self):
        result = 0
        for card in sorted(self.cards, reverse=True):
            match card.face:
                case Face.JACK | Face.QUEEN | Face.KING:
                    result += 10
                case Face.ACE:
                    if (self._BLACKJACK - result) >= 11:
                        result += 11
                    else:
                        result += 1
                case _:
                    result += card.face.value
        return result


def get_card() -> Card:
    card = random.choice(PLAY_DECK)
    PLAY_DECK.remove(card)
    return card


PLAY_DECK = [Card(*item) for item in itertools.product(Face, Suit)] * 8
print(f"{len(PLAY_DECK)=}")

play_hand = Hand([get_card(), get_card()])

print(f"{play_hand._BLACKJACK=}")

print(f"{len(PLAY_DECK)=}")

print(*play_hand.cards, sep='\n')
print(f"{play_hand.calculate_score()=}")
