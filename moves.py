class Moves:
    def __init__(self):
        pass

    def chain_move(self, numbers):

        # CHAIN MOVE

        correct_order_chain = True

        # Iterieren durch die Liste
        for i in range(len(numbers) - 1):
            # Überprüfen, ob die aktuelle Zahl um 1 größer als die vorherige ist
            if numbers[i + 1] != numbers[i] + 1:
                correct_order_chain = False
                break
        if correct_order_chain:
            return True

    def group_move(self, numbers, colors):

        # GROUP MOVE
        # check if there are any doubles
        correct_order_group = True

        for item in colors:
            if colors.count(item) > 1:
                correct_order_group = False
                break

        group_number = numbers[0]

        for i in range(len(numbers)):
            if group_number != numbers[i]:
                correct_order_group = False
                break

        if correct_order_group:
            return True