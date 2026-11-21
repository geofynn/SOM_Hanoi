from Spielfeld import Spielfeld

Feld = Spielfeld(3)
print(Feld)
print(Feld.check_legal_move(0, 2))   
print(Feld.check_legal_move(1, 2))   
print(Feld.check_legal_move(0, 0))   
print(Feld.check_legal_move(0, 3))  
 

while Feld.zeige():
    pass
