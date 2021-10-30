from hand import Hand

#  TODO Refactor this into an extendable class to be used for player and dealer
class Player:

    def __init__(self):
        self.chips = 0
        self.hand = []
        self.split_hand = []
        self.id = ""
        self.last_bet = 0

    def set_last_bet(self, count):
        self.last_bet = count
        return self.last_bet

    def set_chips(self, count):
        self.chips = count
        return self.chips

    def get_chips(self):
        return self.chips

    def add_chips(self, count):
        self.chips += count

    def remove_chips(self, count):
        self.chips -= count

    def set_hand(self, hand):
        self.hand = hand
        return self.hand

    def get_hand(self):
        return self.hand

    def print_hand(self):
        print(self.hand)

    def set_id(self, id):
        self.id = id
        return self.id

    def get_id(self):
        return self.id

    def add_cards_to_hand_from_deck(self, deck, cards_to_add):
        self.hand.append(Hand().get_hand_from_top_of_deck(deck, cards_to_add))
