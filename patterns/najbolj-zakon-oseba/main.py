import math

from jelka import Jelka
from jelka.types import Color

# funkcije bi lahko bile razdeljene med več datotek, ampak niso, zato je z
# ____
# ####
# označeno, kdaj bi morala biti druga datoteka


# stickman______________________________________________________________________________________________________
################################################################################################################
def krogla(position, x0, z0, r):
    # (x0, y0) - središče krogle
    x, _, z = position
    return (x - x0) ** 2 + (z - z0) ** 2 < r**2


def palca(position, x0, z0, fi, h, d):
    # (x0, y0) - začetek palice
    # fi - rotacija palice od (1,0) v pozitivni smeri
    # h - dolžina palice
    # d - debelina palice
    x, _, z = position
    ravnina = (x - x0) * math.sin(fi) + (z - z0) * (-math.cos(fi))  # ravnina kjer leži palica
    odsekovna_ravnina = (x - x0) * math.cos(fi) + (z - z0) * math.sin(fi)  # ravnina pravokotna na palico
    return abs(ravnina) < d and 0 < odsekovna_ravnina < h


def stickman(jelka, position, s, h, fin, fir, d):
    # s - premik centra po z osi
    # (x0, y0) - center lociran v mednožju
    # fin - kot palice za nogo
    # fir - kot palice za roko
    # d - debelina črt
    # position - koordinata lučke
    x0, _, z0 = jelka.center_normalized
    z0 += s
    dvig = h / 2  # koliko je središče glave oddaljeno od centra v mednožju
    gx, gz = x0, z0 + dvig  # koordinate glave
    rx, rz = x0, z0 + h / 3  # koordinate ramen (izhodišče rok)
    lenght = h / 2  # dolžina rok in nog
    return (
        krogla(position, gx, gz, h / 6)  # glava
        or palca(position, rx, rz, fir, lenght, d)  # roka na desni
        or palca(position, rx, rz, math.pi - fir, lenght, d)  # roka na levi
        or palca(position, x0, z0, math.pi - fin, lenght, d)  # noga na levi
        or palca(position, x0, z0, fin, lenght, d)  # noga ne desni
        or palca(position, x0, z0, math.pi / 2, dvig, d)  # telo
    )


# Črke _________________________________________________________________________________________________________
################################################################################################################
# POZOR!: funkcije črk so bile napisane preden sem napisala funkcijo palca,
# zato bi se jih dalo napisati na lepši način, ampak nočem


def vcrka(jelka, position, s, d, h):
    # (x0, z0) - konica V
    # s - premik po z osi
    # position - koordinata lučke
    # d - debelina črt
    # h - višina črke
    x, _, z = position
    x0, _, z0 = jelka.center_normalized
    z0 += s
    fi = math.pi / 2 - math.pi / 3
    # fi - kot med (1, 0) in normalo leve ravnine V-ja (normala kaže desno gor)

    # oddaljenost točke do ravnine
    desna_ravnina = (x - x0) * (-math.cos(fi)) + (z - z0) * math.sin(fi)  # /
    leva_ravnina = (x - x0) * math.cos(fi) + (z - z0) * math.sin(fi)  # \

    pogoji = (abs(desna_ravnina) < d or abs(leva_ravnina) < d) and (h + z0 > z > z0)  # odsekamo lučke, ki so previsoko

    return pogoji


def icrka(jelka, position, s, d, h):
    # (x0, z0) - čisto spodnji del I-ja
    # s - premik po z osi
    # position - koordinata lučke
    # d - debelina črte
    # h - višina črke
    x, _, z = position
    x0, _, z0 = jelka.center_normalized
    z0 += s

    pogoji = abs(x - x0) < d and (z0 < z < z0 + h)
    return pogoji


def dcrka(jelka, position, s, d, h):
    # (x0, z0) - čisto spodnji levi del D-ja
    # s - premik po z osi
    # position - koordinata lučke
    # d - debelina črt
    # h - višina črke
    x, _, z = position
    x0, _, z0 = jelka.center_normalized
    dx = h / 5  # Zamik črke v levo
    x0 -= dx
    z0 += s

    r = h / 2  # polmer krožnice za trebušček D ja (večji del)
    xk, _, zk = x0 + d, _, z0 - s / 2 + d  # središče krožnice

    crta = (abs(x - x0) < d) and (z0 < z < z0 + h)  # ravni del D-ja
    polkrog = (
        (r - d) ** 2 < ((x - xk) ** 2 + (z - zk) ** 2) < (r) ** 2  # krožnica trebuščka D-ja
        and x0 < x
    )  # krožnoca samo desno od rvnega dela D-ja
    pogoji = crta or polkrog
    return pogoji


