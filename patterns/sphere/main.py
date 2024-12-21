import math
import random
from colorsys import hls_to_rgb

from jelka import Jelka
from jelka.shapes import Sphere
from jelka.types import Color

color: Color


def init(jelka: Jelka):
    jelka.clear = True


def callback(jelka: Jelka):
    global color

    radius = math.fabs(math.sin(jelka.frame / jelka.frame_rate)) * 0.55 - 0.1
    sphere = Sphere(jelka.center_normalized, radius)

    if radius <= 0:
        hls = (random.uniform(0, 1), 0.5, 1)
        color = Color(*[int(i * 255) for i in hls_to_rgb(*hls)])

    for light, position in jelka.positions_normalized.items():
        if sphere.is_inside(position):
            intensity = (sphere.center - position).magnitude() / radius

            jelka.set_light(
                light,
                Color(
                    color.red * position.x * intensity,
                    color.green * position.y * intensity,
                    color.blue * position.z * intensity,
                ).vivid(),
            )


def main():
    jelka = Jelka(60)
    jelka.run(callback, init)


main()
