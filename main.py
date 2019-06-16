import objs
import paint


def engine():
    nCards = 6
    nHands = 3

    hands = []
    for i in range(0, nHands):
        hands.append(objs.Hand())

    deck = objs.Deck()
    deck.shuffle()

    if nHands * nCards > len(deck.cards):
        print("Not enough cards for this number of players ")
    for i in range(0, nHands):
        for j in range(0, nCards):
            hands[i].addCard(deck.removeCard())

    k = 0
    for i in hands:
        k += 1
        print('\n\nCards in ', k, ' hand:\n')
        i.print()


if __name__ == '__main__':

    engine()
    paint.main()
