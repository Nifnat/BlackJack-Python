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

    def get_total_of_hand_ace_highest_if_possible(self, hand):
        total = 0
        total = self.get_total_of_hand_ace_high(hand)
        if total > 21:
            total = self.get_total_of_hand_ace_low(hand)
            return total
        return total

    def get_total_of_hand_ace_low(self, hand):
        total = 0
        card_value = 0
        for card in hand:
            if card[0][0] == "queen" or card[0][0] == "king" or card[0][0] == "jack":
                card_value = 10
            elif card[0][0] == "ace":
                card_value = 1
            else:
                card_value = card[0][2]
            total = total + card_value
        return total

    def get_total_of_hand_ace_high(self, hand):
        total = 0
        card_value = 0
        for card in hand:
            if card[0][0] == "queen" or card[0][0] == "king" or card[0][0] == "jack":
                card_value = 10
            elif card[0][0] == "ace":
                card_value = 11
            else:
                card_value = card[0][2]
            total = total + card_value
        return total
