import numpy as np

class Spielfeld():
    def __init__(self, anzahl_Spielsteine=3):
        self.anzahl_Spielsteine = anzahl_Spielsteine
        self.Feld = np.zeros([3, 3])
        self.create_spielfeld()

    def create_spielfeld(self):
        for i in range(self.anzahl_Spielsteine, 0):
            self.Feld[0, i] = i
    def __str__(self):
        
        return str(self.Feld)


Feld = Spielfeld()
#TEst = np.zeros([3,3])
#print(TEst)
print(Feld)