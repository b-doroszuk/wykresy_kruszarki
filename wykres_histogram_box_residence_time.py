import matplotlib.pyplot as plt
import numpy as np
import time
from time import strftime
from edempy import BoxBin, Deck
import edempy
import matplotlib; matplotlib.use("TkAgg")


def maintance_time(interval_table: list, L_boxbin, R_boxbin, deck, is_draw: bool, is_save: bool):
    #'ResidenceTime_Example.dem')
    #deck = Deck(deck_name)
    nTimesteps = deck.numTimesteps    # liczba krokow czasowych
    print("liczba krokow czasowych: ", nTimesteps)
    binbox_name = "123"


    # Step 1: Define size of a single timestep and bin x, y, z max/min
    tstep = deck.timestep[1].timestep  # Size of a single timestep

    # Step 2: Create empty dict to count pID residence time
    insideBin = {}  # Use dict for speed {pID:count}

    for i in range(interval_table[0], interval_table[1]):
        print("krok czasowy: ", i)
        # Step 3: Loop ids per timestep, if particle is inside bin add to the count in "insideBin"
        for j in range(3):  # iteracja po wszystkich skalach
            ids = deck.timestep[i].particle[j].getIds()
            pos = deck.timestep[i].particle[j].getPositions()
            p_ids_first_bin = L_boxbin.getBinnedObjects(ids, pos)
            p_ids_second_bin = R_boxbin.getBinnedObjects(ids, pos)

            for p_id in p_ids_first_bin:
                if p_id in insideBin:
                    insideBin[p_id] = insideBin[p_id] + 1  # If already in dict add 1 to the count
                else:
                    insideBin.update({p_id: 1})  # If not in the dict, add it, and add 1 to the count

            for p_id in p_ids_second_bin:
                if p_id in insideBin:
                    insideBin[p_id] = insideBin[p_id] + 1  # If already in dict add 1 to the count
                else:
                    insideBin.update({p_id: 1})  # If not in the dict, add it, and add 1 to the count

    # Step 5: Plot data as a histogram
    residenceTime = np.array(list(insideBin.values())) * tstep
    plt.hist(residenceTime, 11)
    plt.xlabel('Residence Time [s]')
    plt.ylabel('Frequency')
    plt.title(f'Residence Time Histogram where particle in {binbox_name} BinBox')
    if is_save:
        plt.savefig(f"Residence_Time_{binbox_name}_BinBox_{strftime('%m_%d_%Y-%H_%M_%S')}.png")
    if is_draw:
        plt.show()

def main():
    """
    Main function

    parametry wejsciowe:
    interval_table  = [poczatkowy krok, koncowy krok czasowy],
    list_section    = [20, 30, 40, 50, 60, 80] - od 5 do 10 elementow,
    filepath        = sciezka
    L_boxbin            = wymiary boxa np. BoxBin([0, -0.8, -0.75], 3, 0.25, 1.5)
    R_boxbin            = -||-
    id_draw         = czy rysowac (True / False)
    is_save         = czy zapisac (True / False)
    """

    interval_table = [1, 260]
    filepath = "C:\\Users\\Jakub\\PycharmProjects\\test2\\testownik11_prof_Robert_Krol\\projekt_2\\POLKOWICE_etap_2\\simulation_0\\simulation_0.dem"
    L_boxbin = BoxBin([0, -0.8, -0.75], 3, 0.25, 1.5)
    R_boxbin = BoxBin([0, 0.8, -0.75], 3, 0.25, 1.5)
    is_draw = True
    is_save = False

    deck = Deck(filepath)

    maintance_time(interval_table=interval_table, L_boxbin=L_boxbin, R_boxbin=R_boxbin,
                   deck=deck, is_draw=is_draw, is_save=is_save)

if __name__ == '__main__':
    import sys

    sys.exit(main())
