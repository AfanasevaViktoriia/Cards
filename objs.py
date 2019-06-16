import random
import copy


class Card():
    # 0 - пики
    # 1 - трефы
    # 2 - буби
    # 3 - червы
    # Туз - 1, валет - 11, дама - 12, король - 13

    def __init__(self, val=0, suit=0):
        self.value = val
        self.suit = suit

    def print(self):
        print('Card\'s suit is ', self.suit, ' and card\'s value is ', self.value)


class Deck():
    cards = []

    def __init__(self, type=1):
        if (type == 1):
            for suit in range(0, 4):
                self.cards.append(Card(1, suit))
                for val in range(6, 14):
                    self.cards.append(Card(val, suit))

    def removeCard(self):
        card = self.cards[-1]
        self.cards[:] = self.cards[:-1]
        return card

    def addCard(self, card):
        self.cards.insert(0, card)

    def shuffle(self):
        for i in range(0, len(self.cards)):
            temp = self.cards[i]
            j = random.randint(0, len(self.cards) - 1)
            self.cards[i] = self.cards[j]
            self.cards[j] = temp

    def print(self):
        for i in range(0, len(self.cards)):
            self.cards[i].print()


class Hand():
    cards = []

    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.insert(0, card)

    def removeCard(self, i):
        card = self.cards[i]
        del self.cards[i]
        return card

    # Give away all the cards
    def discard(self):
        handsCard = self.cards
        self.cards = []
        return handsCard

    def print(self):
        for i in range(0, len(self.cards)):
            self.cards[i].print()


class Table():
    hands = []
    cardsInPlay = []

    def __init__(self):
        self.hands = []

    def addHand(self, a):
        tmp = copy.copy(a)
        self.hands.append(tmp)
        return self.hands

    def removeHand(self, d):
        hand = self.hands[d]
        del self.hands[d]
        return hand

    def cleanTable(self):
        hands = []
        return hands

    def findMaxCardIndex(self):
        max = 0
        maxi = 0
        suit = 0
        for i in range(0, len(self.cardsInPlay)):
            if self.cardsInPlay[i].value > max:
                max = self.cardsInPlay[i].value
                maxi = i
                suit = self.cardsInPlay[i].suit
            if self.cardsInPlay[i].value == max:
                if self.cardsInPlay[i].suit > suit:
                    maxi = i
                    suit = self.cardsInPlay[i].suit
        return maxi
