import math
import random

import numpy as np
from jelka import Jelka
from jelka.shapes import Sphere
from jelka.types import Color, Position

# Play around with these parameters
firework_count = 3  # Number of fireworks visible at the same time
firework_lifetime = 42  # Number of frames that a single firework is visible for
expand_speed = 5  # How fast the fireworks expand (not a linear multiplier)
disappear_speed = 1  # How fast the center disappears (is a linear multiplier)
radius = 0.4  # Size of fireworks in range [0, 1]

# Frames between two spawns of fireworks
spawn_offset = firework_lifetime // firework_count

firework_positions = [(0, 0)] * firework_count
firework_colors = [Color(0, 0, 0)] * firework_count


def brighten_color(color: Color) -> Color:
    """Scale up all values so that at least one of the components is 255"""
    mx = 255 / max(*color)
    return Color(*map(lambda x, s: int(x * s), color, (mx, mx, mx)))


def init(jelka: Jelka):
    jelka.clear = True


def callback(jelka: Jelka):
    global firework_positions
    global firework_colors

    looped_frames = [0] * firework_count
    for i in range(firework_count):
        looped_frames[i] = (jelka.frame + i * spawn_offset) % firework_lifetime + 1  # +1 to skip size 0
        if looped_frames[i] == 1:
            firework_positions[i] = (np.random.normal(loc=0.42, scale=0.3), random.uniform(-1, 1))
            firework_colors[i] = brighten_color(Color.random().vivid())

    def radius_function(z: float) -> float:
        return 1 / 2 - z / 2

    def firework_pos_function(za: tuple[float, float]) -> Position:
        """Pass a tuple of height and angle around vertical, it will calculate the firework position on the surface of the tree"""
        origin = jelka.center_normalized - Position(0, 0, -jelka.center_normalized.z)
        offset = Position(radius_function(za[0]) * math.cos(za[1] * 20), radius_function(za[0]) * math.sin(za[1] * 20), za[1])
        return origin + offset

    def firework_radius_function(t: float) -> float:
        """Pass a time, it will calculate the radius of the firework"""
        return 1 / (1 + math.exp(-t * expand_speed)) * radius

    def firework_small_radius_function(t: float) -> float:
        """Pass a time, it will calculate the radius of the disappearing center"""
        return t * radius * disappear_speed

    # Spheres expand with time
    spheres = [
        Sphere(firework_pos_function(firework_positions[i]), firework_radius_function(looped_frames[i] / firework_lifetime))
        for i in range(firework_count)
    ]

    # Smaller spheres for a disappearing center
    spheres_small = [
        Sphere(firework_pos_function(firework_positions[i]), firework_small_radius_function(looped_frames[i] / firework_lifetime))
        for i in range(firework_count)
    ]

    for light, position in jelka.positions_normalized.items():
        summed_color = Color(0, 0, 0)
        summed_count = 0

        for i in range(firework_count):
            if spheres[i].is_inside(position) and not spheres_small[i].is_inside(position):
                summed_color += firework_colors[i]
                summed_count += 1

        if summed_count > 0:
            # Average together colors from fireworks that intersect
            jelka.set_light(light, summed_color / summed_count)


def main():
    jelka = Jelka(60)
    jelka.run(callback, init)


main()
