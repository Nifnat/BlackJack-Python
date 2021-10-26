from random import SystemRandom

from deck import Deck

crypto_gen_random = SystemRandom()


class Hand():

    def __init__(self):
        self.deck_obj = Deck()

    def get_random_hand(self, deck, hand_size):
        hand = []
        for x in range(hand_size):
            hand.append(self.deck_obj.get_random_card(deck))
        return hand

    def get_hand_from_top_of_deck(self, deck, hand_size):
        hand = []
        for x in range(hand_size):
            hand.append(deck.pop(0))  # 0 is top card on deck
        return hand
