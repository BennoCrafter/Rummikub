import random
from card import Cards


class Player:
    def __init__(self):
        # load all cards
        cards = Cards()
        cards.get_all_cards()
        self.all_cards = cards.all_cards

        self.players = 1
        self.player_cards = []
        self.dev_mode = True
        self.remained_cards = self.all_cards.copy()
        
    def spread_cards(self):
        self.remained_cards = self.all_cards.copy()
        for i in range(14):
            random_choice = random.choice(self.remained_cards)
            self.player_cards.append(random_choice)
            self.remained_cards.remove(random_choice)
            
        self.player_cards.sort()


if __name__ == "__main__":
    player_object = Player()
