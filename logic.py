from player import Player
from card import Cards
from GUI import GUI
from moves import Moves

import random


class Logic:
    def __init__(self):
        # load the cards from the player
        self.player_object = Player()
        self.gui_object = GUI()
        self.move_object = Moves()
        self.cards = Cards()

        self.player_object.spread_cards()
        self.player_cards = self.player_object.player_cards

        self.colors = []
        self.numbers = []
        self.groups = []
        self.chains = []
        self.table_table = []
        self.move = ""
        self.player_input_pretty = ""
        self.counter = 0

        self.commands = {"skip": self.pull_card,
                         "put": self.put_card,
                         "expand": self.expand,
                         "show table": self.show_table,
                         "get card": self.cheat_card,
                         "exit": "PLACEHOLDER",
                         "commands": "PLACEHOLDER"}

        self.instruction = "Anleitung:\n\t[skip](ziehe Karte)|[put](lege Reihe oder Gruppe. Format:FARBE,NUMMER + ; + nächste FARBE,NUMMER)||[expand](lege etwas an)||[exit]"
        print("Wilkommen bei Rummikub!")
        print(self.instruction)
        self.gui_object.make_cards_pretty()
        print("Bitte benutze folgendes Format:\nFARBE;NUMMER")

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
        if not self.player_cards:
            print("Player", player, "has won!")
            exit()
        print("Deine Karten sind:", self.player_cards)
        self.player_input = input("Schritt:")
        self.is_input_correct()

    def pull_card(self):
        print("\n")
        random_choice = random.choice(self.player_object.remained_cards)
        self.player_cards.append(random_choice)
        self.player_object.remained_cards.remove(random_choice)
        print("Neue Karte:", random_choice)
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
            if len(self.player_input) >= 3:
                for m in range(len(self.player_input)):
                    if self.colors[m] not in self.cards.colors_list or self.numbers[m] not in self.cards.numbers_list:
                        self.is_correct = False
            else:
                print("Deine Kette ist zu kurz!")
                self.is_correct = False

            if self.is_correct:
                self.is_correct = True
                for card in self.player_input_pretty:
                    if card not in self.player_cards:
                        self.is_correct = False
                        print("Du besitzt deine eingegebene Karten nicht!")
                        break
            if self.is_correct:
                self.logic()
            else:
                print("Deine Reihnfolge ist zu kurz/lang oder die Farbe bzw. Nummer exestiert nicht.")
                self.game_loop()
        except ValueError:
            if self.player_input[0] != "back":
                print("Bitte benutze das richtige Format:\nFARBE,NUMMER + ; + nächste FARBE,NUMMER")
                self.put_card()
            else:
                self.game_loop()

    def expand(self):

        colors = []
        numbers = []
        player_numbers = []
        player_colors = []
        correct = True

        self.player_input = int(input("An welche Kette willst du was hinzufügen?:"))
        pos = self.player_input
        if self.table_table:
            if pos <= len(self.table_table):
                expand_part = self.table_table[pos]
                print(expand_part)
                # split data
                for i in range(len(expand_part)):
                    color, number = expand_part[i].split(",")
                    colors.append(color)
                    numbers.append(number)

                numbers = list(map(int, numbers))
                print(numbers)
                formated_input_for_index = ""
                for i, z in enumerate(numbers):
                    formated_input_for_index += f"{colors[i]},{z}|"
                formated_input_for_index = formated_input_for_index.split("|")
                formated_input_for_index.pop(-1)
        else:
            print("Diese Kette exestiert nicht!")

        # check if it's a chain or group
        if self.move_object.chain_move(numbers=numbers):
            self.player_input = input("Was willst du zur Kette hinzufügen?:")
            # split data
            self.player_input = self.player_input.split(";")
            for i in range(len(self.player_input)):
                player_color, player_number = self.player_input[i].split(",")
                player_colors.append(player_color)
                player_numbers.append(player_number)
            player_numbers = list(map(int, player_numbers))
            # add numbers from player to certain line from table and sort it
            for item in player_numbers:
                numbers.append(item)
            numbers.sort()
            print(numbers)
            correct_order = True

            # Iterieren durch die Liste
            for i in range(len(numbers) - 1):
                # Überprüfen, ob die aktuelle Zahl um 1 größer als die vorherige ist
                if numbers[i + 1] != numbers[i] + 1:
                    correct_order = False
                    break

            if correct_order:
                print(self.chains)
                new_formated_input_for_index = ""
                for i in numbers:
                    new_formated_input_for_index += f"{player_color},{i}|"
                new_formated_input_for_index = new_formated_input_for_index.split("|")
                index = self.chains.index(formated_input_for_index)
                self.chains.insert(index, new_formated_input_for_index)
                self.table_table.append(new_formated_input_for_index)

            self.show_table()

        elif self.move_object.group_move(numbers=numbers, colors=colors):
            pass

    def is_input_correct(self):
        self.is_correct = True
        self.colors = []
        self.numbers = []
        if self.player_input in self.commands.keys():
            # check if it's a special command
            if self.player_input == "commands":
                print(f"The current commands are: {list(self.commands.keys())}")
            elif self.player_input == "exit":
                print("Bis zum nächsten mal!")
                exit()
            else:
                self.commands[self.player_input]()
        else:
            print(self.instruction)

        self.game_loop()

    def table(self):
        pass

    def logic(self):
        if self.move_object.group_move(numbers=self.numbers, colors=self.colors):
            print("Du hast erfolgreich eine Gruppe gebildet!")

            for i in range(len(self.player_input_pretty)):
                self.player_cards.remove(self.player_input[i])

            self.groups.append(self.player_input_pretty)
            self.table_table.append(self.player_input_pretty)

        elif self.move_object.chain_move(numbers=self.numbers):
            print("Du hast erfolgreich eine Reihe gebildet!")

            for i in range(len(self.player_input_pretty)):
                self.player_cards.remove(self.player_input[i])

            self.chains.append(self.player_input_pretty)
            self.table_table.append(self.player_input_pretty)

        else:
            print("Du hast keine sinnvole Reihe oder Gruppe gebildet!")

        self.gui_object.printing_cards(chains=self.chains, groups=self.groups, counter=self.counter)
        self.game_loop()

    def next_number(self, numbers, color, pos, input_number):
        if input_number < 13 and input_number == numbers[-1] + 1:
            return True

        elif input_number == 13:
            v = color + "," + str(input_number)
            self.table_table[pos].append(v)
            self.gui_object.printing_cards(chains=self.chains, groups=self.groups, counter=self.counter)
        else:
            print("Some Error!")

    def show_table(self):
        self.gui_object.printing_cards(chains=self.chains, groups=self.groups, counter=self.counter)

    def cheat_card(self):
        self.player_cards.append(input("Enter card:"))


if __name__ == "__main__":
    logic_object = Logic()
    logic_object.split_cards()
    logic_object.game_loop()
