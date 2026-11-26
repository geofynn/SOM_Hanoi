# @author Julian Kortz
# source for pygame: https://www.pygame.org/docs/


from tracemalloc import start
from Spielfeld import Spielfeld
from SOMPiBrain import SOMPiBrain
from Spieler import Spieler
import time


#Reward-Funktion
Reward_Ziel = 100
Reward_Zug = -1
Reward_illegal = -10
AKTIONEN = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)] #mögliche Aktionen: Stab 1 zu 2; Stab 1 zu 3...

class KI_Spieler(Spielfeld):
    def __init__(self, anzahl_Spielsteine):
        super().__init__(anzahl_Spielsteine)
        self.brain = SOMPiBrain(3 ** anzahl_Spielsteine, len(AKTIONEN), gamma=0.95)

    def get_state(self):
        state = 0
        for zeile in range(self.anzahl_Spielsteine):
            for stab in range(3):
                wert = self.Feld[zeile, stab]
                if wert != 0:
                    state += stab * 3 ** (wert - 1)
        return state

    def step(self, action):
        start, ziel = AKTIONEN[action]
        if not self.zug_ausfuehren(start, ziel):     # Spielfeld prüft ob der Zug legal ist
            return self.get_state(), Reward_illegal, False

        done = self.ist_geloest()   # prüft ob das Spiel gelöst ist
        reward = Reward_Ziel if done else Reward_Zug # Belohnung für die Lösung ansonsten Bestrafung
        return self.get_state(), reward, done

    def reset(self):
        self.Feld[:, :] = 0
        self.create_spielfeld()
        return self.get_state()

    def trainieren(self, episoden=5000):
        print("Training gestartet.")
        for i in range(episoden):
            state = self.reset()
            done = False
            while not done:
                action = self.brain.get_action(state)
                next_state, reward, done = self.step(action)
                state = self.brain.reward_action(state, next_state, action, reward)
        print("Training beendet.")

    def vorfuehren(self, pause=0.7): #Pause damit man in der GUI die Züge sehen kann
        state = self.reset()
        done = False
        while not done:
            if not self.zeige("KI spielt ..."):
                return
            time.sleep(pause)
            action = self.brain.get_action(state, explore=False)
            state, reward, done = self.step(action)
            if reward == Reward_illegal:
                print("Illegaler Zug - mehr trainieren!")
                return
        info = f"Gelöst in {self.zuege} Zügen (optimal: {2 ** self.anzahl_Spielsteine - 1})"
        print(info)
        while self.zeige(info):
            time.sleep(0.05)
 
