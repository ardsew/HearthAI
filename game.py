import Player
import random


class Game:

    def __init__(self, p1: Player, p2: Player):
        self.p1 = p1
        self.p2 = p2

    def start_game(self):
        self.p1.shuffle_deck()
        self.p2.shuffle_deck()
        self.round_start(self.p1)
        self.round_start(self.p2)
        
    def round_start(self, player):
        player.mana = min(player.mana+1, 10)
        player.draw_card()


