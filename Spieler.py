import Spielfeld

class Spieler(Spielfeld):
    def __init__(self, anzahl_Spielsteine):
        super().__init__(anzahl_Spielsteine)
    def Spieler_aktion(self, start, ziel):
        return