from Spieler import Spieler
from KI_Spieler import KI_Spieler


def zahl_abfragen(text, minimum, maximum):
    while True:
        try:
            zahl = int(input(text))
        except ValueError:
            print("Bitte eine Zahl eingeben.")
            continue
        if minimum <= zahl <= maximum:
            return zahl
        print(f"Bitte eine Zahl zwischen {minimum} und {maximum} eingeben.")


print("Türme von Hanoi")
print("1 = selbst spielen")
print("2 = KI trainieren und spielen lassen")
modus = zahl_abfragen("Modus: ", 1, 2)
anzahl = zahl_abfragen("Anzahl Scheiben (3-5): ", 3, 5)

if modus == 1:
    spieler = Spieler(anzahl)
    spieler.spielen()
else:
    ki = KI_Spieler(anzahl)
    ki.trainieren(5000 * 2 ** (anzahl - 3))     # mehr Scheiben -> mehr Training
    ki.vorfuehren()