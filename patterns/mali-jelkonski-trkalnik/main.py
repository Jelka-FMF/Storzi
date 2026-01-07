import random

from jelka import Jelka
from jelka.types import Color
from colorsys import hsv_to_rgb

# import sys
# print(,file=sys.stderr)

## Konfiguracija
hitrostDelcev = 80  # luck/s
dolzinaRepov = 20  # luck
hitrostEksplozije = 0.4  # delez velikosti jelke / s
debelinaEksplozije = 0.3  # delez r na noter

## Debug

# def pobarvajSivoDebug(jelka):
#     for light, position in jelka.positions_normalized.items():
#         jelka.set_light(
#             light,
#             Color(40,40,40)
#         )
# vrsteTrue= list()


## Funkcije
def formulaDelca(x, dolzina):
    if x < 0.5:
        return 1
    else:
        k = 1 / dolzina
        return (x - 0.5) * (-k) + 1


def narisiDelec(jelka: Jelka, stLuck, pozicija, dolzinaRepa, barva, smerNazaj):
    for lucka in range(
        max(0, int(pozicija) - 1 - dolzinaRepa),  # OD
        min(stLuck, int(pozicija) + 1 + dolzinaRepa),  # DO
    ):
        # print(pozicija - lucka, file=sys.stderr)
        koeficientSvetlosti = max(0, formulaDelca(abs(lucka - pozicija), dolzinaRepa))

        # print(lucka-pozicija,formulaDelca(pozicija-lucka,dolzinaRepa), file=sys.stderr)
        barva2 = Color(*(koeficientSvetlosti * a for a in barva.to_tuple()))
        jelka.set_light(lucka, barva2)

        # print('luckam', smerNazaj,lucka, barva2, pozicija ,file=sys.stderr)
        # if smerNazaj: vrsteTrue.append(int(pozicija))


# - <-nazaj         naprej-> +
# smerNazaj: kam kaze glava (rep v drugo)


def narisiSfero(jelka: Jelka, koordinate, zunanjiR, notranjiR, barva1, barva2):
    zunanjiR2 = zunanjiR**2
    notranjiR2 = notranjiR**2
    for light, position in jelka.positions_normalized.items():
        x, y, z = position
        x0, y0, z0 = koordinate

        x1, x2, x3 = x - x0, y - y0, z - z0

        r2 = x1**2 + x2**2 + x3**2

        if r2 < zunanjiR2 and r2 > notranjiR2:
            jelka.set_light(light, random.choice((barva1, barva2)))


## Glavni loop
def glavnaZanka(jelka: Jelka):
    while True:
        ### Izbere barve in parametre

        # barva 1
        hue1 = random.randint(0, 255)

        color = hsv_to_rgb(hue1 / 255.0, 1.0, 1.0)
        color = tuple(map(lambda x: int(x * 255), color))
        barva1 = Color(*color)

        # barva 2
        hue2 = random.randint(0, 255)

        color = hsv_to_rgb(hue2 / 255.0, 1.0, 1.0)
        color = tuple(map(lambda x: int(x * 255), color))
        barva2 = Color(*color)

        stLuck = jelka.number_of_lights
        luckaTrcenja = random.randint(0, int(stLuck / 2)) + int(stLuck / 4)

        ### Potovanje
        cas = jelka.elapsed_time
        casTrcenja = cas + (max(stLuck - luckaTrcenja, luckaTrcenja) / hitrostDelcev)

        while cas < casTrcenja:
            # pobarvajSivoDebug(jelka)
            pozicija1 = luckaTrcenja - (casTrcenja - cas) * hitrostDelcev
            pozicija2 = luckaTrcenja + (casTrcenja - cas) * hitrostDelcev

            # print(pozicija1, pozicija2, luckaTrcenja, cas, casTrcenja, file=sys.stderr)

            narisiDelec(jelka, stLuck, pozicija1, dolzinaRepov, barva1, smerNazaj=False)
            narisiDelec(jelka, stLuck, pozicija2, dolzinaRepov, barva2, smerNazaj=True)

            yield
            cas = jelka.elapsed_time

        ## Debug
        # pobarvajSivoDebug(jelka)
        # print(vrsteTrue)
        # a = 0
        # for b in vrsteTrue:
        #     if b<=a: print(sus)
        #     a=b

        ### Eksplozija
        koordinateTrcenja = jelka.positions_normalized[luckaTrcenja]

        cas = jelka.elapsed_time
        casKonca = cas + 1.1 / hitrostEksplozije
        casZacetka = cas

        while cas < casKonca:
            zunanjiR = (cas - casZacetka) * hitrostEksplozije
            notranjiR = max(0, zunanjiR * (1 - debelinaEksplozije))

            narisiSfero(jelka, koordinateTrcenja, zunanjiR, notranjiR, barva1, barva2)

            yield
            cas = jelka.elapsed_time
        # print('debug')


## Zazeni jelko
def main():
    jelka = Jelka(60)

    jelka.clear = True

    generator = glavnaZanka(jelka)

    def klicnazaj(jelka):
        next(generator)

    jelka.run(klicnazaj)


main()
