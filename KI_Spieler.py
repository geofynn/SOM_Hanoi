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
class KI_Spieler(Spielfeld):
    def __init__(self, anzahl_Spielsteine):
        super().__init__(anzahl_Spielsteine)

    def get_state(self):
        state = 0
        for zeile in range(0,self.anzahl_Spielsteine):
            for stab in range(3):
                wert = self.Feld[zeile,stab]
                if wert !=0:
                    state += stab*3**(wert-1)
        return state

    def KI_aktion(self, start, ziel):   
        return
 
#Bezug zu AKTIONEN in Spielfeld.py
#Bezug zu state und action 
#training: keine Visualisierung, nur Berechnung der Züge und Rewards; Pause benötigt, um die Züge zu sehen
#Belohnung bei optimalen Zügen (optimaler Zug = 2^Anzahl_Spielsteine - 1)
#Vorführfunktion: Visualisierung über pygame in Spielfeld
#Lernerfolg prüfen?