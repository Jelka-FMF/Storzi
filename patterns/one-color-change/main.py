from colorsys import hsv_to_rgb, rgb_to_hsv

from jelka import Jelka
from jelka.types import Color


def callback(jelka: Jelka):
    for i in range(jelka.number_of_lights):
        hue = rgb_to_hsv(jelka.lights[i].red, jelka.lights[i].green, jelka.lights[i].blue)[0] * 360
        hue = (hue + 1) % 360

        color = hsv_to_rgb(hue / 360.0, 1.0, 1.0)
        color = tuple(map(lambda x: int(x * 255), color))
        jelka.set_light(i, Color(*color))


def main():
    jelka = Jelka(60)
    jelka.run(callback)


main()
