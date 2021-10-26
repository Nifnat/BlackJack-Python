from deck import Deck
from hand import Hand

class Dealer:

    def __init__(self):
        self.dealers_deck_obj = Deck()
        self.dealers_deck = []
        self.dealers_hand = []
        self.id = ""

    def set_hand(self, hand):
        self.hand = hand
        return self.hand

    def get_hand(self):
        return self.dealers_hand

    def print_hand(self):
        print(self.dealers_hand)

    def set_id(self, id):
        self.id = id
        return self.id

    def get_id(self):
        return self.id

    def add_cards_to_hand_from_deck(self, deck, cards_to_add):
        self.dealers_hand.append(Hand().get_hand_from_top_of_deck(deck, cards_to_add))

    def start_round(self, players):
        self.dealers_deck = self.dealers_deck_obj.get_shuffled_deck()
        for player in players:  # pretend it's initial betting phase
            player.set_chips(10)
            print("bet?")
            player.remove_chips(5)  # static bet amount

        for player in players:  # pretend it's initial betting phase
            print(f'Give card to {player.get_id()}')
            print(player.get_chips())
            player.add_cards_to_hand_from_deck(self.dealers_deck, 1)
            player.print_hand()
            self.add_cards_to_hand_from_deck(self.dealers_deck, 1)
            self.print_hand()
