class GUI:
    def __init__(self):
        # colors
        self.red = "\033[31m"
        self.green = "\033[92m"
        self.yellow = "\033[93m"
        self.orange = "\033[33m"
        # reset color
        self.reset = "\033[0m"

    def printing_cards(self, chains, groups, counter):
        for i in range(len(chains)):
            print("\n")
            print(counter, chains[i])
            counter += 1

        for i in range(len(groups)):
            print("\n")
            print("\t\t", counter, groups[i])
            counter += 1
        print("\n")

    def make_cards_pretty(self):
        pass


if __name__ == "__main__":
    gui_object = GUI()
