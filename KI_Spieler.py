from tracemalloc import start

from Spielfeld import Spielfeld
from SOMPiBrain import SOMPiBrain
from Spieler import Spieler


#KI-Spieler und Spieler sind zwei separate Klassen
#Bezug zum Spielfeld xxxx

#Reward-Funktion
#Reward_Ziel = 100
#Reward_Zug = -1
#Reward_illegal = -10

#action_num = 6

#Klasse KI_Spieler bezieht sich auf Spielfeld bzgl. legale Züge 
import time
from Spielfeld import Spielfeld, AKTIONEN
from SOMPiBrain import SOMPiBrain

#Reward-Funktion
Reward_Ziel = 100
Reward_Zug = -1
Reward_illegal = -10


class KI_Spieler(Spielfeld):
    def __init__(self, anzahl_Spielsteine):
        super().__init__(anzahl_Spielsteine)
        #state_num = 3^n (jede Scheibe auf einem von 3 Stäben), action_num = 6 (AKTIONEN)
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
        if not self.zug_ausfuehren(start, ziel):     # Spielfeld prüft selbst, ob der Zug legal ist
            return self.get_state(), Reward_illegal, False

        done = self.ist_geloest()
        reward = Reward_Ziel if done else Reward_Zug
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

    def vorfuehren(self, pause=0.7):
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
 
#Bezug zu AKTIONEN in Spielfeld.py
#Bezug zu state und action 
#training: keine Visualisierung, nur Berechnung der Züge und Rewards; Pause benötigt, um die Züge zu sehen
#Belohnung bei optimalen Zügen (optimaler Zug = 2^Anzahl_Spielsteine - 1)
#Vorführfunktion: Visualisierung über pygame in Spielfeld
#Lernerfolg prüfen?