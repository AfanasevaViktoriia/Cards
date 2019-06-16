import objs
import paint


def engine():
    nCards = 6
    nHands = 3

    table = objs.Table()
    deck = objs.Deck()
    deck.shuffle()

    if nHands * nCards > len(deck.cards):
        print("Not enough cards for this number of players ")
    hand = objs.Hand()
    for i in range(0, nHands):
        for j in range(0, nCards):
            hand.addCard(deck.removeCard())
        table.addHand(hand)
        hand.discard()

    k = 0
    for i in table.hands:
        k += 1
        print('\n\nCards in ', k, ' hand:\n')
        i.print()


if __name__ == '__main__':

    engine()
#    paint.main()
