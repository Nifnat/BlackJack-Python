from blackjack import Blackjack
from deck import Deck

if __name__ == '__main__':
    deckObj = Deck()
    s_deck = deckObj.get_shuffled_deck()
    print(s_deck)
    cards_to_add = []
    for x in range(15, 18):
        cards_to_add.append(s_deck.pop(x))
    deckObj.shuffle_cards_into_deck(s_deck, cards_to_add)
    print(s_deck)
    deckObj.shuffle_deck(s_deck)
    print(deckObj.shuffle_deck(s_deck))
    hand = deckObj.get_random_hand(s_deck, 5)
    print(hand)
    print(s_deck)
    blackjackobj = Blackjack()
    blackjackobj.start()

