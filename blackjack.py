from Dealer import Dealer
from Player import Player

class Blackjack:

    def __init__(self):
        self.Dealer = Dealer()


    def start(self):
        player_list = []
        #  Pretend a player joins
        player_1 = Player()
        player_1.set_id("Player 1")
        player_list = [player_1]
        self.Dealer.start_round(player_list)