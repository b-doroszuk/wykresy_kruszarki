from edempy import Deck
import edempy






filepath = "C:\\Users\\Jakub\\PycharmProjects\\test2\\testownik11_prof_Robert_Krol\\projekt_2\\POLKOWICE_etap_2\\simulation_0\\simulation_0.dem"

deck = Deck(filepath)

id = 95346

print(len(deck.timestep[240].particle[3].getMass()))
print(deck.timestep[240].particle[3].getMass())

#(self.deck.timestep[self.time_step].particle[3].getMass()))