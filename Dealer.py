from deck import Deck
from hand import Hand


class Dealer:

    def __init__(self):
        self.dealers_deck_obj = Deck()
        self.dealers_deck = []
        self.dealers_hand = []
        self.id = ""

    def set_hand(self, hand):
        self.dealers_hand = hand
        return self.dealers_hand

    def get_hand(self):
        return self.dealers_hand

    def print_hand(self):
        print(self.dealers_hand)

    def print_init_hand(self):
        print(self.init_hand(self.dealers_hand))

    def init_hand(self, cards):
        dealer_init_hand = []
        for i, card in enumerate(self.dealers_hand):
            if i == 0:
                dealer_init_hand.append("Face Down Card")
            else:
                dealer_init_hand.append(card)
        return dealer_init_hand

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
            print("bet?")  # Event here to ask if player is playing the hand
            player.remove_chips(5)  # static bet amount
            player.set_last_bet(5)

        #  These two loops and dealer code after each loop deal with the first round of cards being dealt out.
        for player in players:  # pretend it's initial betting phase

            print(f'Give card to {player.get_id()}')
            print(player.get_chips())
            player.add_cards_to_hand_from_deck(self.dealers_deck, 1)
            player.print_hand()

        #  Dealer
        self.add_cards_to_hand_from_deck(self.dealers_deck, 1)
        self.print_init_hand()  # this hand (1 card) would be show face down

        for player in players:  # pretend it's initial betting phase

            print(f'Give card to {player.get_id()}')
            print(player.get_chips())
            player.add_cards_to_hand_from_deck(self.dealers_deck, 1)
            player.print_hand()

        #  Dealer
        self.add_cards_to_hand_from_deck(self.dealers_deck, 1)
        self.print_init_hand()  # one face down and up (implement print method for this case)
        self.print_hand()
        #  Check dealers hand for 21
        print(Hand().get_total_of_hand_ace_highest_if_possible(self.dealers_hand))
        if (Hand().get_total_of_hand_ace_highest_if_possible(self.dealers_hand) == 21):
            print("BlackJack")
            # End hand here


        #  Await response from players

        #  Example of listener for player command
        player_command = "hit"
        for player in players:
            if player.get_id() == "Player 1":
                if player_command == "hit":
                    player.add_cards_to_hand_from_deck(self.dealers_deck, 1)
                    player.print_hand()
                    print(player.get_total_of_hand())
                if player_command == "split" and player.is_split_avail():
                    print("in split")
                    player.init_split_hand()
                    player.print_split_hand()
                    player.print_hands()
                if player_command == "Hold":
                    print("Skip")
                    #  Skip turn
