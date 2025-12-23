import math

from jelka import Jelka
from jelka.types import Color

nova = (255, 0, 0)
stara = (0, 255, 0)
tretja = (0, 0, 255)
mz = 0


def callback(jelka: Jelka):
    global stara, nova, tretja, mz
    t = jelka.elapsed_time
    tz = t / 5 - mz
    ta = 10 * t % (2 * math.pi)

    vse_nove = True

    for light, position in jelka.positions_normalized.items():
        x, y, z = position
        cx, cy, cz = jelka.center_normalized
        r, g, b = (
            (position[0] * 255 + math.tan((jelka.elapsed_time % 4) / 4) * 255 + 256) % 256,
            (position[0] * 255 + math.tan((jelka.elapsed_time % 4) / 4) * 255 + 256) % 256,
            (position[0] * 255 + math.tan((jelka.elapsed_time % 4) / 4) * 255 + 256) % 256,
        )
        l = math.atan2(y - cy, x - cx)
        k = (ta - l) % (2 * math.pi)
        if position.z > tz:
            r, g, b = stara
            vse_nove = False
        elif tz - 0.02 * k > z:
            r, g, b = nova
        else:
            r, g, b = stara
            vse_nove = False
        jelka.set_light(
            light,
            Color(r % 256, g % 256, b % 256).vivid(),
        )
    if vse_nove:
        nova, stara, tretja = tretja, nova, stara
        mz = t / 5 - jelka.bounds_normalized.min_z


def main():
    jelka = Jelka(30)
    jelka.run(callback)


main()
