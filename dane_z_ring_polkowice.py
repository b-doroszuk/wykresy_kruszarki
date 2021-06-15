import time
from edempy import Deck
import numpy as np
from edempy import BoxBin, CylinderBin

filepath = "C:\\Users\\Jakub\\PycharmProjects\\test2\\testownik11_prof_Robert_Krol\\projekt_2\\POLKOWICE_etap_2\\simulation_0\\simulation_0.dem"

deck = Deck(filepath)


def ring_bin_all(time_step, deck):

    #"simulation_0.dem"
    start = time.time()


    A_boxbin = BoxBin([0, 0, 0.9], 3.6, 2, 1.8)
    B_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.8)
    C_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.5)


    #nTimeSteps = deck.numTimesteps
    #print("liczba krokow czasowych", nTimeSteps)
    #test = deck.creatorData.particleNames
    #print("nazwy czasteczek", test)

    mass = []
    diameter = []

    """LUPEK"""
    ids_0 = deck.timestep[time_step].particle[0].getIds()
    pos_0 = deck.timestep[time_step].particle[0].getPositions()

    binned_ids_A0 = set(A_boxbin.getBinnedObjects(ids_0, pos_0))
    binned_ids_B0 = set(B_cylinderbin.getBinnedObjects(ids_0, pos_0))
    binned_ids_C0 = set(C_cylinderbin.getBinnedObjects(ids_0, pos_0))

    binned_ids_E0 = binned_ids_B0 - (binned_ids_A0 & binned_ids_B0)
    binned_ids_D0 = binned_ids_C0 - (binned_ids_A0 & binned_ids_C0)
    binned_ids_X0 = binned_ids_E0 - binned_ids_D0

    for i in binned_ids_X0:
        mass.append(deck.timestep[time_step].particle[0].getMass(id=i))
        diameter.append(deck.timestep[time_step].particle[0].getSphereRadii(id=i)[0] * 2 * 1000)

    """PIASKOWIEC"""
    ids_1 = deck.timestep[time_step].particle[1].getIds()
    pos_1 = deck.timestep[time_step].particle[1].getPositions()

    binned_ids_A1 = set(A_boxbin.getBinnedObjects(ids_1, pos_1))
    binned_ids_B1 = set(B_cylinderbin.getBinnedObjects(ids_1, pos_1))
    binned_ids_C1 = set(C_cylinderbin.getBinnedObjects(ids_1, pos_1))

    binned_ids_E1 = binned_ids_B1 - (binned_ids_A1 & binned_ids_B1)
    binned_ids_D1 = binned_ids_C1 - (binned_ids_A1 & binned_ids_C1)
    binned_ids_X1 = binned_ids_E1 - binned_ids_D1

    for i in binned_ids_X1:
        mass.append(deck.timestep[time_step].particle[1].getMass(id=i))
        diameter.append(deck.timestep[time_step].particle[1].getSphereRadii(id=i)[0] * 2 * 1000)

    """DOLOMIT"""
    ids_2 = deck.timestep[time_step].particle[2].getIds()
    pos_2 = deck.timestep[time_step].particle[2].getPositions()

    binned_ids_A2 = set(A_boxbin.getBinnedObjects(ids_2, pos_2))
    binned_ids_B2 = set(B_cylinderbin.getBinnedObjects(ids_2, pos_2))
    binned_ids_C2 = set(C_cylinderbin.getBinnedObjects(ids_2, pos_2))

    binned_ids_E2 = binned_ids_B2 - (binned_ids_A2 & binned_ids_B2)
    binned_ids_D2 = binned_ids_C2 - (binned_ids_A2 & binned_ids_C2)
    binned_ids_X2 = binned_ids_E2 - binned_ids_D2

    for i in binned_ids_X2:
        mass.append(deck.timestep[time_step].particle[2].getMass(id=i))
        diameter.append(deck.timestep[time_step].particle[2].getSphereRadii(id=i)[0] * 2 * 1000)

    koniec = time.time()
    print("czas: ", koniec - start)

    return list(diameter), list(mass)



def ring_bin_lupek(time_step, deck):

    #"simulation_0.dem"
    start = time.time()


    A_boxbin = BoxBin([0, 0, 0.9], 3.6, 2, 1.8)
    B_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.8)
    C_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.5)

    mass = []
    diameter = []

    """LUPEK"""
    ids_0 = deck.timestep[time_step].particle[0].getIds()
    pos_0 = deck.timestep[time_step].particle[0].getPositions()

    binned_ids_A0 = set(A_boxbin.getBinnedObjects(ids_0, pos_0))
    binned_ids_B0 = set(B_cylinderbin.getBinnedObjects(ids_0, pos_0))
    binned_ids_C0 = set(C_cylinderbin.getBinnedObjects(ids_0, pos_0))

    binned_ids_E0 = binned_ids_B0 - (binned_ids_A0 & binned_ids_B0)
    binned_ids_D0 = binned_ids_C0 - (binned_ids_A0 & binned_ids_C0)
    binned_ids_X0 = binned_ids_E0 - binned_ids_D0

    for i in binned_ids_X0:
        mass.append(deck.timestep[time_step].particle[0].getMass(id=i))
        diameter.append(deck.timestep[time_step].particle[0].getSphereRadii(id=i)[0] * 2 * 1000)

    koniec = time.time()
    print("czas: ", koniec - start)

    return list(diameter), list(mass)


