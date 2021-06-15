from edempy import Deck
import numpy as np
from edempy import BoxBin, CylinderBin
import matplotlib.pyplot as plt
import matplotlib; matplotlib.use("TkAgg")
from time import strftime


def get_mass_time_box(time_step: int, deck, L_boxbin, R_boxbin):

    # zamienia krok czasowy na jednostke czasu
    czas = deck.timestepKeys[time_step]

    # zmienne do przechowywania masy
    mass_lupek = 0
    mass_piaskowiec = 0
    mass_dolomit = 0

    mass_dummy_lupek = 0
    mass_dummy_piaskowiec = 0
    mass_dummy_dolomit = 0

    """LUPEK"""
    binned_ids_L0_lupek = L_boxbin.getBinnedObjects(deck.timestep[time_step].particle[0].getIds(),
                                                    deck.timestep[time_step].particle[0].getPositions())

    binned_ids_R0_lupek = R_boxbin.getBinnedObjects(deck.timestep[time_step].particle[0].getIds(),
                                                    deck.timestep[time_step].particle[0].getPositions())
    # dummy lupek

    binned_ids_L0_dummy_lupek = L_boxbin.getBinnedObjects(
                                deck.timestep[time_step].particle[3].getIds(),
                                deck.timestep[time_step].particle[3].getPositions())

    binned_ids_R0_dummy_lupek = R_boxbin.getBinnedObjects(
                                deck.timestep[time_step].particle[3].getIds(),
                                deck.timestep[time_step].particle[3].getPositions())
        # lupek loop
    for i in binned_ids_L0_lupek:
        mass_lupek += deck.timestep[time_step].particle[0].getMass(id=i)
    for i in binned_ids_R0_lupek:
        mass_lupek += deck.timestep[time_step].particle[0].getMass(id=i)
        # dummy lupek loop
    for i in binned_ids_L0_dummy_lupek:
        mass_dummy_lupek += deck.timestep[time_step].particle[3].getMass(id=i)
    for i in binned_ids_R0_dummy_lupek:
        mass_dummy_lupek += deck.timestep[time_step].particle[3].getMass(id=i)



    """PIASEK"""
    binned_ids_L1_piaskowiec = L_boxbin.getBinnedObjects(deck.timestep[time_step].particle[1].getIds(),
                                                         deck.timestep[time_step].particle[1].getPositions())
    binned_ids_R1_piaskowiec = R_boxbin.getBinnedObjects(deck.timestep[time_step].particle[1].getIds(),
                                                         deck.timestep[time_step].particle[1].getPositions())
    binned_ids_L0_dummy_piaskowiec = L_boxbin.getBinnedObjects(
                                    deck.timestep[time_step].particle[4].getIds(),
                                    deck.timestep[time_step].particle[4].getPositions())

    binned_ids_R0_dummy_piaskowiec = R_boxbin.getBinnedObjects(
                                    deck.timestep[time_step].particle[4].getIds(),
                                    deck.timestep[time_step].particle[4].getPositions())
    # piaskowiec loop
    for i in binned_ids_L1_piaskowiec:
        mass_piaskowiec += deck.timestep[time_step].particle[1].getMass(id=i)
    for i in binned_ids_R1_piaskowiec:
        mass_piaskowiec += deck.timestep[time_step].particle[1].getMass(id=i)
        # dummy piaskowiec loop
    for i in binned_ids_L0_dummy_piaskowiec:
        mass_dummy_piaskowiec += deck.timestep[time_step].particle[4].getMass(id=i)
    for i in binned_ids_R0_dummy_piaskowiec:
        mass_dummy_piaskowiec += deck.timestep[time_step].particle[4].getMass(id=i)



    """DOLOMIT"""
    binned_ids_L2_dolomit = L_boxbin.getBinnedObjects(deck.timestep[time_step].particle[2].getIds(),
                                              deck.timestep[time_step].particle[2].getPositions())
    binned_ids_R2_dolomit = R_boxbin.getBinnedObjects(deck.timestep[time_step].particle[2].getIds(),
                                              deck.timestep[time_step].particle[2].getPositions())

    binned_ids_L0_dummy_dolomit = L_boxbin.getBinnedObjects(
                                    deck.timestep[time_step].particle[5].getIds(),
                                    deck.timestep[time_step].particle[5].getPositions())

    binned_ids_R0_dummy_dolomit = R_boxbin.getBinnedObjects(
                                    deck.timestep[time_step].particle[5].getIds(),
                                    deck.timestep[time_step].particle[5].getPositions())
    # dolomit loop
    for i in binned_ids_L2_dolomit:
        mass_dolomit += deck.timestep[time_step].particle[2].getMass(id=i)
    for i in binned_ids_R2_dolomit:
        mass_dolomit += deck.timestep[time_step].particle[2].getMass(id=i)

    # dummy dolomit loop
    for i in binned_ids_L0_dummy_dolomit:
        mass_dummy_dolomit += deck.timestep[time_step].particle[5].getMass(id=i)
    for i in binned_ids_R0_dummy_dolomit:
        mass_dummy_dolomit += deck.timestep[time_step].particle[5].getMass(id=i)

    #print()
    #print(mass_lupek, mass_piaskowiec, mass_dolomit)
    #print(mass_dummy_lupek, mass_dummy_piaskowiec, mass_dummy_dolomit)
    #print()

    rock_mass = mass_lupek + mass_piaskowiec + mass_dolomit
    dummy_mass = mass_dummy_lupek + mass_dummy_piaskowiec + mass_dummy_dolomit
    total_mass = rock_mass + dummy_mass

    #print(rock_mass, dummy_mass)
    # zwraca mase calkowita i czas w sekundach !!
    return total_mass, czas


