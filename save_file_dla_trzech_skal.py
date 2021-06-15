

def zapisz(table_1, table_2, table_3, title):

    with open(f"{title}.txt", "w") as f:
        f.write("x,y\n")

        f.write("lupek\n")
        for i in range(len(table_1[0])):
            f.write(str(round(table_1[0][i], 2)) + "," + str(round(table_1[1][i], 2)) + "\n")

        f.write("piaskowiec\n")
        for i in range(len(table_2[0])):
            f.write(str(round(table_2[0][i], 2)) + "," + str(round(table_2[1][i], 2)) + "\n")

        f.write("dolomit\n")
        for i in range(len(table_3[0])):
            f.write(str(round(table_3[0][i], 2)) + "," + str(round(table_3[1][i], 2)) + "\n")