def ring_bin_piaskowiec(time_step, deck):

    #"simulation_0.dem"
    start = time.time()


    A_boxbin = BoxBin([0, 0, 0.9], 3.6, 2, 1.8)
    B_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.8)
    C_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.5)

    mass = []
    diameter = []

    """PIASKOWIEC"""
    ids_1 = deck.timestep[time_step].particle[1].getIds()
    pos_1 = deck.timestep[time_step].particle[1].getPositions()

    binned_ids_A1 = set(A_boxbin.getBinnedObjects(ids_1, pos_1))
    binned_ids_B1 = set(B_cylinderbin.getBinnedObjects(ids_1, pos_1))
    binned_ids_C1 = set(C_cylinderbin.getBinnedObjects(ids_1, pos_1))

    binned_ids_E1 = binned_ids_B1 - (binned_ids_A1 & binned_ids_B1)
    binned_ids_D1 = binned_ids_C1 - (binned_ids_A1 & binned_ids_C1)
    binned_ids_X1 = binned_ids_E1 - binned_ids_D1

    for i in binned_ids_X1:
        mass.append(deck.timestep[time_step].particle[1].getMass(id=i))
        diameter.append(deck.timestep[time_step].particle[1].getSphereRadii(id=i)[0] * 2 * 1000)

    koniec = time.time()
    print("czas: ", koniec - start)

    return list(diameter), list(mass)

def ring_bin_dolomit(time_step, deck):

    #"simulation_0.dem"
    start = time.time()


    A_boxbin = BoxBin([0, 0, 0.9], 3.6, 2, 1.8)
    B_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.8)
    C_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.5)

    mass = []
    diameter = []

    """DOLOMIT"""
    ids_2 = deck.timestep[time_step].particle[2].getIds()
    pos_2 = deck.timestep[time_step].particle[2].getPositions()

    binned_ids_A2 = set(A_boxbin.getBinnedObjects(ids_2, pos_2))
    binned_ids_B2 = set(B_cylinderbin.getBinnedObjects(ids_2, pos_2))
    binned_ids_C2 = set(C_cylinderbin.getBinnedObjects(ids_2, pos_2))

    binned_ids_E2 = binned_ids_B2 - (binned_ids_A2 & binned_ids_B2)
    binned_ids_D2 = binned_ids_C2 - (binned_ids_A2 & binned_ids_C2)
    binned_ids_X2 = binned_ids_E2 - binned_ids_D2

    for i in binned_ids_X2:
        mass.append(deck.timestep[time_step].particle[2].getMass(id=i))
        diameter.append(deck.timestep[time_step].particle[2].getSphereRadii(id=i)[0] * 2 * 1000)

    koniec = time.time()
    print("czas: ", koniec - start)

    return list(diameter), list(mass)

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

