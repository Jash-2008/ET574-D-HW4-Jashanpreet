# Name: Jashanpreet Kaur
# QCC ID:24648806
# ET574 Homework 4 - Dice Game Simulator

import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class DiceGame:
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def evaluate_roll(self, total):
        if total in [7, 11]:
            return "Win"
        elif total in [2, 3, 12]:
            return "Lose"
        else:
            return "Roll Again"

    def play_round(self):
        roll1 = self.die1.roll()
        roll2 = self.die2.roll()

        total = roll1 + roll2
        result = self.evaluate_roll(total)

        return roll1, roll2, total, result


def main():
    game = DiceGame()

    while True:
        print("\n===== DICE GAME =====")
        print("1. Play a round")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll1, roll2, total, result = game.play_round()

            print("\nDie 1:", roll1)
            print("Die 2:", roll2)
            print("Total:", total)
            print("Result:", result)

        elif choice == "2":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
