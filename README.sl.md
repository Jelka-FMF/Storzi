# Storži

Zbirka vzorcev za Jelko FMF.

## O projektu

Ta repozitorij vsebuje vse vzorce, ki tečejo na [Jelki FMF](https://jelka.fmf.uni-lj.si/).

Vzorci so na voljo v mapi `patterns`. Vsak vzorec je v svoji mapi in je lahko napisan
v večini programskih jezikov, ki podpirajo izpis na standardni izhod in se lahko izvajajo
v Docker vsebniku.

Vsi vzorci iz repozitorija se samodejno prevedejo in namestijo na strežnik Jelkob ter bodo
prikazani na uradni novoletni jelki Fakultete za matematiko in fiziko Univerze v Ljubljani.

## Prispevanje

> [!TIP]
> Če ne znate uporabljati Gita/GitHuba ali ne morete slediti tem navodilom iz kakršnega
> koli drugega razloga, si lahko ogledate [Jelkly](https://jelkly.fmf.uni-lj.si/docs).
> Nudi orodje za vizualno programiranje, podobno Scratchu, za ustvarjanje in pošiljanje
> svojih vzorcev za Jelko FMF, brez potrebe po znanju programiranja.

### Splošne informacije

Vse vzorce najdete v mapi `patterns`.

Vsak vzorec vključuje svojo mapo, ki mora vsebovati datoteki `config.yml` in `main.*`
ter opcijsko `Dockerfile`.

Ime mape služi kot ID vzorca. Ime mape naj bo podobno imenu vzorca, in naj vsebuje
le male črke, številke ter pomišljaje.

Datoteka `config.yml` vsebuje konfiguracijo vzorca. Nastavlja osnovne informacije o vzorcu,
kot so ime, opis, avtor in šola. Ime mora biti kratko, opisno in unikatno, medtem ko naj opis
v stavku ali dveh razloži, kaj vzorec počne.

Datoteka `main.*` je glavna datoteka vzorca, ki se izvede, ko se vzorec zažene.

Če pišete vzorec v jeziku, za katerega nudimo uradno predlogo, bo jezik samodejno zaznan
glede na končnico datoteke.

Če vzorec pišete v jeziku, za katerega ne nudimo predloge, boste morali napisati tudi
lasten `Dockerfile`, ki bo uporabljen za prevajanje in zagon vzorca. Med zagonom naj `Dockerfile`
zažene vzorec in preusmeri izhod vzorca na `/tmp/jelka`. Več informacij o razvoju vzorcev
brez knjižnjice lahko preberete [spodaj](#vzorci-v-drugih-jezikih).

Če pišete vzorec v jeziku, za katerega nudimo predlogo, lahko kljub temu napišete lasten
`Dockerfile`, če potrebujete dodatno konfiguracijo, vendar je priporočeno uporabljati
privzeto predlogo, če je le mogoče.

### Dodajanje vzorca

Če nimate že nastavljenega Gita oziroma GitHuba, si lahko [tukaj](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git)
prebereta uradna navodila.

Najprej naredite razcep (fork) repozitorija, kot je opisano v [dokumentaciji](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).

Nato ga klonirajte na svoj računalnik:

```bash
git clone https://github.com/VASE-GITHUB-UPORABNISKO-IME/Storzi.git
cd Storzi
```

Ko ste v repozitoriju, ustvarite Python virtualno okolje (venv):

```bash
python -m venv venv
```

Okolje lahko nato aktivirate:

```bash
venv\Scripts\activate # Na Windowsu
```

```bash
source venv/bin/activate # Na Linuxu and macOSu
```

Če uporabljate urejevalnik kot je Visual Studio Code ali PyCharm, lahko namesto tega
ustvarite in aktivirate virtualno okolje s funkcijami v urejevalniku.

Nato namestite zahtevane knjižnice:

```bash
pip install -r requirements.txt
```

Za dodajanje novega vzorca ustvarite novo mapo v mapi `patterns` ter dodajte datoteki
`config.yml` in `main.*`. Preglejte navodila zgoraj za splošne informacije o datotekah
ter spodnje razdelke, specifične za jezik.

Ko ste vzorec dodali (in ga ustrezno oblikovali), shranite spremembe:

```bash
git add patterns/vase-ime-vzorca
git commit -m "Vaše sporočilo ob shranjevanju"
```

Spremembe lahko nato objavite:

```bash
git push
```

Nato s pomočjo GitHub vmesnika ustvarite pull request (PR).

### Vzorci v Pythonu

Ko pišete Python vzorec, namestite priporočene knjižnice iz datoteke
`requirements.txt` v korenu repozitorija:

```bash
pip install -r requirements.txt
```

To bo namestilo vse razpoložljive knjižnice, ki jih lahko uporabljate
v Python vzorcih, poleg simulacije za lokalni zagon vzorcev in drugih
razvojnih orodij.

Vaš vzorec lahko uporablja [Jelka Python API](https://github.com/Jelka-FMF/JelkaPy)
in druge razpoložljive knjižnice (glejte spodaj).

Glavno ime datoteke vzorca mora biti `main.py`.

Kot predlogo lahko preverite [primer Python vzorca](patterns/example-python/).
Za inspiracijo si lahko pogledate tudi obstoječe Python vzorce.

Med razvojem vzorca ga lahko zaženete lokalno z uporabo simulacije:

```bash
jelkasim patterns/vase-ime-vzorca/main.py
```

Pred shranjevanjem vzorca se prepričajte, da je ustrezno oblikovan:

```bash
ruff check patterns/vase-ime-vzorca
ruff format patterns/vase-ime-vzorca
```

### Vzorci v JavaScriptu

Ko pišete JavaScript vzorec, namestite priporočene knjižnice iz datoteke
`package.json` v korenu repozitorija:

```bash
npm install
```

To bo namestilo vse razpoložljive knjižnice, ki jih lahko uporabljate
v JavaScript vzorcih, poleg razvojnih orodij.

Še vedno pa morate namestiti Python knjižnjice, kot je specifirano
v zgornjem razdelku, saj se uporabljajo za zagon simulacije.

Vaš vzorec lahko uporablja [Jelka JavaScript API](https://github.com/Jelka-FMF/JelkaJS)
in druge razpoložljive knjižnice (glejte spodaj).

Glavno ime datoteke vzorca mora biti `main.js`.

Kot predlogo lahko preverite [primer JavaScript vzorca](patterns/example-javascript/).
Za inspiracijo si lahko pogledate tudi obstoječe JavaScript vzorce.

Med razvojem vzorca ga lahko zaženete lokalno z uporabo simulacije:

```bash
jelkasim node patterns/vase-ime-vzorca/main.js
```

Pred shranjevanjem vzorca se prepričajte, da je ustrezno oblikovan:

```bash
npm run format patterns/vase-ime-vzorca
```

### Vzorci v drugih jezikih

Za pisanje vzorcev v drugih jezikih je potrebno izdelati `Dockerfile`,
ki bo gradil in zagnal vašo kodo. Ko se Docker vsebnik zažene, mora
zagnati vaš vzorec.

Za razvijanje vzorca in uporabo simulacije morate še vedno namestiti
Python knjižnjice, kot je specifirano v zgornjem razdelku.

Docker vsebniki pritrdijo cev `/tmp/jelka`, kamor se morajo zapisovati
informacije o barvah. To lahko dosežete bodisi z neposrednim pisanjem
v cev bodisi z preusmeritvijo standardnega izhoda v cev.

Prva vrstica mora biti glava vzorca, ki specificira podatke o vzorcih:

```
#{"version": 0, "led_count": 500, "fps": 60}\n
```

Nato mora vzorec za vsako sličico poslati podatke o barvah v naslednjem formatu:

```
#<barva v hexadecimalni obliki><naslednja barva v hexadecimalni obliki> ... <zadnja barva v hexadecimalni obliki>\n
```

Glavne smernice za predstavitev barv:

* Vsaka sličica mora biti na svoji vrstici.
* Barve morajo biti zapisane le v hexadecimalni obliki (npr. veljavna bela je `ffffff`, ne pa `#ffffff`).
* Vrstica se mora začeti z `#` in končati z znakom za novo vrstico, in drugje ne sme vsebovati `#`.
* Vrstice, ki se ne začnejo z `#`, so obravnavane kot komentarji in so ignorirane.

Pomembne opombe:

* Hitrost prikaza je strojno omejena na 66 sličic na sekundo, zato ne pričakujte več kot 60 sličic na sekundo.
* Številni jeziki ne omogočajo avtomatskega praznjenja izhodnega toka, zato boste morda morali implementirati ročno praznjenje

Docker vsebniki priklopijo CSV datoteko s pozicijami na `/tmp/positions.csv`.
Zunaj vsebnika je primer CSV datoteke s pozicijami na voljo v [`data/positions.csv`](data/positions.csv)
v tem repozitoriju. Vsaka vrstica vsebuje ID luči in XYZ pozicijo luči. Če ne
uporabljate uradne knjižnice, boste morali ročno naložiti pravilno datoteko
in razčleniti pozicije, če jih potrebujete. Če uporabljate uradno knjižnico,
bo to obdelano samodejno.

### Smernice

* Vzorci morajo biti napisani tako, da jih je mogoče zagnati v Docker vsebniku.
* Vzorci morajo izhod posredovati na standardni izhod (ki je preusmerjen v `/tmp/jelka`).
* Vzorci ne smejo prikazovati neprimerne vsebine.

## Predloge

### Python

* Osnovna konfiguracija: [`images/python`](images/python)
* Privzeta predloga: [`defaults/python`](defaults/python)
* Razpoložljive knjižnice: [`requirements.in`](images/python/requirements.in)
* Ime datoteke vzorca: `main.py`

### JavaScript

* Osnovna konfiguracija: [`images/javascript`](images/javascript)
* Privzeta predloga: [`defaults/javascript`](defaults/javascript)
* Razpoložljive knjižnice: [`package.json`](images/javascript/package.json)
* Ime datoteke vzorca: `main.js`

# OCaml

* Osnovna konfiguracija: [`images/ocaml`](images/ocaml)
* Privzeta predloga: [`defaults/ocaml`](defaults/ocaml)
* Razpoložljive knjižnice: *Ni na voljo*
* Ime datoteke vzorca: `main.ml`

## Struktura

* `patterns/` - Imenik, ki vsebuje vse vzorce
  * `ime-vzorca/`
    * `config.yml` - Konfiguracijska datoteka za vzorec
    * `main.*` - Glavna datoteka vzorca

* `defaults/` - Privzete Docker predloge za vzorce
  * `javascript/` - Privzeta Docker predloga za JavaScript vzorce
  * `python/` - Privzeta Docker predloga za Python vzorce

* `images/` - Osnovne Docker podobe za vzorce
  * `javascript/` - Osnovna Docker podoba za JavaScript vzorce
  * `python/` - Osnovna Docker podoba za Python vzorce

## Licenca

S prispevanjem v ta repozitorij se strinjate, da licencirate svoje delo pod licenco MIT.
