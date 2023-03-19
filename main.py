from random import randint
import matplotlib.pyplot as plt


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self, die_number):
        results = 0
        for __ in range(die_number):
            amount = randint(1, self.num_sides)
            results += amount
        return results


def collecting_data():
    amount_of_dies = int(input("Jak wieloma kostkami chcesz rzucić?: "))
    amount_of_throws = int(input(f"Ile razy chcesz rzucić {amount_of_dies} kostkami?: "))
    return amount_of_dies, amount_of_throws


def main():
    die = Die()
    results, frequencies = [], []
    amount_of_dies, throws = collecting_data()
    numbers = [f'{number}' for number in range(amount_of_dies, amount_of_dies * die.num_sides + 1)]
    colors = ['green', 'blue', 'purple', 'brown', 'teal']

    for __ in range(throws):
        result = die.roll(amount_of_dies)
        results.append(result)

    for value in range(amount_of_dies, amount_of_dies * die.num_sides + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    dice_throws = frequencies
    plt.bar(numbers, dice_throws, color=colors)
    plt.title(f'Ilość wystąpień danej liczby przy rzucie {amount_of_dies} kostką/ami {throws} razy', fontsize=14)
    plt.xlabel('Liczba', fontsize=17)
    plt.ylabel('Ilość wystąpień', fontsize=14)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()


