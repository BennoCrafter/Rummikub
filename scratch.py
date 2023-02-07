# Liste von Zahlen
numbers = [3, 4, 5, 6]
input_numbers = input("Enter your numbers please and split by  : ").split(":")
input_numbers = list(map(int, input_numbers))

for item in input_numbers:
    numbers.append(item)

numbers.sort()

# Flag für korrekte Reihenfolge
correct_order = True

# Iterieren durch die Liste
for i in range(len(numbers) - 1):
    # Überprüfen, ob die aktuelle Zahl um 1 größer als die vorherige ist
    if numbers[i + 1] != numbers[i] + 1:
        correct_order = False
        break

# Ausgabe des Ergebnisses
if correct_order:
    print("Die Zahlen sind in korrekter Reihenfolge ohne Lücken.")
else:
    print("Die Zahlen sind nicht in korrekter Reihenfolge oder es gibt Lücken.")
