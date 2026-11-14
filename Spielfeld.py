import numpy as np

class Spielfeld():
    def __init__(self, anzahl_Spielsteine):
        self.anzahl_Spielsteine = anzahl_Spielsteine
        self.Feld = np.zeros([anzahl_Spielsteine, 3])
        self.create_spielfeld()

    def create_spielfeld(self):
                for i in range(0, self.anzahl_Spielsteine):
                    self.Feld[i, 0] = i+1

    def __str__(self):
        return str(self.Feld)
