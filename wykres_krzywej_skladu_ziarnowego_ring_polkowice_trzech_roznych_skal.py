import time
from edempy import Deck
import catmull_spline as script
import save_file_dla_trzech_skal
import dane_z_ring_polkowice as polk
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

    def get_data(self, rock_number) -> tuple:

        dummy_sum = self.get_dummy(self.rock_number)
        sections = self.list_sections

        rocks_diameter = []
        rocks_mass = []

        if rock_number == 0:
            # Wszystkie skaly
            rocks_diameter, rocks_mass = polk.ring_bin_all(self.time_step, deck=self.deck)

        elif rock_number == 1:
            # Lupek
            rocks_diameter, rocks_mass = polk.ring_bin_lupek(self.time_step, deck=self.deck)

        elif rock_number == 2:
            # Piaskowiec
            rocks_diameter, rocks_mass = polk.ring_bin_piaskowiec(self.time_step, deck=self.deck)

        elif rock_number == 3:
            # Dolomit
            rocks_diameter, rocks_mass = polk.ring_bin_dolomit(self.time_step, deck=self.deck)


        rocks_diameter.sort()
        rocks_mass.sort()

        """ Return two lists with diameters and mass """
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        total_mass = sum(rocks_mass) + dummy_sum

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


        diameter_sections_list = [[] for i in range(self.how_many_sections)]
        counter = -1

        for i in range(self.how_many_sections):
            counter += 1

            if i == 0:
                for j in rocks_diameter:
                    if j <= sections[i]:
                        diameter_sections_list[i].append(j)

            elif i == counter:
                for j in rocks_diameter:
                    if sections[i - 1] < j <= sections[i]:
                        diameter_sections_list[i].append(j)

            elif i == len(diameter_sections_list) - 1:
                for j in rocks_diameter:
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
            for i in rocks_mass:
                if j < if_list[0]:
                    # print(i, "dodatek", dummy_sum / len(diameter_sections_list[0]))
                    mass_sections_list[0].append(i)  # + (dummy_sum / len(diameter_sections_list[0])))

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

            if_was = False
            for i in mass_sections_list:
                if i and if_was is False:
                    if_was = True
                    print("true")
                    for j in range(len(i)):
                        i[j] += (dummy_sum / len(i))

                elif not i:
                    print("miss")
                    continue

                else:
                    print("exit")
                    break

        elif self.how_many_sections == 6:
            print("6 ELEMENTOW!!!!")
            for i in rocks_mass:
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
                else:
                    break

            if_was = False
            for i in mass_sections_list:
                if i and if_was is False:
                    if_was = True
                    print("true")
                    for j in range(len(i)):
                        i[j] += (dummy_sum / len(i))

                elif not i:
                    print("miss")
                    continue

                else:
                    print("exit")
                    break

        elif self.how_many_sections == 7:
            print("7 ELEMENTOW!!!!")
            for i in rocks_mass:
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

            if_was = False
            for i in mass_sections_list:
                if i and if_was is False:
                    if_was = True
                    print("true")
                    for j in range(len(i)):
                        i[j] += (dummy_sum / len(i))

                elif not i:
                    print("miss")
                    continue

                else:
                    print("exit")
                    break

        elif self.how_many_sections == 8:
            print("8 ELEMENTOW!!!!")
            for i in rocks_mass:
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

            if_was = False
            for i in mass_sections_list:
                if i and if_was is False:
                    if_was = True
                    print("true")
                    for j in range(len(i)):
                        i[j] += (dummy_sum / len(i))

                elif not i:
                    print("miss")
                    continue

                else:
                    print("exit")
                    break

        elif self.how_many_sections == 9:
            print("9 ELEMENTOW!!!!")
            for i in rocks_mass:
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

            if_was = False
            for i in mass_sections_list:
                if i and if_was is False:
                    if_was = True
                    print("true")
                    for j in range(len(i)):
                        i[j] += (dummy_sum / len(i))

                elif not i:
                    print("miss")
                    continue

                else:
                    print("exit")
                    break

        elif self.how_many_sections == 10:
            print(" 10 ELEMENTOW!!!!")
            for i in rocks_mass:
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

            if_was = False
            for i in mass_sections_list:
                if i and if_was is False:
                    if_was = True
                    print("true")
                    for j in range(len(i)):
                        i[j] += (dummy_sum / len(i))

                elif not i:
                    print("miss")
                    continue

                else:
                    print("exit")
                    break

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        counter_80 = 0
        f_1 = (0.80 * total_mass)
        s_value_1 = 0
        for i in rocks_mass:
            if s_value_1 <= f_1:
                if diameter_sections_list[0]:
                    if counter_80 <= len(diameter_sections_list[0]):
                        s_value_1 += (i + (dummy_sum / len(diameter_sections_list[0])))
                        counter_80 += 1
                    else:
                        s_value_1 += i
                        counter_80 += 1

                elif diameter_sections_list[1]:
                    if counter_80 <= len(diameter_sections_list[1]):
                        s_value_1 += (i + (dummy_sum / len(diameter_sections_list[1])))
                        counter_80 += 1
                    else:
                        s_value_1 += i
                        counter_80 += 1

                elif diameter_sections_list[2]:
                    if counter_80 <= len(diameter_sections_list[2]):
                        s_value_1 += (i + (dummy_sum / len(diameter_sections_list[2])))
                        counter_80 += 1
                    else:
                        s_value_1 += i
                        counter_80 += 1

                elif diameter_sections_list[3]:
                    if counter_80 <= len(diameter_sections_list[3]):
                        s_value_1 += (i + (dummy_sum / len(diameter_sections_list[3])))
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
        for i in rocks_mass:
            if s_value_2 <= f_2:
                if diameter_sections_list[0]:
                    if counter_50 <= len(diameter_sections_list[0]):
                        s_value_2 += (i + (dummy_sum / len(diameter_sections_list[0])))
                        counter_50 += 1
                    else:
                        s_value_2 += i
                        counter_50 += 1

                elif diameter_sections_list[1]:
                    if counter_50 <= len(diameter_sections_list[1]):
                        s_value_2 += (i + (dummy_sum / len(diameter_sections_list[1])))
                        counter_50 += 1
                    else:
                        s_value_2 += i
                        counter_50 += 1

                elif diameter_sections_list[2]:
                    if counter_50 <= len(diameter_sections_list[2]):
                        s_value_2 += (i + (dummy_sum / len(diameter_sections_list[2])))
                        counter_50 += 1
                    else:
                        s_value_2 += i
                        counter_50 += 1

                elif diameter_sections_list[3]:
                    if counter_50 <= len(diameter_sections_list[3]):
                        s_value_2 += (i + (dummy_sum / len(diameter_sections_list[3])))
                        counter_50 += 1

                    else:
                        s_value_2 += i
                        counter_50 += 1

                else:
                    break
            else:
                break

        counter_15 = 0
        f_2 = (0.15 * total_mass)
        s_value_2 = 0
        for i in rocks_mass:
            if s_value_2 <= f_2:
                if diameter_sections_list[0]:
                    if counter_15 <= len(diameter_sections_list[0]):
                        s_value_2 += (i + (dummy_sum / len(diameter_sections_list[0])))
                        counter_15 += 1
                    else:
                        s_value_2 += i
                        counter_15 += 1

                elif diameter_sections_list[1]:
                    if counter_15 <= len(diameter_sections_list[1]):
                        s_value_2 += (i + (dummy_sum / len(diameter_sections_list[1])))
                        counter_15 += 1
                    else:
                        s_value_2 += i
                        counter_15 += 1

                elif diameter_sections_list[2]:
                    if counter_15 <= len(diameter_sections_list[2]):
                        s_value_2 += (i + (dummy_sum / len(diameter_sections_list[2])))
                        counter_15 += 1
                    else:
                        s_value_2 += i
                        counter_15 += 1

                elif diameter_sections_list[3]:
                    if counter_15 <= len(diameter_sections_list[3]):
                        s_value_2 += (i + (dummy_sum / len(diameter_sections_list[3])))
                        counter_15 += 1
                    else:
                        s_value_2 += i
                        counter_15 += 1

                else:
                    break
            else:
                break

        return rocks_diameter, rocks_mass, diameter_sections_list, mass_sections_list, total_mass, counter_50, counter_80, counter_15

    def get_dummy(self, rock_number=0) -> float:

        """ Getting dummy mass """

        dummy_mass = 0
        if rock_number == 0:
            dummy_mass += sum(polk.ring_dummy_bin_all(self.time_step, self.deck))

        elif rock_number == 1:
            dummy_mass += sum(polk.ring_dummy_bin_lupek(self.time_step, self.deck))

        elif rock_number == 2:
            dummy_mass += sum(polk.ring_dummy_bin_piaskowiec(self.time_step, self.deck))

        elif rock_number == 3:
            dummy_mass += sum(polk.ring_dummy_bin_dolomit(self.time_step, self.deck))

        return dummy_mass

    def prepate_data(self):

        sections = self.list_sections
        rock_diameter, rock_mass, diameter_sections_list, mass_sections_list, total_mass, counter_50, \
        counter_80, counter_15 = self.get_data(self.rock_number)

        lista = []
        for i in range(self.how_many_sections):
            if not lista:
                lista.append(sum(mass_sections_list[i]) / total_mass)
            else:
                lista.append(sum(mass_sections_list[i]) / total_mass + lista[len(lista) - 1])

        Points = []

        # X
        tab_1 = [0]
        # Y
        tab_2 = [0]
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

        Points.sort(key=lambda x: (x[0], x[1]))

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
        axes.plot([Points[n - 2][0], Points[n - 1][0]], [Points[n - 2][1], Points[n - 1][1]], color='r')
        axes.plot([Points[0][0], Points[1][0]], [Points[0][1], Points[1][1]], color='r')

        # Define a set of points for curve to go through
        # Points = [[tab_1[0], tab_2[0]], [tab_1[1], tab_2[1]], [tab_1[2], tab_2[2]],[dol_d[count_2], 50]

        # Calculate the Catmull-Rom splines through the points
        c = script.CatmullRomChain(Points)
        # Convert the Catmull-Rom curve points into x and y arrays and plot
        x, y = zip(*c)
        plt.plot(x, y, color='b')

        """Plotting points and additionals"""  # 50 i 80 !!!
        axes.plot(char_50[0], 50, 'o', color='r')
        axes.plot(char_80[0], 80, 'o', color='r')
        axes.text(char_80[0] + 0.5, 80, f"d80= {round(char_80[0], 2)}")
        axes.text(char_50[0] + 0.5, 50, f"d50= {round(char_50[0], 2)}")

        # punkty !!!
        axes.plot(tab_1, tab_2, 'o', color='b')  # draw points

        """ Plotting text """

        blue_line = mlines.Line2D([], [], color='blue', marker='o', label=f'wychód {self.numer_wychodu}')
        plt.legend(handles=[blue_line])
        plt.title(f'wychód 1 {self.numer_wychodu}')
        plt.xlabel('górna granica przedzialu')
        plt.ylabel('Σ masa %')

        if self.is_save:
            plt.savefig(f"wychod{self.numer_wychodu}__{time.strftime('%m_%d_%Y-%H_%M_%S')}__{self.time_step}.png")

        if self.is_draw:
            plt.show()

    def draw_graph(self):

        tab_1, tab_2, char_80, char_50, thick_15 = self.prepate_data()
        rock_diameter, rock_mass, diameter_sections_list, mass_sections_list, total_mass, counter_50, counter_80, counter_15 = self.get_data(self.rock_number)


        #counter_15 = self.thickening_points()
        #counter_50, counter_80 = self.characteristic_points()

        fig = plt.figure(figsize=(7, 6))
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])


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

    def test_draw(self, tab_1, tab_2, char_80, char_50, thick_15, tab_1_2, tab_2_2, char_80_2, char_50_2, thick_15_2,
                  tab_1_3, tab_2_3, char_80_3, char_50_3, thick_15_3):

        fig = plt.figure(figsize=(7, 6))
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        Points = []

        Points.append(char_80)
        Points.append(char_50)
        Points.append(thick_15)
        for i in range(len(tab_1)):
            Points.append([tab_1[i], tab_2[i]])

        n = len(Points)  # amount elements in Points

        Points.sort(key=lambda x: (x[1], x[0]))

        """ Printuje linie na wykresie poczatek-koniec """
        axes.plot([Points[n - 2][0], Points[n - 1][0]], [Points[n - 2][1], Points[n - 1][1]], color='r')
        axes.plot([Points[0][0], Points[1][0]], [Points[0][1], Points[1][1]], color='r')

        # Define a set of points for curve to go through
        # Points = [[tab_1[0], tab_2[0]], [tab_1[1], tab_2[1]], [tab_1[2], tab_2[2]],[dol_d[count_2], 50]

        # Calculate the Catmull-Rom splines through the points
        c = script.CatmullRomChain(Points)
        # Convert the Catmull-Rom curve points into x and y arrays and plot
        x, y = zip(*c)
        plt.plot(x, y, color='r')

        """Plotting points and additionals"""  # 50 i 80 !!!
        axes.plot(char_50[0], 50, 'o', color='r')
        axes.plot(char_80[0], 80, 'o', color='r')
        axes.text(char_80[0], 83, f"d80= {round(char_80[0], 2)}", color='r')
        axes.text(char_50[0], 53, f"d50= {round(char_50[0], 2)}", color='r')

        # punkty !!!
        axes.plot(tab_1, tab_2, 'o', color='r')  # draw points

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        Points_2 = []

        Points_2.append(char_80_2)
        Points_2.append(char_50_2)
        Points_2.append(thick_15_2)
        for i in range(len(tab_1_2)):
            Points_2.append([tab_1_2[i], tab_2_2[i]])

        n = len(Points_2)  # amount elements in Points

        Points_2.sort(key=lambda x: (x[1], x[0]))

        """ Printuje linie na wykresie poczatek-koniec """
        axes.plot([Points_2[n - 2][0], Points_2[n - 1][0]], [Points_2[n - 2][1], Points_2[n - 1][1]], color='b')
        axes.plot([Points_2[0][0], Points_2[1][0]], [Points_2[0][1], Points_2[1][1]], color='b')

        # Define a set of points for curve to go through
        # Points = [[tab_1[0], tab_2[0]], [tab_1[1], tab_2[1]], [tab_1[2], tab_2[2]],[dol_d[count_2], 50]

        # Calculate the Catmull-Rom splines through the points
        c_2 = script.CatmullRomChain(Points_2)
        # Convert the Catmull-Rom curve points into x and y arrays and plot
        x_2, y_2 = zip(*c_2)
        plt.plot(x_2, y_2, color='b')

        """Plotting points and additionals"""  # 50 i 80 !!!
        axes.plot(char_50_2[0], 50, 'o', color='b')
        axes.plot(char_80_2[0], 80, 'o', color='b')
        axes.text(char_80_2[0], 80, f"d80= {round(char_80_2[0], 2)}", color='b')
        axes.text(char_50_2[0], 50, f"d50= {round(char_50_2[0], 2)}", color='b')

        # punkty !!!
        axes.plot(tab_1_2, tab_2_2, 'o', color='b')  # draw points

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        Points_3 = []

        Points_3.append(char_80_3)
        Points_3.append(char_50_3)
        Points_3.append(thick_15_3)
        for i in range(len(tab_1_3)):
            Points_3.append([tab_1_3[i], tab_2_3[i]])

        n = len(Points_3)  # amount elements in Points

        Points_3.sort(key=lambda x: (x[1], x[0]))

        """ Printuje linie na wykresie poczatek-koniec """
        axes.plot([Points_3[n - 2][0], Points_3[n - 1][0]], [Points_3[n - 2][1], Points_3[n - 1][1]], color='y')
        axes.plot([Points_3[0][0], Points_3[1][0]], [Points_3[0][1], Points_3[1][1]], color='y')

        # Define a set of points for curve to go through
        # Points = [[tab_1[0], tab_2[0]], [tab_1[1], tab_2[1]], [tab_1[2], tab_2[2]],[dol_d[count_2], 50]

        # Calculate the Catmull-Rom splines through the points
        c_3 = script.CatmullRomChain(Points_3)
        # Convert the Catmull-Rom curve points into x and y arrays and plot
        x_3, y_3 = zip(*c_3)
        plt.plot(x_3, y_3, color='y')

        """Plotting points and additionals"""  # 50 i 80 !!!
        axes.plot(char_50_3[0], 50, 'o', color='y')
        axes.plot(char_80_3[0], 80, 'o', color='y')
        axes.text(char_80_3[0], 77, f"d80= {round(char_80_3[0], 2)}", color='y')
        axes.text(char_50_3[0], 47, f"d50=  {round(char_50_3[0], 2)}", color='y')

        # punkty !!!
        axes.plot(tab_1_3, tab_2_3, 'o', color='y')  # draw points

        """ Plotting text """
        blue_line = mlines.Line2D([], [], color='blue', marker='o', label=f'wychód {self.numer_wychodu}')
        #plt.legend(handles=[blue_line])
        #plt.title(f'wychód {self.numer_wychodu}')
        plt.xlabel('górna granica przedzialu')
        plt.ylabel('Σ masa %')
        if self.is_save:
            plt.savefig(f"wychod{self.numer_wychodu}__{time.strftime('%m_%d_%Y-%H_%M_%S')}__{self.time_step}.png")

        if self.is_draw:
            plt.show()

        pass

