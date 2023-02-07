class Cards:
    def __init__(self):
        self.numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.colors_list = ["rot", "orange", "gelb", "grün"]
        self.all_cards = []

    def get_all_cards(self):
        for z in range(len(self.colors_list)):
            for i in range(len(self.numbers_list)):
                self.all_cards.append(self.colors_list[z] + "," + str(self.numbers_list[i]))
                self.all_cards.append(self.colors_list[z] + "," + str(self.numbers_list[i]))


if __name__ == "__main__":
    cards_object = Cards()
    cards_object.get_all_cards()
