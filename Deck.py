import random


class Deck:
    def __init__(self, player_class, deck=[]):
        self.size = 0
        self.deck = deck
        self.player_class = player_class
    
    def add_card(self, card):
        pass

    def draw_card(self):
        pass

    def shuffle(self):
        random.shuffle(self.deck)  # in-place