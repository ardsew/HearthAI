import Deck


class Player:

    def __init__(self, deck: Deck):
        self.mana = 0
        self.hand = None
        self.deck = deck
        self.graveyard = None
        self.board = None
        self.player_class = deck.player_class
        self.fatigue = 0
        self.health = 30

    def perform_action(self):
        queue = []
        return queue

    def end_turn(self):
        pass

    def shuffle_deck(self):
        self.deck.shuffle()

    def draw_card(self):
        if self.deck:
            card_drawn = self.deck.pop()

            if len(self.hand) < 10:
                self.hand.append(card_drawn)
        else:
            self.fatigue += 1
            self.health -= self.fatigue
    