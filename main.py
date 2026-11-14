import Spielfeld

Feld = Spielfeld.Spielfeld(3)
print(Feld)
print(Feld.check_legal_move(0, 0, 2, 2))
print(Feld.check_legal_move(0, 0, 2, 1))
print(Feld.check_legal_move(0, 0, 2, 0))
print(Feld.check_legal_move(0, 0, 1, 2))

