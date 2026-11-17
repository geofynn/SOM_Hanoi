from Spielfeld import Spielfeld

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
        
        return