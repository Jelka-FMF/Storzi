from colorsys import hsv_to_rgb

from jelka import Jelka
from jelka.types import Color


def f(x, m):
    k = 0.5
    y = k * x + m
    return y


def callback(jelka: Jelka):
    a = jelka.elapsed_time / 2 % 1
    b = a + 0.2
    c = a - 0.2
    cl1, cl2, cl3 = hsv_to_rgb(a, 1, 1)
    dl1, dl2, dl3 = hsv_to_rgb((a + 0.5) % 1, 1, 1)
    for light, position in jelka.positions_normalized.items():
        if position.z > f(position.x, a) and position.z < f(position.x, b):
            jelka.set_light(light, Color(cl1 * 255, cl2 * 255, cl3 * 255))
        elif position.z < f(position.x, a) and position.z > f(position.x, c):
            jelka.set_light(light, Color(dl1 * 255, dl2 * 255, dl3 * 255))
        else:
            jelka.set_light(light, Color(0, 0, 0))


def main():
    jelka = Jelka(60)
    jelka.run(callback)


main()
