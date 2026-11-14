import numpy as np

class Spielfeld():
    def __init__(self, anzahl_Spielsteine):
        self.anzahl_Spielsteine = anzahl_Spielsteine
        self.Feld = np.zeros([anzahl_Spielsteine, 3])
        self.create_spielfeld()

    def create_spielfeld(self):
        for i in range(0, self.anzahl_Spielsteine):
            self.Feld[i, 0] = i+1
    def check_legal_move(self, start, start_hoehe, ziel, ziel_hoehe):
        print(self.Feld[start_hoehe, start], self.Feld[ziel_hoehe, ziel])
        if start < 0 or start >= 3 or ziel < 0 or ziel >= 3:
            return False
        if start_hoehe < 0 or start_hoehe >= self.anzahl_Spielsteine or ziel_hoehe < 0 or ziel_hoehe >= self.anzahl_Spielsteine:
            return False
        if self.Feld[start_hoehe, start] == 0:
            return False
        if self.Feld[ziel_hoehe, ziel] != 0:
            return False
        if ziel_hoehe != self.anzahl_Spielsteine-1:
            if self.Feld[ziel_hoehe+1, ziel] < self.Feld[start_hoehe, start]:
                return False
        return True
    
    def __str__(self):
        return str(self.Feld)
