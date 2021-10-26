from random import SystemRandom

import cards

crypto_gen_random = SystemRandom()


class Deck():

    def get_shuffled_deck(self):
        # list52 = [x for x in range(52)]
        list52 = cards.cards.copy()
        list_rand_52 = []
        while list52:
            c_rand = crypto_gen_random.randrange(len(list52))
            list_rand_52.append(list52.pop(c_rand))
        return list_rand_52

    def shuffle_card_into_deck(self, deck, in_card):
        c_rand = crypto_gen_random.randrange(len(deck))
        deck.insert(c_rand, in_card)
        return deck

    def shuffle_cards_into_deck(self, deck, in_cards):
        for card in in_cards:
            self.shuffle_card_into_deck(deck, card)
        return deck

    def shuffle_deck(self, deck):
        deck_us = deck.copy()
        deck_s = []
        while deck_us:
            c_rand = crypto_gen_random.randrange(len(deck_us))
            deck_s.append(deck_us.pop(c_rand))
        return deck_s

    def get_random_card(self, deck):
        c_rand = crypto_gen_random.randrange(len(deck))
        card = deck.pop(c_rand)
        return card

    def get_random_hand(self, deck, hand_size):
        hand = []
        for x in range(hand_size):
            hand.append(self.get_random_card(deck))
        return hand
