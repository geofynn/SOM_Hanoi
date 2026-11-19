from Spielfeld import Spielfeld

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
        while True:
            try:
                start = int(input("Von Stab (1-3): ")) - 1
                ziel = int(input("Auf Stab (1-3): ")) - 1
            except ValueError:
                print("Bitte eine Zahl eingeben.")
                continue

            if self.check_legal_move(start, ziel):
                return start, ziel
            print("Ungültiger Zug, bitte nochmal eine Zahl eingeben.")

    def Spieler_aktion(self):
        start, ziel = self.eingabe()
        self.zug_ausfuehren(start, ziel)
        

    def spielen(self):
        self.zeige()                      # Fenster öffnen, Startposition zeigen
        while not self.ist_geloest():
            self.Spieler_aktion()         # Zug in der Konsole eingeben
            self.zeige()                  # Fenster nach dem Zug neu zeichnen
        print(f"Gewonnen in {self.zuege} Zügen! "
              f"(optimal: {2 ** self.anzahl_Spielsteine - 1})")
        
        return