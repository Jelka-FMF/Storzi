import math
import random

from jelka import Jelka
from jelka.types import Color


class Snežinka:

    def __init__(self, x, y, v_x, v_y_max, radius, odmik=0):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y_max = v_y_max
        self.timer = 0  # frames
        self.radius = radius
        self.odmik = odmik
        self.barva = random.randrange(70)
    

    def update(self):
        self.v_x = 2*self.v_y_max * math.sin(self.timer/30 + self.odmik)
        self.v_y = self.v_y_max * (abs(math.cos(self.timer/30 + self.odmik))) ** (1/2)
        self.x += self.v_x
        self.y -= self.v_y
        self.timer += 1
        if self.y < -self.radius:
            self.x = random.uniform(-math.pi, math.pi)
            self.y = 1 + self.radius
        

def init(jelka: Jelka):
    global m, M, center_x, center_y, snežinke

    višine = []
    iksi = []
    ipsiloni = []
    for _, j in jelka.positions_normalized.items():
        višine.append(j.z)
        iksi.append(j.x)
        ipsiloni.append(j.y)
    M = max(višine)
    m = min(višine)

    center_x = sum(iksi)/len(iksi)
    center_y = sum(ipsiloni)/len(ipsiloni)

    # parametri za spreminjat
    radius = 0.25  # polmer snežinke
    horizontalna_hitrost_na_začetku = 0.005
    max_vertikalna_hitrost = 0.005

    snežinke = []
    št_snežink_x = 5
    št_snežink_y = 4
    for i in range(št_snežink_x):
        for j in range(št_snežink_y):
            snežinke.append(Snežinka(-math.pi + 2*math.pi * ((i + random.uniform(-0.5, 0.5))/št_snežink_x), -radius + (1 + 2*radius)*((j + 1 + random.uniform(-0.5, 0.5))/št_snežink_y), horizontalna_hitrost_na_začetku, max_vertikalna_hitrost, radius, random.uniform(0, 2*math.pi)))


def pretvori_lučko_v_kvadrat(pozicija_lučke):
    # m je višina najnižje lučke, M višina najvišje

    x, y, z = pozicija_lučke.x, pozicija_lučke.y, pozicija_lučke.z
    # assert m <= z <= M
    y_ = (z - m)/(M - m)  # normalizirana višina

    x_ = math.atan2(y - center_y, x - center_x)  # kot je na intervalu [-pi, pi]

    return x_, y_  # element [-pi, pi] x [0, 1]


def znotraj_snežinke(x, y):
    for i in snežinke:
        X, Y = i.x, i.y
        if ((x - X)*2/3) ** 2 + (2.5*(y - Y)) ** 2 <= i.radius ** 2:
            return True, i.barva
    return False, None


def callback(jelka: Jelka):
    for i, j in jelka.positions_normalized.items():
        x, y = pretvori_lučko_v_kvadrat(j)
        if (a := znotraj_snežinke(x, y))[0]:
            jelka.set_light(i, Color(255 - a[1], 255 - a[1], 255 - a[1]))
        else:
            jelka.set_light(i, Color(0, 0, 0))
    
    for i in snežinke:
        i.update()


def main():
    jelka = Jelka(60)
    jelka.run(callback, init)


main()
