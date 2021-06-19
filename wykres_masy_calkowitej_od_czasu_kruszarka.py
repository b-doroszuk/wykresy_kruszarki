import time
import save_file

from edempy import Deck
import numpy as np
from edempy import BoxBin, CylinderBin
import matplotlib.pyplot as plt
import matplotlib; matplotlib.use("TkAgg")






def get_data(time_step_list: list, deck: object):

    mass_array = []  # y
    timestep_array = []  # x

    for i in range(time_step_list[0], time_step_list[1], time_step_list[2]):
        print(f"krok czasowy: {i}")
        rock_mass = 0
        dummy_mass = 0

        # mass_lupek
        rock_mass += sum(list(deck.timestep[i].particle[0].getMass()))
        # mass_piaskowiec
        rock_mass += sum(list(deck.timestep[i].particle[1].getMass()))
        # mass_dolomit
        rock_mass += sum(list(deck.timestep[i].particle[2].getMass()))

        # dummy_mass_lupek
        try:
            dummy_mass += sum(list(deck.timestep[i].particle[3].getMass()))
        except Exception:
            continue
        # dummy_mass_piaskowiec
        try:
            dummy_mass += sum(list(deck.timestep[i].particle[4].getMass()))
        except Exception:
            continue
        # dummy_mass_dolomit
        try:
            dummy_mass += sum(list(deck.timestep[i].particle[5].getMass()))
        except Exception:
            continue

        total_mass = rock_mass + dummy_mass
        timestep_array.append(round(float(deck.timestepKeys[i]), 2))
        mass_array.append(round(total_mass, 4))

    return timestep_array, mass_array

def draw_graph(x, y, is_save=True, is_draw=False):
    fig = plt.figure(figsize=(7, 6))
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    axes.plot(x, y)
    #plt.title(f'wydajnosc od czasu')
    plt.xlabel('Czas [s]')
    plt.ylabel('Masa w układzie [kg]')

    plt.xlim([0, 20])
    plt.ylim([0, 250])

    if is_save:
        plt.savefig(f"wydajnosc_od_czasu__{time.strftime('%m_%d_%Y-%H_%M_%S')}.png")

    if is_draw:
        plt.show()


def main():
    """

    parametry wejsciowe:
    interval_table  = [poczatkowy krok, koncowy krok czasowy, interwal],
    filepath        = sciezka
    is_export       = czy exportowac do txt (True / False)

    """
    interval_table = [1, 2000, 10]
    filepath = "E:\\Etap2_Polkowice\\simulation_0\\simulation_0.dem"
    is_export = True

    # All bellow treat as black-box
    start = time.time()
    deck = Deck(filepath)
    timestep_array, mass_array = get_data(interval_table, deck=deck)

    print(mass_array)
    print(timestep_array)
    draw_graph(timestep_array, mass_array)

    if is_export:
        save_file.zapisz([timestep_array, mass_array], ("czas", "masa"), "export_masa_calkowita_od_czasu_kruszarka_" + str(time.strftime('%m_%d_%Y-%H_%M_%S')))

    koniec = time.time()
    print("czas: ", koniec - start)


if __name__ == '__main__':
    import sys
    sys.exit(main())