def ring_dummy_bin_all(time_step, deck):


    A_boxbin = BoxBin([0, 0, 0.9], 3.6, 2, 1.8)
    B_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.8)
    C_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.5)


    mass = []


    """LUPEK"""
    ids_0 = deck.timestep[time_step].particle[3].getIds()
    pos_0 = deck.timestep[time_step].particle[3].getPositions()

    binned_ids_A0 = set(A_boxbin.getBinnedObjects(ids_0, pos_0))
    binned_ids_B0 = set(B_cylinderbin.getBinnedObjects(ids_0, pos_0))
    binned_ids_C0 = set(C_cylinderbin.getBinnedObjects(ids_0, pos_0))

    binned_ids_E0 = binned_ids_B0 - (binned_ids_A0 & binned_ids_B0)
    binned_ids_D0 = binned_ids_C0 - (binned_ids_A0 & binned_ids_C0)
    binned_ids_X0 = binned_ids_E0 - binned_ids_D0

    for i in binned_ids_X0:
        mass.append(deck.timestep[time_step].particle[3].getMass(id=i))

    """PIASKOWIEC"""
    ids_1 = deck.timestep[time_step].particle[4].getIds()
    pos_1 = deck.timestep[time_step].particle[4].getPositions()

    binned_ids_A1 = set(A_boxbin.getBinnedObjects(ids_1, pos_1))
    binned_ids_B1 = set(B_cylinderbin.getBinnedObjects(ids_1, pos_1))
    binned_ids_C1 = set(C_cylinderbin.getBinnedObjects(ids_1, pos_1))

    binned_ids_E1 = binned_ids_B1 - (binned_ids_A1 & binned_ids_B1)
    binned_ids_D1 = binned_ids_C1 - (binned_ids_A1 & binned_ids_C1)
    binned_ids_X1 = binned_ids_E1 - binned_ids_D1

    for i in binned_ids_X1:
        mass.append(deck.timestep[time_step].particle[4].getMass(id=i))

    """DOLOMIT"""
    ids_2 = deck.timestep[time_step].particle[5].getIds()
    pos_2 = deck.timestep[time_step].particle[5].getPositions()

    binned_ids_A2 = set(A_boxbin.getBinnedObjects(ids_2, pos_2))
    binned_ids_B2 = set(B_cylinderbin.getBinnedObjects(ids_2, pos_2))
    binned_ids_C2 = set(C_cylinderbin.getBinnedObjects(ids_2, pos_2))

    binned_ids_E2 = binned_ids_B2 - (binned_ids_A2 & binned_ids_B2)
    binned_ids_D2 = binned_ids_C2 - (binned_ids_A2 & binned_ids_C2)
    binned_ids_X2 = binned_ids_E2 - binned_ids_D2

    for i in binned_ids_X2:
        mass.append(deck.timestep[time_step].particle[5].getMass(id=i))

    return list(mass)

def ring_dummy_bin_lupek(time_step, deck) -> list:

    A_boxbin = BoxBin([0, 0, 0.9], 3.6, 2, 1.8)
    B_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.8)
    C_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.5)

    mass = []

    """LUPEK"""
    ids_0 = deck.timestep[time_step].particle[3].getIds()
    pos_0 = deck.timestep[time_step].particle[3].getPositions()

    binned_ids_A0 = set(A_boxbin.getBinnedObjects(ids_0, pos_0))
    binned_ids_B0 = set(B_cylinderbin.getBinnedObjects(ids_0, pos_0))
    binned_ids_C0 = set(C_cylinderbin.getBinnedObjects(ids_0, pos_0))

    binned_ids_E0 = binned_ids_B0 - (binned_ids_A0 & binned_ids_B0)
    binned_ids_D0 = binned_ids_C0 - (binned_ids_A0 & binned_ids_C0)
    binned_ids_X0 = binned_ids_E0 - binned_ids_D0

    for i in binned_ids_X0:
        mass.append(deck.timestep[time_step].particle[3].getMass(id=i))

    return mass


def ring_dummy_bin_piaskowiec(time_step, deck):


    A_boxbin = BoxBin([0, 0, 0.9], 3.6, 2, 1.8)
    B_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.8)
    C_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.5)

    mass = []

    """PIASKOWIEC"""
    ids_1 = deck.timestep[time_step].particle[4].getIds()
    pos_1 = deck.timestep[time_step].particle[4].getPositions()

    binned_ids_A1 = set(A_boxbin.getBinnedObjects(ids_1, pos_1))
    binned_ids_B1 = set(B_cylinderbin.getBinnedObjects(ids_1, pos_1))
    binned_ids_C1 = set(C_cylinderbin.getBinnedObjects(ids_1, pos_1))

    binned_ids_E1 = binned_ids_B1 - (binned_ids_A1 & binned_ids_B1)
    binned_ids_D1 = binned_ids_C1 - (binned_ids_A1 & binned_ids_C1)
    binned_ids_X1 = binned_ids_E1 - binned_ids_D1

    for i in binned_ids_X1:
        mass.append(deck.timestep[time_step].particle[4].getMass(id=i))

    return mass

def ring_dummy_bin_dolomit(time_step, deck):


    A_boxbin = BoxBin([0, 0, 0.9], 3.6, 2, 1.8)
    B_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.8)
    C_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.5)

    mass = []

    """DOLOMIT"""
    ids_2 = deck.timestep[time_step].particle[5].getIds()
    pos_2 = deck.timestep[time_step].particle[5].getPositions()

    binned_ids_A2 = set(A_boxbin.getBinnedObjects(ids_2, pos_2))
    binned_ids_B2 = set(B_cylinderbin.getBinnedObjects(ids_2, pos_2))
    binned_ids_C2 = set(C_cylinderbin.getBinnedObjects(ids_2, pos_2))

    binned_ids_E2 = binned_ids_B2 - (binned_ids_A2 & binned_ids_B2)
    binned_ids_D2 = binned_ids_C2 - (binned_ids_A2 & binned_ids_C2)
    binned_ids_X2 = binned_ids_E2 - binned_ids_D2

    for i in binned_ids_X2:
        mass.append(deck.timestep[time_step].particle[5].getMass(id=i))


    return mass