def acrka(jelka, position, s, d, h):
    # (x0, z0) - čisto zgornji del A-ja
    # s - premik po z osi
    # position - koordinata lučke
    # d - debelina črt
    # h - višina črke
    x, _, z = position
    x0, _, z0 = jelka.center_normalized
    z0 += s + h
    fi = math.pi / 2 - math.pi / 3
    # fi - kot med (1, 0) in normalo desne ravnine A-ja
    rz = z0 - 2 * h / 3  # središče črtice A (samo z oordinata je potebna, ostalo je defoltno)

    prva_crta = (x - x0) * math.cos(fi) + (z - z0) * math.sin(fi)  # \
    druga_crta = (x - x0) * (-math.cos(fi)) + (z - z0) * math.sin(fi)  # /
    crtica = z - rz  # -

    pogoji = (
        (
            abs(prva_crta) < d  # \
            or abs(druga_crta) < d  # /
        )
        and (0 - h < z < z0)
    ) or (
        abs(crtica) < d  # ravnina crtice
        and (prva_crta < 0 and druga_crta < 0)  # crtica med /\
    )
    return pogoji


# Izvajajoč del ________________________________________________________________________________________________
################################################################################################################
# funkcija ki se izvede na začetku
def init(jelka: Jelka):
    global barva, odzadje  # global, da lahko uporabljamo to spremenljivko v funkciji `callback`
    barva = Color(255, 0, 255)  # barva črk: Vijolična (ena mojih najljubših barv)
    odzadje = Color(0, 155, 0)  # zelena

    d = 0.035  # debelina črt črk
    h = 0.35  # višina črk
    s = -0.3  # zamik izhodišč črk iz centra (jelka.center_normalize) po z osi

    h_stick = 0.475  # višina stickmana (bolj približek višine. Uporablja se bolj kot scale)
    s_stick = -0.15  # zamik izhodišča stickmana (mednožje) iz centra (jelka.center_normalize) po z osi
    d_stick = d  # debelina črt stickmana
    fin = -math.pi / 3  # kot med (1, 0) in nogo stickmana
    fir = -math.pi / 6  # kot med (1, 0) in roko stickmana

    # ustvarjanje seznamov lučk objektov (črke in stickman)
    global sezv, sezi, sezd, seza
    global sez_stickman

    sezv, sezi, sezd, seza = [], [], [], []
    sez_stickman = []

    # funkcije črk in stickmana vzamejo pozicijo lučke in vrnejo, če lučka leži v objektu
    # v sezname zberemo vse lučke, ki ležijo v posameznem objektu
    for light, position in jelka.positions_normalized.items():
        if vcrka(jelka, position, s, d, h):
            sezv.append(light)
        if icrka(jelka, position, s, d, h):
            sezi.append(light)
        if dcrka(jelka, position, s, d, h):
            sezd.append(light)
        if acrka(jelka, position, s, d, h):
            seza.append(light)
        if stickman(jelka, position, s_stick, h_stick, fin, fir, d_stick):
            sez_stickman.append(light)


# funkcija ki se kliče vsak frame
def callback(jelka: Jelka):
    t = (jelka.frame // 60) % 5
    # z `jelka.frame // 60` kontroliram koliko časa bo trajala posamezna slika (1s, ker je frame_rate = 60)
    # `... & 5` razdelim čas na 5 slik

    # POZOR!: Lahko bi prilagodila frame_rate na 1 in ne bi rabila deliti z 60,
    # ampak če bila kakšna moja slika nestatična (na primer rotirajoča ravnina),
    # se premikanje na sliki ne bi kazalo

    for j in range(jelka.number_of_lights):  # nastavi vse lučke na barvo odzadja
        jelka.set_light(j, odzadje)

    # pokaži lučke iz seznamov objektov odvisno na kateri sliki je program
    if t == 0:
        for light in sezv:
            jelka.set_light(light, barva)  # vsako lučko iz seznama nastavi na barvo
    elif t == 1:
        for light in sezi:
            jelka.set_light(light, barva)
    elif t == 2:
        for light in sezd:
            jelka.set_light(light, barva)
    elif t == 3:
        for light in seza:
            jelka.set_light(light, barva)
    elif t == 4:
        for light in sez_stickman:
            jelka.set_light(light, barva)


def main():
    jelka = Jelka(60, Color(0, 155, 0))  # lahko podamo frame_rate in initial_color (barva celotne jelke čisto na začetku vzorca)
    jelka.run(callback, init)


main()