def main():
    """
    Main function
    
    parametry wejsciowe:
    interval_table  = [poczatkowy krok, koncowy krok czasowy, interwal],
    list_section    = [20, 30, 40, 50, 60, 80] - od 5 do 10 elementow,
    filepath        = sciezka
    is_export       = czy exportowac do txt (True / False)
    """

    interval_table = [1900, 2000, 50]
    list_sections = [2, 4, 5, 8, 10, 15, 20, 25, 30]
    filepath = "E:\\Etap2_Polkowice\\simulation_0\\simulation_0.dem"
    is_export = True

    # All below treat as black-box
    fake_object = WykresKrzywejSkladuZiarnowego(enter_time_step=0, rock_number=0, is_save=False,
                                                is_draw=True, numer_wychodu=0, filepath=filepath,
                                                list_sections=[])

    table = [[] for x in range(5)]
    export_table = [[] for x in range(5)]

    table_2 = [[] for x in range(5)]
    export_2_table = [[] for x in range(5)]

    table_3 = [[] for x in range(5)]
    export_3_table = [[] for x in range(5)]

    # Utility to average lists
    avg = lambda items: float(sum(items)) / len(items)

    for i in range(interval_table[0], interval_table[1], interval_table[2]):

        test_object = WykresKrzywejSkladuZiarnowego(enter_time_step=i, rock_number=1, is_save=False,
                                                    is_draw=True, numer_wychodu=1, filepath=filepath,
                                                    list_sections=list_sections)  # , 120, 200, 300, 1000])

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

    for i in range(interval_table[0], interval_table[1], interval_table[2]):
        test_object = WykresKrzywejSkladuZiarnowego(enter_time_step=i, rock_number=2, is_save=False,
                                                    is_draw=True, numer_wychodu=1, filepath=filepath,
                                                    list_sections=list_sections)

        tab_1, tab_2, char_80, char_50, thick_15 = test_object.prepate_data()
        export_2_table[0] = tab_1
        table_2[0].append(tab_1)
        table_2[1].append(tab_2)
        table_2[2].append(char_80)
        table_2[3].append(char_50)
        table_2[4].append(thick_15)

    transposed_1_2 = zip(*table_2[1])
    averages_1_2 = map(avg, transposed_1_2)
    for i in averages_1_2:
        export_2_table[1].append(i)

    transposed_2_2 = zip(*table_2[2])
    averages_2_2 = map(avg, transposed_2_2)
    for i in averages_2_2:
        export_2_table[2].append(i)

    transposed_3_2 = zip(*table_2[3])
    averages_3_2 = map(avg, transposed_3_2)
    for i in averages_3_2:
        export_2_table[3].append(i)

    transposed_4_2 = zip(*table_2[4])
    averages_4_2 = map(avg, transposed_4_2)
    for i in averages_4_2:
        export_2_table[4].append(i)

    for i in range(interval_table[0], interval_table[1], interval_table[2]):
        test_object = WykresKrzywejSkladuZiarnowego(enter_time_step=i, rock_number=3, is_save=False,
                                                    is_draw=True, numer_wychodu=1, filepath=filepath,
                                                    list_sections=list_sections)

        tab_1, tab_2, char_80, char_50, thick_15 = test_object.prepate_data()
        export_3_table[0] = tab_1
        table_3[0].append(tab_1)
        table_3[1].append(tab_2)
        table_3[2].append(char_80)
        table_3[3].append(char_50)
        table_3[4].append(thick_15)

    transposed_1_3 = zip(*table_3[1])
    averages_1_3 = map(avg, transposed_1_3)
    for i in averages_1_3:
        export_3_table[1].append(i)

    transposed_2_3 = zip(*table_3[2])
    averages_2_3 = map(avg, transposed_2_3)
    for i in averages_2_3:
        export_3_table[2].append(i)

    transposed_3_3 = zip(*table_3[3])
    averages_3_3 = map(avg, transposed_3_3)
    for i in averages_3_3:
        export_3_table[3].append(i)

    transposed_4_3 = zip(*table_3[4])
    averages_4_3 = map(avg, transposed_4_3)
    for i in averages_4_3:
        export_3_table[4].append(i)

    fake_object.test_draw(tab_1=export_table[0], tab_2=export_table[1], char_80=export_table[2],
                          char_50=export_table[3], thick_15=export_table[4],
                          tab_1_2=export_2_table[0], tab_2_2=export_2_table[1], char_80_2=export_2_table[2],
                          char_50_2=export_2_table[3], thick_15_2=export_2_table[4],
                          tab_1_3=export_3_table[0], tab_2_3=export_3_table[1], char_80_3=export_3_table[2],
                          char_50_3=export_3_table[3], thick_15_3=export_3_table[4])

    # Przygotowanie danych do zapisu
    for k in range(2, 5):
        export_table[0].append(export_table[k][0])
        export_table[1].append(export_table[k][1])
        export_2_table[0].append(export_table[k][0])
        export_2_table[1].append(export_table[k][1])
        export_3_table[0].append(export_table[k][0])
        export_3_table[1].append(export_table[k][1])
    for i in range(3):
        export_table.pop()
        export_2_table.pop()
        export_3_table.pop()

    export_table[0].sort()
    export_table[1].sort()
    export_2_table[0].sort()
    export_2_table[1].sort()
    export_3_table[0].sort()
    export_3_table[1].sort()

    print("lupek", export_table)
    print("piaskowiec", export_2_table)
    print("dolomit", export_3_table)
    if is_export:
        save_file_dla_trzech_skal.zapisz(export_table, export_2_table, export_3_table, "export_kruszarka_dla_trzech_skal_" + str(time.strftime('%m_%d_%Y-%H_%M_%S')))

if __name__ == '__main__':
    import sys

    sys.exit(main())
