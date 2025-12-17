import os


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


with open(os.environ["JELKA_POSITIONS"]) as file:
    n = len(file.readlines())

print(f'#{{"version": 0, "led_count": {n}, "fps": 60}}')

h = 0
while True:
    h += 1
    h %= 360
    st = "#"
    for i in range(n):
        st += hsv_to_hex((h + i) % 360, 100, 100)
    print(st, flush=True)
