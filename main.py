# This is a sample Python script.
# Press Umschalt+F10 to execute it or replace it with your code.
import math
import random


# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# ---------------------Aufgabe 1 ------------------------------------
def compute_r2d2_population(steps: int) -> tuple[int, int, int]:
    step = 0
    young = 10
    middle = 10
    old = 10

    while step < steps:
        to_middle = math.floor(young / 2)
        to_old = math.floor(middle / 3)
        to_young = middle * 4 + old * 2

        young = to_young
        middle = to_middle
        old = to_old

        step += 1

    return young, middle, old


# ---------------------Aufgabe 2 Streichholz------------------------------
# IMPLEMENT YOUR SOLUTION FOR THE STEICHHOLZSPIEL HERE
def matches_game():
    matches = 31

    while matches > 1:
        if matches % 7 == 0:
            computer_turn = random.randint(1, 6)
        else:
            computer_turn = (matches % 7) - 1
        if computer_turn == 0:
            computer_turn = 1

        print("Spieler A nimmt", computer_turn, "Streichhölzer.")
        matches -= computer_turn
        print("Es verbleiben:", matches, "Streichhölzer.")

        if matches == 1:
            print("Spieler B (Sie) müssen das letzte Streichholz nehmen und haben daher verloren.")
            break

        user_turn = int(input("Geben Sie an, wie viele Streichhölzer Sie nehmen möchten (1 bis 6): "))
        while user_turn < 1 or user_turn > 6 or user_turn > matches:
            user_turn = int(input(
                "Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und 6 und stellen Sie sicher, dass sie nicht größer ist als die verbleibende Anzahl von Streichhölzern: "))

        matches -= user_turn
        print("Es verbleiben:", matches, "Streichhölzer.")

    print("Spiel beendet.")


# ---------------------Aufgabe 3 Heron ------------------------------------
def heron_verfahren(area: float, threshold: float) -> float:
    """
        computes the square root using the heron method
    :param area: size of the area e.g.25
    :param threshold: threshold for the heron method e.g. 0.01
    :return:the square root of the given area according to the heron method
    """

    return 0


# ---------------------Aufgabe 4 Quersumme------------------------------
# IMPLEMENT, IF NECESSARY, EXERCISE 4 HERE BUT USE A FUNCTION!


# ---------------MANAGEMENT----------------------
# -------------COMMENT/UNCOMMENT lines to launch the different exercises
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("You need to adjust this code to run your implementation")

    # Aufgabe 1
    # print(f"""
    # R2D2 Population after 5 steps is:
    # Young: {compute_r2d2_population(5)[0]}
    # Adults: {compute_r2d2_population(5)[1]}
    # Old: {compute_r2d2_population(5)[2]}""")
    # print (compute_r2d2_population(5))

    # Aufgabe 2
    print(matches_game())

    # Aufgabe 3
    # print(f"Die Wurzel für die Fläche 25 und Grenze 0.01 nach Heron ist: {heron_verfahren(25, 0.01)}")

    # Aufgabe 4
    # TO BE IMPLEMENTED

    # Use a breakpoint in the code line below to debug your script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
