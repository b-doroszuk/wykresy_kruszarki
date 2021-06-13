import time
from typing import Any, Union

from edempy import Deck
import numpy as np
import wykres_krzywej_skladu_ziarnowego_catmull_spline as script
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib

matplotlib.use("TkAgg")


class WykresKrzywejSkladuZiarnowego:

    def __init__(self, list_sections: list, enter_time_step: int, rock_number=0,
                 is_save=False, is_draw=True, numer_wychodu=1, filepath=""):

        """
            Parametry wejscia:
            enter_time_step     - numer kroku czasowego,
            rock_number         -
            is_save             - czy zapisac wykres,
            is_draw             - czy rysowac wykres,
            numer_wychodu       - numner wychodu,
            filepath            - sciezka do pliku
            list_section        - tablica przedzialow,
        """

        self.deck = Deck(filepath)
        self.time_step = enter_time_step
        self.rock_number = rock_number
        self.list_sections = list_sections

        self.how_many_sections = len(self.list_sections)  # ile mamy sekcji ?

        self.numer_wychodu = numer_wychodu
        self.is_save = is_save
        self.is_draw = is_draw

    def info(self):
        print("nazwy skal:", end="\t")
        print(self.deck.particleNames)
        print("liczba krokow czasowych:", end="\t")
        print(self.deck.numTimesteps)

    def get_data(self, rock_number=0) -> tuple:


        rocks_diameter = []
        rocks_mass = []

        if rock_number == 0:
            """ Getting list diameters """
            lupek_diameter = list(self.deck.timestep[self.time_step].particle[0].getSphereRadii() * 2000)
            piaskowiec_diameter = list(self.deck.timestep[self.time_step].particle[1].getSphereRadii() * 2000)
            dolomit_diameter = list(self.deck.timestep[self.time_step].particle[2].getSphereRadii() * 2000)
            rocks_diameter = lupek_diameter + piaskowiec_diameter + dolomit_diameter

            """ Getting list mass """
            lupek_mass = list(self.deck.timestep[self.time_step].particle[0].getMass())  # self.rock_number
            piaskowiec_mass = list(self.deck.timestep[self.time_step].particle[1].getMass())
            dolomit_mass = list(self.deck.timestep[self.time_step].particle[2].getMass())
            rocks_mass = lupek_mass + piaskowiec_mass + dolomit_mass

        elif rock_number == 1:
            lupek_diameter = list(self.deck.timestep[self.time_step].particle[0].getSphereRadii() * 2000)
            rocks_diameter = lupek_diameter
            lupek_mass = list(self.deck.timestep[self.time_step].particle[0].getMass())  # self.rock_number
            rocks_mass = lupek_mass

        elif rock_number == 2:
            piaskowiec_diameter = list(self.deck.timestep[self.time_step].particle[1].getSphereRadii() * 2000)
            rocks_diameter = piaskowiec_diameter
            piaskowiec_mass = list(self.deck.timestep[self.time_step].particle[1].getMass())
            rocks_mass = piaskowiec_mass

        elif rock_number == 3:
            dolomit_diameter = list(self.deck.timestep[self.time_step].particle[2].getSphereRadii() * 2000)
            rocks_diameter = dolomit_diameter
            dolomit_mass = list(self.deck.timestep[self.time_step].particle[2].getMass())
            rocks_mass = dolomit_mass

        rocks_diameter.sort()
        rocks_mass.sort()

        """ Return two lists with diameters and mass """
        return rocks_diameter, rocks_mass

    def get_dummy(self, rock_number=0) -> float:

        """
        Getting dummy mass:
        - lupek,
        - piaskowiec
        - dolomit
         """

        dummy_mass = 0

        if rock_number == 0:
            for i in range(3, 6):
                try:
                    dummy_mass += sum(list(self.deck.timestep[self.time_step].particle[i].getMass()))
                except Exception:
                    continue

        elif rock_number == 1:
            dummy_mass += sum(list(self.deck.timestep[self.time_step].particle[3].getMass()))

        elif rock_number == 2:
            dummy_mass += sum(list(self.deck.timestep[self.time_step].particle[4].getMass()))

        elif rock_number == 3:
            dummy_mass += sum(list(self.deck.timestep[self.time_step].particle[5].getMass()))

        return dummy_mass

    def get_total_mass(self):

        rocks_diameter, rocks_mass = self.get_data(self.rock_number)
        dummmy_mass = self.get_dummy(self.rock_number)

        total_mass = sum(rocks_mass) + dummmy_mass

        return total_mass

    def split_data_into_arrays(self):
        rock_diameter, rock_mass = self.get_data(self.rock_number)
        dummy_sum = self.get_dummy(self.rock_number)
        sections = self.list_sections
        rock_diameter_2, rock_mass_2 = self.get_data(self.rock_number)

        diameter_sections_list = [[] for i in range(self.how_many_sections)]
        counter = -1

        for i in range(self.how_many_sections):
            counter += 1

            if i == 0:
                for j in rock_diameter_2:
                    if j <= sections[i]:
                        diameter_sections_list[i].append(j)

            elif i == counter:
                for j in rock_diameter_2:
                    if sections[i - 1] < j <= sections[i]:
                        diameter_sections_list[i].append(j)

            elif i == len(diameter_sections_list) - 1:
                for j in rock_diameter_2:
                    if sections[i - 1] < j <= sections[i]:
                        diameter_sections_list[i].append(j)

        if_list = []
        for i in range(self.how_many_sections):
            if i == 0:
                if_list.append(len(diameter_sections_list[i]))
            else:
                if_list.append(len(diameter_sections_list[i]) + if_list[i - 1])

        mass_sections_list = [[] for x in range(self.how_many_sections)]

        j = 0
        if self.how_many_sections == 5:
            print("5 ELEMENTOW!!!!")
            for i in rock_mass:
                if j < if_list[0]:
                    mass_sections_list[0].append(i + (dummy_sum / len(diameter_sections_list[0])))  # + ))
                    j += 1
                elif if_list[0] <= j < if_list[1]:
                    mass_sections_list[1].append(i)
                    j += 1
                elif if_list[1] <= j < if_list[2]:
                    mass_sections_list[2].append(i)
                    j += 1
                elif if_list[2] <= j < if_list[3]:
                    mass_sections_list[3].append(i)
                    j += 1
                elif if_list[3] <= j < if_list[4]:
                    mass_sections_list[4].append(i)
                    j += 1

                else:
                    break
        elif self.how_many_sections == 6:
            print("6 ELEMENTOW!!!!")
            for i in rock_mass:
                if j < if_list[0]:
                    mass_sections_list[0].append(i + (dummy_sum / len(diameter_sections_list[0])))  # + ))
                    j += 1
                elif if_list[0] <= j < if_list[1]:
                    mass_sections_list[1].append(i)
                    j += 1
                elif if_list[1] <= j < if_list[2]:
                    mass_sections_list[2].append(i)
                    j += 1
                elif if_list[2] <= j < if_list[3]:
                    mass_sections_list[3].append(i)
                    j += 1
                elif if_list[3] <= j < if_list[4]:
                    mass_sections_list[4].append(i)
                    j += 1
                elif if_list[4] <= j < if_list[5]:
                    mass_sections_list[5].append(i)
                    j += 1
                else:
                    break
        elif self.how_many_sections == 7:
            print("7 ELEMENTOW!!!!")
            for i in rock_mass:
                if j < if_list[0]:
                    mass_sections_list[0].append(i + (dummy_sum / len(diameter_sections_list[0])))
                    j += 1
                elif if_list[0] <= j < if_list[1]:
                    mass_sections_list[1].append(i)
                    j += 1
                elif if_list[1] <= j < if_list[2]:
                    mass_sections_list[2].append(i)
                    j += 1
                elif if_list[2] <= j < if_list[3]:
                    mass_sections_list[3].append(i)
                    j += 1
                elif if_list[3] <= j < if_list[4]:
                    mass_sections_list[4].append(i)
                    j += 1
                elif if_list[4] <= j < if_list[5]:
                    mass_sections_list[5].append(i)
                    j += 1
                elif if_list[5] <= j < if_list[6]:
                    mass_sections_list[6].append(i)
                    j += 1
                else:
                    break

        elif self.how_many_sections == 8:
            print("8 ELEMENTOW!!!!")
            for i in rock_mass:
                if j < if_list[0]:
                    mass_sections_list[0].append(i + (dummy_sum / len(diameter_sections_list[0])))
                    j += 1
                elif if_list[0] <= j < if_list[1]:
                    mass_sections_list[1].append(i)
                    j += 1
                elif if_list[1] <= j < if_list[2]:
                    mass_sections_list[2].append(i)
                    j += 1
                elif if_list[2] <= j < if_list[3]:
                    mass_sections_list[3].append(i)
                    j += 1
                elif if_list[3] <= j < if_list[4]:
                    mass_sections_list[4].append(i)
                    j += 1
                elif if_list[4] <= j < if_list[5]:
                    mass_sections_list[5].append(i)
                    j += 1
                elif if_list[5] <= j < if_list[6]:
                    mass_sections_list[6].append(i)
                    j += 1
                elif if_list[6] <= j < if_list[7]:
                    mass_sections_list[7].append(i)
                    j += 1
                else:
                    break

        elif self.how_many_sections == 9:
            print("9 ELEMENTOW!!!!")
            for i in rock_mass:
                if j < if_list[0]:
                    mass_sections_list[0].append(i + (dummy_sum / len(diameter_sections_list[0])))
                    j += 1
                elif if_list[0] <= j < if_list[1]:
                    mass_sections_list[1].append(i)
                    j += 1
                elif if_list[1] <= j < if_list[2]:
                    mass_sections_list[2].append(i)
                    j += 1
                elif if_list[2] <= j < if_list[3]:
                    mass_sections_list[3].append(i)
                    j += 1
                elif if_list[3] <= j < if_list[4]:
                    mass_sections_list[4].append(i)
                    j += 1
                elif if_list[4] <= j < if_list[5]:
                    mass_sections_list[5].append(i)
                    j += 1
                elif if_list[5] <= j < if_list[6]:
                    mass_sections_list[6].append(i)
                    j += 1
                elif if_list[6] <= j < if_list[7]:
                    mass_sections_list[7].append(i)
                    j += 1
                elif if_list[7] <= j < if_list[8]:
                    mass_sections_list[8].append(i)
                    j += 1
                else:
                    break

        elif self.how_many_sections == 10:
            print("10 ELEMENTOW!!!!")
            for i in rock_mass:
                if j < if_list[0]:
                    mass_sections_list[0].append(i + (dummy_sum / len(diameter_sections_list[0])))
                    j += 1
                elif if_list[0] <= j < if_list[1]:
                    mass_sections_list[1].append(i)
                    j += 1
                elif if_list[1] <= j < if_list[2]:
                    mass_sections_list[2].append(i)
                    j += 1
                elif if_list[2] <= j < if_list[3]:
                    mass_sections_list[3].append(i)
                    j += 1
                elif if_list[3] <= j < if_list[4]:
                    mass_sections_list[4].append(i)
                    j += 1
                elif if_list[4] <= j < if_list[5]:
                    mass_sections_list[5].append(i)
                    j += 1
                elif if_list[5] <= j < if_list[6]:
                    mass_sections_list[6].append(i)
                    j += 1
                elif if_list[6] <= j < if_list[7]:
                    mass_sections_list[7].append(i)
                    j += 1
                elif if_list[7] <= j < if_list[8]:
                    mass_sections_list[8].append(i)
                    j += 1
                elif if_list[8] <= j < if_list[9]:
                    mass_sections_list[9].append(i)
                    j += 1
                else:
                    break

        return diameter_sections_list, mass_sections_list

    def characteristic_points(self):
        total_mass = self.get_total_mass()
        rocks_diameter, rock_mass = self.get_data(self.rock_number)
        diameter_sections_list, mass_sections_list = self.split_data_into_arrays()
        dummy_mass = self.get_dummy(self.rock_number)

        counter_80 = 0
        f_1 = (0.80 * total_mass)
        s_value_1 = 0
        for i in rock_mass:
            if s_value_1 <= f_1:
                if diameter_sections_list[0]:
                    if counter_80 <= len(diameter_sections_list[0]):
                        s_value_1 += (i + (dummy_mass / len(diameter_sections_list[0])))
                        counter_80 += 1
                    else:
                        s_value_1 += i
                        counter_80 += 1
                else:
                    break
            else:
                break

        counter_50 = 0
        f_2 = (0.50 * total_mass)
        s_value_2 = 0
        for i in rock_mass:
            if s_value_2 <= f_2:
                if diameter_sections_list[0]:
                    if counter_50 <= len(diameter_sections_list[0]):
                        s_value_2 += (i + (dummy_mass / len(diameter_sections_list[0])))
                        counter_50 += 1
                    else:
                        s_value_2 += i
                        counter_50 += 1
                else:
                    break
            else:
                break

        return counter_50, counter_80

    def thickening_points(self):

        total_mass = self.get_total_mass()
        rocks_diameter, rock_mass = self.get_data(self.rock_number)
        diameter_sections_list, mass_sections_list = self.split_data_into_arrays()
        dummy_mass = self.get_dummy(self.rock_number)

        counter_15 = 0
        f_2 = (0.15 * total_mass)
        s_value_2 = 0
        for i in rock_mass:
            if s_value_2 <= f_2:
                if diameter_sections_list[0]:
                    if counter_15 <= len(diameter_sections_list[0]):
                        s_value_2 += (i + (dummy_mass / len(diameter_sections_list[0])))
                        counter_15 += 1
                    else:
                        s_value_2 += i
                        counter_15 += 1
                else:
                    break
            else:
                break

        return counter_15

    def prepate_data(self):
        total_mass = self.get_total_mass()
        diameter_sections_list, mass_sections_list = self.split_data_into_arrays()
        sections = self.list_sections
        counter_15 = self.thickening_points()
        counter_50, counter_80 = self.characteristic_points()
        rock_diameter, rock_mass = self.get_data(self.rock_number)

        lista = []

        for i in range(self.how_many_sections):
            if not lista:
                lista.append(sum(mass_sections_list[i]) / total_mass)
            else:
                lista.append(sum(mass_sections_list[i]) / total_mass + lista[len(lista) - 1])

        Points = []

        tab_1 = [0]  # X
        tab_2 = [0]  # Y
        for i in range(self.how_many_sections):  # iteruje tyle ile mamy sekcji !!!
            tab_1.append(sections[i])
            tab_2.append(lista[i] * 100)

        char_50 = [rock_diameter[counter_50], 50]
        char_80 = [rock_diameter[counter_80], 80]
        thick_15 = [rock_diameter[counter_15], 15]

        Points.append(char_50)
        Points.append(char_80)
        Points.append(thick_15)

        for i in range(len(tab_1)):
            Points.append([tab_1[i], tab_2[i]])

        # Points.sort(key=lambda x: (x[1], x[0]))
        Points.sort(key=lambda x: (x[0], x[1]))

        # rock_diameter[counter_50]
        # rock_diameter[counter_50]

        return tab_1, tab_2, char_80, char_50, thick_15

    def averaged_draw(self, tab_1, tab_2, char_80, char_50, thick_15):

        fig = plt.figure(figsize=(7, 6))
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

        Points = []

        Points.append(char_80)
        Points.append(char_50)
        Points.append(thick_15)
        for i in range(len(tab_1)):
            Points.append([tab_1[i], tab_2[i]])

        n = len(Points)  # amount elements in Points

        Points.sort(key=lambda x: (x[1], x[0]))

        """ Printuje linie na wykresie poczatek-koniec """
        axes.plot([Points[n - 2][0], Points[n - 1][0]], [Points[n - 2][1], Points[n - 1][1]], color='b')
        axes.plot([Points[0][0], Points[1][0]], [Points[0][1], Points[1][1]], color='b')

        # Define a set of points for curve to go through
        # Points = [[tab_1[0], tab_2[0]], [tab_1[1], tab_2[1]], [tab_1[2], tab_2[2]],[dol_d[count_2], 50]

        # Calculate the Catmull-Rom splines through the points
        c = script.CatmullRomChain(Points)
        # Convert the Catmull-Rom curve points into x and y arrays and plot
        x, y = zip(*c)
        plt.plot(x, y, color='b')

        """Plotting points and additionals"""  # 50 i 80 !!!
        axes.plot(char_50[0], 50, 'o', color='k')
        axes.plot(char_80[0], 80, 'o', color='k')
        axes.text(char_80[0] + 0.5, 80, f" {round(char_80[0], 2)} w 80%")
        axes.text(char_50[0] + 0.5, 50, f" {round(char_50[0], 2)} w 50%")

        # punkty !!!
        axes.plot(tab_1, tab_2, 'o', color='b')  # draw points

        """ Plotting text """

        blue_line = mlines.Line2D([], [], color='blue', marker='o', label=f'wychód {self.numer_wychodu}')
        plt.legend(handles=[blue_line])
        plt.title(f'wychód {self.numer_wychodu}')
        plt.xlabel('górna granica przedzialu')
        plt.ylabel('Σ masa %')

        if self.is_save:
            plt.savefig(f"wychod{self.numer_wychodu}__{time.strftime('%m_%d_%Y-%H_%M_%S')}__{self.time_step}.png")

        if self.is_draw:
            plt.show()



    def draw_graph(self):
        diameter_sections_list, mass_sections_list = self.split_data_into_arrays()
        rock_diameter, rock_mass = self.get_data(self.rock_number)
        sections = self.list_sections

        acc_in_sec = self.prepate_data()  ##

        counter_15 = self.thickening_points()
        counter_50, counter_80 = self.characteristic_points()

        fig = plt.figure(figsize=(7, 6))
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

        tab_1, tab_2, char_80, char_50, thick_15 = self.prepate_data()
        """POINTS"""
        Points = []

        # tab_1 = [0]  # X
        # tab_2 = [0]  # Y

        # for i in range(self.how_many_sections):  # iteruje tyle ile mamy sekcji !!!
        #    tab_1.append(sections[i])
        #    tab_2.append(acc_in_sec[i] * 100)

        Points.append([rock_diameter[counter_15], 15])
        Points.append([rock_diameter[counter_50], 50])
        Points.append([rock_diameter[counter_80], 80])

        for i in range(len(tab_1)):
            Points.append([tab_1[i], tab_2[i]])

        n = len(Points)  # amount elements in Points

        Points.sort(key=lambda x: (x[1], x[0]))
        print("POINTS\n\n", Points)

        """ Printuje linie na wykresie poczatek-koniec """
        axes.plot([Points[n - 2][0], Points[n - 1][0]], [Points[n - 2][1], Points[n - 1][1]], color='b')
        axes.plot([Points[0][0], Points[1][0]], [Points[0][1], Points[1][1]], color='b')

        # Define a set of points for curve to go through
        # Points = [[tab_1[0], tab_2[0]], [tab_1[1], tab_2[1]], [tab_1[2], tab_2[2]],[dol_d[count_2], 50]

        # Calculate the Catmull-Rom splines through the points
        c = script.CatmullRomChain(Points)
        # Convert the Catmull-Rom curve points into x and y arrays and plot
        x, y = zip(*c)
        plt.plot(x, y, color='b')

        # Plot the control points
        # px, py = zip(*Points)
        # plt.plot(px, py, 'o', color='r')

        """Plotting points and additionals"""  # 50 i 80 !!!
        axes.plot(rock_diameter[counter_50], 50, 'o', color='k')
        axes.plot(rock_diameter[counter_80], 80, 'o', color='k')
        axes.text(rock_diameter[counter_80] + 0.5, 80, f" {round(rock_diameter[counter_80], 2)} w 80%")
        axes.text(rock_diameter[counter_50] + 0.5, 50, f" {round(rock_diameter[counter_50], 2)} w 50%")

        # punkty !!!
        axes.plot(tab_1, tab_2, 'o', color='b')  # draw points

        """ Plotting text """

        blue_line = mlines.Line2D([], [], color='blue', marker='o', label=f'wychód {self.numer_wychodu}')
        plt.legend(handles=[blue_line])
        plt.title(f'wychód {self.numer_wychodu}')
        plt.xlabel('górna granica przedzialu')
        plt.ylabel('Σ masa %')

        if self.is_save:
            plt.savefig(f"wychod{self.numer_wychodu}__{time.strftime('%m_%d_%Y-%H_%M_%S')}__{self.time_step}.png")

        if self.is_draw:
            plt.show()

        pass


