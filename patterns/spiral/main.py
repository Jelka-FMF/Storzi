import math
from typing import List

from jelka import Jelka
from jelka.shapes import Sphere
from jelka.types import Color, Position

normalized: List[Position]
color: Color


def init(jelka: Jelka):
    global normalized

    normalized = [Position(0, 0, 0)] * jelka.number_of_lights

    min_x = jelka.bounds_raw.min_x
    max_x = jelka.bounds_raw.max_x
    min_y = jelka.bounds_raw.min_y
    max_y = jelka.bounds_raw.max_y
    min_z = jelka.bounds_raw.min_z
    max_z = jelka.bounds_raw.max_z

    for light, position in jelka.positions_raw.items():
        normalized[light] = Position(
            (position.x - min_x) / (max_x - min_x + 0.01),
            (position.y - min_y) / (max_y - min_y + 0.01),
            (position.z - min_z) / (max_z - min_z + 0.01),
        )


def callback(jelka: Jelka):
    global color

    height = 1 - 0.0075 * (jelka.frame % 150)

    if height == 1:
        color = Color.vivid(Color.random())

    rad = 1 / 2 - height / 2
    x = 0.5 + rad * math.cos(height * 20)
    y = 0.5 + rad * math.sin(height * 20)

    sphere = Sphere((x, y, height), 0.1)

    for i in range(len(jelka.lights)):
        position = normalized[i]
        if sphere.is_inside(position):
            jelka.set_light(i, color)
        # else:
        #   jelka.set_light(i, Color(0, 0, 0))


def main():
    jelka = Jelka(60)
    jelka.run(callback, init)


main()
