
def zapisz(table: list, krotka_kolumn: tuple, title):
    with open(f"{title}.txt", "w") as f:
        f.write(f"{krotka_kolumn[0]},{krotka_kolumn[1]}\n")
        for i in range(len(table[0])):
            f.write(str(round(table[0][i], 2)) + "," + str(round(table[1][i], 2)) + "\n")