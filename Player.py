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

    def print_split_hand(self):
        print(self.split_hand)

    def set_split_hand(self, split_hand):
        self.split_hand = split_hand
        return self.split_hand

    def get_split_hand(self):
        return self.split_hand

    def print_hands(self):
        joined_hand = []
        hand = self.hand.copy()
        hand.extend(self.split_hand)
        joined_hand.append(hand)
        print(joined_hand)

    def print_hand(self):
        print(self.hand)

    def set_id(self, id):
        self.id = id
        return self.id

    def get_id(self):
        return self.id

    def is_split_avail(self):
        return Hand().is_split_avail(self.hand)

    def add_cards_to_hand_from_deck(self, deck, hand_size):
        self.hand.append(Hand().get_hand_from_top_of_deck(deck, hand_size))

    def add_cards_to_split_hand_from_deck(self, deck, hand_size):
        self.split_hand.append(Hand().get_hand_from_top_of_deck(deck, hand_size))

    def init_split_hand(self):
        self.split_hand.append(self.hand.pop(1))

    def is_bust(self):
        total = 0
        for card in self.hand:
            total = total + card[0][2]
        if total > 21:
            return True
        else:
            return False

    def is_21(self):
        total = 0
        for card in self.hand:
            total = total + card[0][2]
        if total == 21:
            return True
        else:
            return False

    def get_total_of_hand(self):
        Hand().get_total_of_hand_ace_highest_if_possible(self.hand)

    def get_total_of_split_hand(self):
        Hand().get_total_of_hand_ace_highest_if_possible(self.split_hand)
