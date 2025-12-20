import numpy as np
from jelka import Jelka
from jelka.types import Color

M = np.array(
    [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    ]
)

F = np.array(
    [
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)

blank = np.zeros_like(F)

s = [
    (F, 10, np.array([[0.5, 1, 1]])),
    (M, 10, np.array([[0.5, 1, 0.6]])),
    (F, 10, np.array([[0.7, 0.5, 1]])),
    (blank, 10, np.array([[0, 0, 0]])),
]

pos: np.ndarray


def init(jelka: Jelka):
    global pos

    pos = np.array([(p.x, p.y, p.z) for p in jelka.positions_raw.values()])
    dists = np.linalg.norm(pos, axis=1)
    radius = float(dists.max()) if dists.size else 0.0

    if radius > 0.0:
        pos = pos / radius * 200.0


def callback(jelka: Jelka):
    t = jelka.frame

    total_duration = sum([d for _, d, _ in s])
    T = t % total_duration
    tt = 0
    idx = 0

    for i, (_, duration, _) in enumerate(s):
        tt += duration
        if tt > T:
            idx = i
            break

    img, duration, c = s[idx]

    fi = t // total_duration * 0.3

    uu = np.array([[np.sin(fi), np.cos(fi), 0]])
    vv = np.array([[0, 0, 1]])

    u = (pos @ uu.T).flatten()
    v = (pos @ vv.T).flatten()

    h = 130
    w = 100

    i = np.round((v / h) * img.shape[0]).astype(int)
    j = np.round(((u + w / 2) / w) * img.shape[1]).astype(int)
    ok = (i >= 0) & (i < img.shape[0]) & (j >= 0) & (j < img.shape[1])

    col = np.zeros((len(u), 3))
    col[:, :] = np.array([0.0, 0.0, 0.0])
    col[ok] = (img[-i[ok], j[ok]] * c.T).T

    col[pos[:, 2] > 175] = np.array([1, 1, 0.4])

    for i, c in enumerate(col):
        jelka.set_light(i, Color(c[0] * 255, c[1] * 255, c[2] * 255))


def main():
    jelka = Jelka(25)
    jelka.run(callback, init)


main()
