import numpy as np


class Spielfeld():
    Hintergrund = (30, 30, 46)
    Boden = (90, 90, 110)
    Stab = (160, 160, 180)
    Text = (230, 230, 240)
    FARBEN = [(230, 80, 80), (240, 160, 60), (230, 220, 70),
              (80, 200, 110), (70, 170, 230), (150, 100, 230)]

    def __init__(self, anzahl_Spielsteine):
        self.anzahl_Spielsteine = anzahl_Spielsteine
        self.Feld = np.zeros([anzahl_Spielsteine, 3], dtype=int)
        self.create_spielfeld()
        self._fenster = None  

    def create_spielfeld(self):
        self.zuege = 0
        for i in range(0, self.anzahl_Spielsteine):
            self.Feld[i, 0] = i+1

    def oberster_ring(self, stab):
        for zeile in range(self.anzahl_Spielsteine):
            if self.Feld[zeile, stab] != 0:
                return zeile
        return None

    def check_legal_move(self, start, ziel):
        if start < 0 or start >= 3 or ziel < 0 or ziel >= 3:
            return False
        if start == ziel:
            return False
        start_zeile = self.oberster_ring(start)
        if start_zeile is None:
            return False
        ziel_zeile = self.oberster_ring(ziel)
        if ziel_zeile is not None:
            if self.Feld[ziel_zeile, ziel] < self.Feld[start_zeile, start]:
                return False
        return True

    def __str__(self):
        return str(self.Feld)


    def fenster_oeffnen(self, breite=900, hoehe=420):
        import pygame as pg  
        self.pg = pg
        pg.display.init()
        pg.font.init()
        self._screen = pg.display.set_mode((breite, hoehe))
        pg.display.set_caption("Türme von Hanoi")
        self._breite = breite
        self._boden_y = hoehe - 60
        self._ring_h = min(35, (self._boden_y - 100) // (self.anzahl_Spielsteine + 1))
        self._max_breite = breite // 4 - 20
        self._min_breite = 40
        self._font = pg.font.Font(None, 36)
        self._fenster = True

    def zeige(self, info=None):
        if self._fenster is None:
            self.fenster_oeffnen()
        pg, screen, n = self.pg, self._screen, self.anzahl_Spielsteine
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.display.quit()
                self._fenster = None
                return False
        screen.fill(self.Hintergrund)
        pg.draw.rect(screen, self.Boden, (30, self._boden_y, self._breite - 60, 10))
        for s in range(3):
            x = self._breite * (s + 1) // 4
            stab_h = (n + 1) * self._ring_h
            pg.draw.rect(screen, self.Stab, (x - 4, self._boden_y - stab_h, 8, stab_h))
            for zeile in range(n):
                wert = self.Feld[zeile, s]
                if wert != 0:
                    b = self._min_breite + wert * (self._max_breite - self._min_breite) // n
                    y = self._boden_y - (n - zeile) * self._ring_h + 2
                    pg.draw.rect(screen, self.FARBEN[wert % len(self.FARBEN)],
                                 (x - b // 2, y, b, self._ring_h - 4), border_radius=8)
        text = self._font.render(f"Züge: {self.zuege}", True, self.Text)
        screen.blit(text, (20, 15))
        pg.display.flip()
        return True
