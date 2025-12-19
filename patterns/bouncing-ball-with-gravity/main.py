import numpy as np
from jelka import Jelka
from jelka.types import Color
from opt_einsum import contract as opt_einsum
from scipy.interpolate import CubicSpline

jelka = Jelka(60)

####################################### TU SO NASTAVLJIVI PARAMETRI

v0 = np.array([0.1, 0.2, 0.1])  # Začetna hitrost krogle
radius = 0.1  # Radij krogle

gravity = 1  # Gravitacijski pospešek

tmax = 100  # Čas v sekundah preden se vzorec ponovi
dt = 0.001  # Časovni korak integracije (mora biti majhen, sicer krogla prebije steno)

#######################################


##### Predprocesiranje roba jelke

s = 0
N = 0
for light, position in jelka.positions_normalized.items():
    s += np.array(position)
    N += 1

a = 0.35  # Manualno fitani parametri
h = 1.15
bottom = 0.36

center_of_mass = s / N
r0 = np.copy(center_of_mass)

center_of_mass[2] = 0  # Hočemo središče samo na 2D ravnini, ne v višini


#######


def get_trajectory(r0, v0, dt, tmax):
    ts = np.arange(0, tmax, dt)
    rs = np.zeros((len(ts), 3))
    vs = np.zeros((len(ts), 3))

    rs[0, :] = r0
    vs[0, :] = v0
    for i in range(1, len(ts)):
        r = rs[i - 1, :] + dt * vs[i - 1, :]
        r, v = reflect_from_actual_cone(r, vs[i - 1, :], dt)
        rs[i, :] = r
        vs[i, :] = v - gravity * dt

    print(rs)

    return CubicSpline(ts, rs)


def is_in_ball(radij, pozicija, r):
    return radij**2 > (pozicija[0] - r[0]) ** 2 + (pozicija[2] - r[2]) ** 2 + (pozicija[1] - r[1]) ** 2


def reflect_from_actual_cone(r, v, timestep):
    rel_position = r - center_of_mass
    x, y, z = rel_position

    if z < bottom:
        # print("bottom")
        r = r - v * timestep
        v[2] = -v[2]

    elif z > 0.9:  # Da se ne zatakne na vrhu
        # print("vrh")
        r = r - v * timestep
        v[2] = -v[2]

    elif x**2 + y**2 > (a * (z - h)) ** 2 and z < 500:
        # Da se ne zatakne v kotu odbijemo od valja
        normal_vector = np.array([x / np.sqrt(x**2 + y**2), y / np.sqrt(x**2 + y**2), 0])

        # Standardna formula za zraljenje vzdolž vektorja
        v_mirrored = v - 2 * opt_einsum("i,i,j->j", v, normal_vector, normal_vector)
        v = v_mirrored

    elif x**2 + y**2 > (a * (z - h)) ** 2:
        # print("side")
        r = r - v * timestep

        # Vektor pravokoten na stožec
        normal_vector = 1 / np.sqrt(1 + a**2) * np.array([x / np.sqrt(x**2 + y**2), y / np.sqrt(x**2 + y**2), -a])

        # Standardna formula za zrcaljenje vzdolž vektorja
        v_mirrored = v - 2 * opt_einsum("i,i,j->j", v, normal_vector, normal_vector)
        v = v_mirrored

    return r, v


r_func = get_trajectory(r0, v0, dt=dt, tmax=tmax)


def callback(jelka: Jelka):
    t = (jelka.frame / 60) % tmax
    r = r_func(t)

    for light, position in jelka.positions_normalized.items():
        if np.linalg.norm(np.array(position) - r) < radius:
            jelka.set_light(light, Color(255, 255, 255))
        else:
            jelka.set_light(light, Color(0, 0, 0))


jelka.run(callback)
