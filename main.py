# This is a sample Python script.
# Press Umschalt+F10 to execute it or replace it with your code.

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# ---------------------Aufgabe 1 ------------------------------------
def compute_r2d2_population(steps: int) -> tuple[int, int, int]:
    """
        Computes the r2d2 population for the given step amount
    :param steps: amount of steps to compute the population (e.g.: 5)
    :return: tuple of childs adults and old r2d2
    """
    return (0, 0, 0)


# ---------------------Aufgabe 2 Streichholz------------------------------
# IMPLEMENT YOUR SOLUTION FOR THE STEICHHOLZSPIEL HERE
def streich_holz_spiel():
    text = "Geben sie an wie viele Streichhölzer sie nehmen, eine Zahl von 1 bis 6"
    streichhölzer = 31
    round_1 = 2

    print("Spieler A nimmt", round_1, "Streichhölzer")
    streichhölzer = streichhölzer - round_1
    print("Es verbleiben:", streichhölzer, "Streichölzer")

    round_2 = int(input(text))
    streichhölzer = streichhölzer - round_2
    print("Es verbleiben:", streichhölzer, "Streichhölzer")

    seven = 7
    rounds = 3
    round_4 = 0

    while rounds <= 6:
        if rounds == 1:
            round_3 = seven - round_2
            print("Spieler A nimmt", round_3, "Streichhölzer")
            streichhölzer = streichhölzer - round_3
            print("Es verbleiben:", streichhölzer, "Streichhölzer")

        elif rounds == 2:
            round_4 = int(input(text))
            streichhölzer = streichhölzer - round_4
            print("Es verbleiben:", streichhölzer, "Streichhölzer")

        elif rounds == 3:
            round_5 = seven - round_4
            print("Spieler A nimmt", round_5, "Streichhölzer")
            streichhölzer = streichhölzer - round_5
            print("Es verbleiben:", streichhölzer, "Streichhölzer")

        else:
            round_6 = int(input(text))
            streichhölzer = streichhölzer - round_6
            print("Es verbleiben:", streichhölzer, "Streichhölzer")

        rounds = rounds + 1

    print("Es verbleiben:", streichhölzer, "Streichhölzer")


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
    print(streich_holz_spiel())

    # Aufgabe 3
    # print(f"Die Wurzel für die Fläche 25 und Grenze 0.01 nach Heron ist: {heron_verfahren(25, 0.01)}")

    # Aufgabe 4
    # TO BE IMPLEMENTED

    # Use a breakpoint in the code line below to debug your script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