def main():
    """

    parametry wejsciowe:
    interval_table      = [poczatkowy krok, koncowy krok czasowy, interwal],
    filepath            = sciezka
    L_boxbin            = wymiary boxa np. BoxBin([0, -0.8, -0.75], 3, 0.25, 1.5)
    R_boxbin            = -||-
    is_export           = czy exportowac do txt (True / False)
    is_draw             = czy rysowac wykres (True / False)
    is_save             = czy zapisac wykres (True / False)

        PONIZEJ 68 KROKU CZASOWEGO SKRYPT WYWALA BLAD !!!
    """
    interval_table = [68, 260, 10]
    filepath = "C:\\Users\\Jakub\\PycharmProjects\\test2\\testownik11_prof_Robert_Krol\\projekt_2\\POLKOWICE_etap_2\\simulation_0\\simulation_0.dem"
    L_boxbin = BoxBin([0, -0.8, -0.75], 3, 0.25, 1.5)
    R_boxbin = BoxBin([0, 0.8, -0.75], 3, 0.25, 1.5)
    is_draw = True
    is_save = False


    deck = Deck(filepath)
    mass_list = []
    time = []

    for i in range(interval_table[0], interval_table[1], interval_table[2]):
        print("krok czasowy: ", i)
        total_mass, czas = get_mass_time_box(time_step=i, deck=deck, L_boxbin=L_boxbin, R_boxbin=R_boxbin)
        mass_list.append(round(total_mass, 2))
        time.append(round(float(czas), 2))

    fig = plt.figure(figsize=(7, 6))
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    # rysuje wykres
    axes.plot(time, mass_list)
    axes.set_xlabel("czas [s]")
    axes.set_ylabel("masa [kg]")
    axes.set_title("Left BinBox")
    if is_save:
        plt.savefig(f"Left_BinBox_{strftime('%m_%d_%Y-%H_%M_%S')}.png")
    if is_draw:
        plt.show()


if __name__ == '__main__':
    import sys

    sys.exit(main())






