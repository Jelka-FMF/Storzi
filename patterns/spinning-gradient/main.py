import os
import random
import numpy as np


def hsv_to_hex(h, s, v):
    """
    Convert HSV color values to hexadecimal color code.

    :param h: Hue (0-360)
    :param s: Saturation (0-100)
    :param v: Value (0-100)
    :return: Hexadecimal color code
    """
    # Convert percentage-based saturation and value to 0-1 range
    s /= 100
    v /= 100

    # Convert hue to 0-1 range
    h /= 360

    # Calculate chroma
    c = v * s

    # Find intermediate value
    x = c * (1 - abs((h * 6) % 2 - 1))

    # Determine RGB values based on hue sector
    if 0 <= h < 1 / 6:
        r, g, b = c, x, 0
    elif 1 / 6 <= h < 1 / 3:
        r, g, b = x, c, 0
    elif 1 / 3 <= h < 1 / 2:
        r, g, b = 0, c, x
    elif 1 / 2 <= h < 2 / 3:
        r, g, b = 0, x, c
    elif 2 / 3 <= h < 5 / 6:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    # Add match value to adjust luminance
    m = v - c
    r, g, b = r + m, g + m, b + m

    # Convert to 0-255 range and then to hex
    return "{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))


lucke = []
with open(os.environ["JELKA_POSITIONS"]) as f:
    for line in f.readlines():
        split_line = line.strip().split(",")
        lucke.append([int(split_line[0]), float(split_line[1]), float(split_line[2]), float(split_line[3])])
lucke.sort(key=lambda x: x[0])  # Make sure the LED indices are in order
stevilo_luck = len(lucke)


def make_gradient(vector, h_start):
    global lucke

    def dot_prod(v1, v2):
        return sum([v1[i] * v2[i] for i in range(3)])

    products = np.empty(stevilo_luck)
    for i in range(stevilo_luck):
        products[i] = dot_prod(vector, lucke[i][1:])
    products = products + np.min(products)
    products = products / np.max(products)
    st = "#"
    for value in products:
        h = h_start + round(value * 120)  # One third of the color wheel
        h %= 360
        st += hsv_to_hex(h, 100, 100)
    return st


def random_vector(norm):
    v = np.array([random.random(), random.random(), random.random()])
    v = v / np.linalg.norm(v)
    return v * norm


print(f'#{{"version": 0, "led_count": {stevilo_luck}, "fps": 60}}')


h_start = random.randint(0, 360)
vector = random_vector(1)
while True:
    h_start += 1
    h_start %= 360
    vector = vector + random_vector(0.005)
    vector = vector / np.linalg.norm(vector)
    st = make_gradient(vector, h_start)
    print(st, flush=True)
