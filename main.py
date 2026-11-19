from Spielfeld import Spielfeld

Feld = Spielfeld(3)
print(Feld)
print(Feld.check_legal_move(0, 2))   
print(Feld.check_legal_move(1, 2))   
print(Feld.check_legal_move(0, 0))   
print(Feld.check_legal_move(0, 3))  
 

from Spieler import Spieler

Spieler(3).spielen()

while Feld.zeige():
    pass