def main(args):
    """

    parametry wejsciowe:
    interval_table  = [poczatkowy krok, koncowy krok czasowy, interwal],
    list_section    = [20, 30, 40, 50, 60, 80] - od 5 do 10 elementow,
    filepath        = sciezka

    """

    interval_table = [100, 200, 50]
    list_sections = [20, 30, 50, 60, 80]
    filepath = "C:\\Users\\Jakub\\PycharmProjects\\test2\\testownik11_prof_Robert_Krol\\projekt_2\\POLKOWICE_etap_2\\simulation_0\\simulation_0.dem"



    table = [[] for x in range(5)]
    export_table = [[] for x in range(5)]

    # Utility to average lists
    avg = lambda items: float(sum(items)) / len(items)

    for i in range(interval_table[0], interval_table[1], interval_table[2]):
        test_object = WykresKrzywejSkladuZiarnowego(enter_time_step=i, rock_number=0, is_save=False,
                                             is_draw=True, numer_wychodu=1, filepath=filepath,
                                             list_sections=list_sections) #, 120, 200, 300, 1000])


        #test_object.draw_graph()
        #points = test.prepate_data()

        tab_1, tab_2, char_80, char_50, thick_15 = test_object.prepate_data()
        export_table[0] = tab_1
        table[0].append(tab_1)
        table[1].append(tab_2)
        table[2].append(char_80)
        table[3].append(char_50)
        table[4].append(thick_15)


    transposed_1 = zip(*table[1])
    averages_1 = map(avg, transposed_1)
    for i in averages_1:
        export_table[1].append(i)

    transposed_2 = zip(*table[2])
    averages_2 = map(avg, transposed_2)
    for i in averages_2:
        export_table[2].append(i)

    transposed_3 = zip(*table[3])
    averages_3 = map(avg, transposed_3)
    for i in averages_3:
        export_table[3].append(i)

    transposed_4 = zip(*table[4])
    averages_4 = map(avg, transposed_4)
    for i in averages_4:
        export_table[4].append(i)

    print(table)
    print(export_table)
    test_object.averaged_draw(tab_1=export_table[0], tab_2=export_table[1], char_80=export_table[2],
                              char_50=export_table[3], thick_15=export_table[4])



    #for i in range(len(table)):
    #    for j in table[i]:
    #        print(j)

    #print(avg)


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
