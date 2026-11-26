from Spielfeld import Spielfeld
import time

#KI-Spieler und Spieler sind zwei separate Klassen
#Bezug zum Spielfeld 

#Bezug zu AKTIONEN in Spielfeld.py
#Eingabe von Spielerzug über Konsole
#Überprüfung legaler Züge über Spielfeld
#Visualisierung über pygame in Spielfeld
#keine Reward Funktion - Hinweis nur über illegale Züge
#Ausgabe über gewonnene Spiele und Anzahl der Züge

class Spieler(Spielfeld):
    def __init__(self, anzahl_Spielsteine):
        super().__init__(anzahl_Spielsteine)
    def eingabe(self):
        start = None
        info = "Start-Stab wählen (Taste 1-3)"
        while True:
            if not self.zeige(info):
                return None
            for taste in self.tasten:
                if taste not in ("1", "2", "3"):
                    continue
                stab = int(taste) - 1
                if start is None:
                    start = stab
                    info = f"Von Stab {stab + 1} nach ... (Taste 1-3)"
                elif self.check_legal_move(start, stab):
                    return start, stab
                else:
                    info = "Ungültiger Zug! Start-Stab wählen (Taste 1-3)"
                    start = None
            time.sleep(0.02)

    def Spieler_aktion(self):
        zug = self.eingabe()
        if zug is None:
            return False
        self.zug_ausfuehren(*zug)
        return True

    def spielen(self):
        while not self.ist_geloest():
            if not self.Spieler_aktion():
                print("Spiel abgebrochen.")
                return
        self.zeige(f"Gewonnen in {self.zuege} Zügen! "
                   f"(optimal: {self.optimal_zuege})")
        print(f"Gewonnen in {self.zuege} Zügen!")
        time.sleep(3)