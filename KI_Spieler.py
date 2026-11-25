import time
from Spielfeld import Spielfeld, AKTIONEN
from SOMPiBrain import SOMPiBrain

#KI-Spieler und Spieler sind zwei separate Klassen
#Bezug zum Spielfeld: KI_Spieler erbt von Spielfeld (Feld, check_legal_move, zeige)
#Aufbau wie im testGym: reset() -> state, step(action) -> next_state, reward, done
#gymnasium wird hier nicht gebraucht, das Spielfeld ist unsere eigene "Umgebung"

#Reward-Funktion
Reward_Ziel = 100
Reward_Zug = -1
Reward_illegal = -10

#action: Index in AKTIONEN (0..5), z.B. 0 = Stab 1 zu Stab 2
action_num = len(AKTIONEN)


#Klasse KI_Spieler bezieht sich auf Spielfeld bzgl. legale Züge
class KI_Spieler(Spielfeld):
    def __init__(self, anzahl_Spielsteine, alpha=0.1, gamma=0.95, epsilon=0.1):
        super().__init__(anzahl_Spielsteine)
        #state: jeder Stein liegt auf einem von 3 Stäben -> 3^n mögliche Zustände
        self.state_num = 3 ** anzahl_Spielsteine
        self.max_zuege = 20 * (2 ** anzahl_Spielsteine)   #Abbruch, falls die KI sich verläuft
        #gamma höher als im testGym (0.6), weil die Belohnung erst nach 2^n-1 Zügen kommt
        self.brain = SOMPiBrain(self.state_num, action_num, alpha, gamma, epsilon)

    # ---------- Umgebung (wie env im testGym) ----------

    def reset(self):
        self.Feld[:, :] = 0
        self.create_spielfeld()
        return self.get_state()

    def get_state(self):
        #Zustand als Zahl im 3er-System: Ziffer i = Stab, auf dem Stein i+1 liegt
        state = 0
        for zeile in range(self.anzahl_Spielsteine):
            for stab in range(3):
                wert = self.Feld[zeile, stab]
                if wert != 0:
                    state += stab * 3 ** (wert - 1)
        return state

    def gewonnen(self):
        #alle Steine auf Stab 3
        return all(self.Feld[:, 2] != 0)

    def zug(self, start, ziel):
        #obersten Stein von start nach ziel legen (Zug muss legal sein)
        s_zeile = self.oberster_ring(start)
        z_zeile = self.oberster_ring(ziel)
        neue_zeile = self.anzahl_Spielsteine - 1 if z_zeile is None else z_zeile - 1
        self.Feld[neue_zeile, ziel] = self.Feld[s_zeile, start]
        self.Feld[s_zeile, start] = 0
        self.zuege += 1

    def step(self, action):
        start, ziel = AKTIONEN[action]
        if not self.check_legal_move(start, ziel):
            #illegaler Zug: Strafe, Feld bleibt gleich
            return self.get_state(), Reward_illegal, False
        self.zug(start, ziel)
        if self.gewonnen():
            return self.get_state(), Reward_Ziel, True
        return self.get_state(), Reward_Zug, False

    # ---------- KI-Spielzug ----------

    def KI_aktion(self, explore=False):
        #KI wählt selbst einen Zug und führt ihn aus
        state = self.get_state()
        action = self.brain.get_action(state, explore)
        return self.step(action)

    # ---------- Training (ohne Visualisierung) ----------

    def trainieren(self, episoden=5000):
        print("Training gestartet.")
        for i in range(1, episoden + 1):
            state = self.reset()
            done = False
            schritte = 0
            while not done and schritte < self.max_zuege:
                action = self.brain.get_action(state)
                next_state, reward, done = self.step(action)
                state = self.brain.reward_action(state, next_state, action, reward)
                schritte += 1
            if i % (episoden // 5) == 0:
                print(f"Episode {i}: {self.zuege} Züge")
        print("Training beendet.")

    # ---------- Lernerfolg prüfen ----------

    def pruefen(self):
        #ein Spiel ohne Zufall (explore=False), Vergleich mit optimaler Zugzahl
        self.reset()
        done = False
        illegal = 0
        while not done and self.zuege < self.max_zuege and illegal < self.max_zuege:
            _, reward, done = self.KI_aktion(explore=False)
            if reward == Reward_illegal:
                illegal += 1
        optimal = 2 ** self.anzahl_Spielsteine - 1
        print(f"Gelöst: {done}, Züge: {self.zuege}, optimal: {optimal}, illegale Versuche: {illegal}")
        return done and self.zuege == optimal

    # ---------- Vorführfunktion mit pygame ----------

    def vorfuehren(self, pause=0.7):
        self.reset()
        done = False
        if not self.zeige():
            return
        time.sleep(pause)
        while not done and self.zuege < self.max_zuege:
            _, reward, done = self.KI_aktion(explore=False)
            if reward == Reward_illegal:
                print("KI will einen illegalen Zug machen - mehr trainieren!")
                break
            if not self.zeige():
                return
            time.sleep(pause)
        #Fenster offen lassen, bis es geschlossen wird
        while self.zeige():
            time.sleep(0.05)


if __name__ == "__main__":
    ki = KI_Spieler(3)
    ki.trainieren(5000)
    ki.pruefen()
    ki.vorfuehren()
