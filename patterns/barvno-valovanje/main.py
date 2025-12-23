from jelka import Jelka
from jelka.types import Color


def wave(x):
    return abs(x - round(x))


def callback(jelka: Jelka):
    for light, position in jelka.positions_normalized.items():
        r = 8 * 255 * wave(position.z) * wave((jelka.elapsed_time + 2) / 4) * 10
        g = 2 * 255 * wave(position.z) * wave((jelka.elapsed_time) / 4) * 10
        b = 4 * 255 * wave(position.z) * wave((jelka.elapsed_time - 2) / 4) * 10

        jelka.set_light(
            light,
            Color(r % 256, g % 256, b % 256).vivid(),
        )


def main():
    jelka = Jelka(30)
    jelka.run(callback)


main()
