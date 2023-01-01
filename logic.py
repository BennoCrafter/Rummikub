from player import Player
from card import Cards
from GUI import GUI
import random


class Logic:
    def __init__(self):
        # load the cards from the player
        self.player_object = Player()
        self.cards = Cards()
        self.player_object.spread_cards()
        self.player_cards = self.player_object.player_cards
        self.gui_object = GUI()

        self.colors = []
        self.numbers = []
        self.move = ""
        self.player_input_pretty = ""
        self.groups = []
        self.chains = []
        self.counter = 0
        self.table_table = []


        print("Wilkommen bei Rummikub!")
        print("Anleitung:")
        print("[skip](ziehe Karte)|[put](lege Reihe oder Gruppe. Format:FARBE,NUMMER + ; + nächste FARBE,NUMMER)||[expand](lege etwas an)||[exit]")
        self.gui_object.make_cards_pretty()
        print("Bitte benutze folgendes Format:\nFARBE;NUMMER")
        self.game_loop()


    def split_cards(self):
        splitted_player_cards = []
        numbers = []
        colors = []

        for i in range(len(self.player_cards)):
            splitted_player_cards += self.player_cards[i].split(",")

        for i, element in enumerate(splitted_player_cards):
            # If index of the element is even (i.e. 0, 2, 4, etc.), append it
            if i % 2 == 0:
                colors.append(element)
            # If index of the element is odd (i.e. 1, 3, 5, etc.), append it
            else:
                numbers.append(element)


    def game_loop(self):
        player = 1
        self.player_cards.sort()
        if self.player_cards == []:
            print("Player",player,"has won!")
            exit
        print("Deine Karten sind:", self.player_cards)
        self.player_input = input("Schritt:")
        self.is_input_correct()


    def pull_card(self):
        print("\n")
        random_choice = random.choice(self.player_object.remained_cards)
        self.player_cards.append(random_choice)
        self.player_object.remained_cards.remove(random_choice)
        print("Neue Karte:",random_choice)
        self.game_loop()


    def put_card(self):
        self.player_input = input("Was willst du legen?")
        try:
            self.player_input = self.player_input.split(";")
            self.player_input_pretty = self.player_input.copy()
            for i in range(len(self.player_input)):
                color, number = self.player_input[i].split(",")
                self.colors.append(color)
                self.numbers.append(number)
            self.numbers = list(map(int, self.numbers))
            if len(self.player_input) <= 3:
                for m in range(len(self.player_input)):
                    if self.colors[m] not in self.cards.colors_list or self.numbers[m] not in self.cards.numbers_list:
                        self.is_correct = False
            if self.is_correct:
                self.is_correct = True
                for i in range(len(self.player_input_pretty)):
                    if self.player_input_pretty[i] not in self.player_input_pretty:    
                        self.is_correct = False
                        print("Du hast deine eingegebene Karten nicht!")
                        break
            if self.is_correct:
                self.logic()
            else:
                print("Deine Reihnfolge ist zu kurz/lang oder die Farbe bzw. Nummer exestiert nicht.")
                self.game_loop()
        except ValueError:

            print("Bitte benutze das richtige Format:\nFARBE,NUMMER + ; + nächste FARBE,NUMMER")
            self.game_loop()


    def expand(self):
        # replace something with the list element player_input groups or chains
        
        colors = []
        numbers = []

        self.player_input = int(input("An welche Kette willst du was hinzufügen?:"))
        expand_part = self.table_table[self.player_input]
        print(expand_part)
        # split data
        for i in range(len(expand_part)):
            color, number = expand_part[i].split(",")
            colors.append(color)
            numbers.append(number)

    def is_input_correct(self):
        self.is_correct = True
        self.colors = []
        self.numbers = []

        if self.player_input.startswith("skip"):
            self.pull_card()

        elif self.player_input.startswith("put"):
            self.put_card()
            
        elif self.player_input.startswith("expand"):
            self.expand()

        elif self.player_input.startswith("exit"):
            print("Bis zum nächsten mal!")
            exit()
        else:
            print("Anleitung:")
            print("[skip](ziehe Karte)|[put](lege Reihe oder Gruppe. Format:FARBE,NUMMER + ; + nächste FARBE,NUMMER)||[expand](lege etwas an)||[exit]")


    def chain_move(self):
                
        # CHAIN MOVE

        correct_order_chain = True

        # Iterieren durch die Liste
        for i in range(len(self.numbers) - 1):
        # Überprüfen, ob die aktuelle Zahl um 1 größer als die vorherige ist
            if self.numbers[i + 1] != self.numbers[i] + 1:
                correct_order_chain = False
                break
        if correct_order_chain:
            return True

    def group_move(self):
             
        # GROUP MOVE
        # check if there are any doubles
        correct_order_group = True

        for item in self.colors:
            if self.colors.count(item) > 1:
                correct_order_group = False
                break


        group_number = self.numbers[0]

        for i in range(len(self.numbers)):
            if group_number != self.numbers[i]:
                correct_order_group = False
                break
        
        if correct_order_group:
            return True

    def table(self):
        pass


    def logic(self):

        # check correct order
        if self.chain_move():
            self.move = "chain"
        elif self.group_move:
            self.move = "group"
        else:
            self.move = "None"

        self.get_answer()

    def get_answer(self):
        if self.move == "group":
            print("Du hast erfolgreich eine Gruppe gebildet!")
            for i in range(len(self.player_input_pretty)):
                self.player_cards.remove(self.player_input[i])
            self.groups.append(self.player_input_pretty)
            self.table_table.append(self.player_input_pretty)

        elif self.move == "chain":
            print("Du hast erfolgreich eine Reihe gebildet!")
            for i in range(len(self.player_input_pretty)):
                self.player_cards.remove(self.player_input[i])
            self.chains.append(self.player_input_pretty)
            self.table_table.append(self.player_input_pretty)

        else:
            print("Du hast keine sinnvole Reihe oder Gruppe gebildet!")

        self.gui_object.printing(chains=self.chains,groups=self.groups,counter=self.counter)
        self.game_loop()


if __name__ == "__main__":
    logic_object = Logic()
    logic_object.split_cards()
