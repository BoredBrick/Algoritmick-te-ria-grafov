import InicializaciaPola
import sys


class Ocislovanie():

    def __init__(self, cesta):
        p = InicializaciaPola.InicializaciaPola(cesta)
        self.H = p.vytvorPoleHran()
        self.pocetHran = p.zistiPocetHran()
        self.pocetV = p.zistiPocetVrcholov()
        # najvacsie cislo z druheho stlpca (vchadzajuce vrcholy)
        maxi = max(l[1] for l in self.H)
        # pocet vrcholov je vacsie cislo z dvoch stlpcov
        self.pocetV = self.pocetV if self.pocetV > maxi else maxi
        self.poleS = p.vytvorPoleS()

    def ocislovanie(self):
        H = self.H
        S = self.poleS
        # ukladam ideg kazdeho vrchola
        d = {}
        # postupnost vrcholov pri ocislovani
        p = []
        # inicializacia d, kazdemu vrcholu nastavim jeho prisluchajuci ideg na 0
        for i in range(1, self.pocetV + 1):
            d[i] = 0
        # prechadzam vsetkymi hranami, z kazdej hrany vezmem vrchol do ktorej vchadza a danemu vrcholu zvacsim ideg o 1
        for line in self.H:
            if line[0] == 0:
                continue
            d[line[1]] += 1
        # tie vrcholy, ktore maju ideg 0, vlozim do postupnosti p
        for v in d:
            if d[v] == 0:
                p.append(v)
        # ak je prazdne, tak skoncim, kedze to nie je acyklicky graf
        if len(p) == 0:
            print("Nie je acyklicky, chyba mu vrchol s ideg 0")
            sys.exit()
        # pocet vrcholov, tym kontrolujem, ci su uz vsetky pouzite
        k = len(p)
        i = 0
        while (True):
            # ak nastane index error, tak to znamena, ze niekedy v priebehu programu som uz nenasiel ziadny vrchol s ideg 0, cize nie je acyklicky, inaksie vyberiem dalsi
            # vrchol s mnoziny vrcholov ktore maju nulovy ideg
            try:
                v = p[i]
            except IndexError:
                print("Nie je acyklicky")
                sys.exit()
            # kontrola, ci z daneho vrchola vychadzaju nejake hrany, ak nie, tak len zvacsim i a pokracujem
            try:
                if S[v][1] == 0:
                    i += 1
                    continue
            except IndexError:
                i += 1
                continue
            dalsieU = v
            # znova len kontrola pre poleS, v priprade, ze by nasledujuci vrchol neexistoval, tak hladam dalej, aby som nasiel nejaky, co existuje a vedel pocet hran vychadzajucich zo sucanseho vrchola
            try:
                while (S[dalsieU+1][1] == 0):
                    dalsieU += 1
            # ak nastane IndexError, tak to len znamena, ze z daneho vrchola nevychadza ziadna hrana, to problem nie je, pokracujem dalej s dalsim vrcholom
            except IndexError:
                print(v)
                i += 1
                continue
            # prechadzam hranami ktore vychadzaju z vrcholu a akoby ich odstranujem, cize znuzujem ideg vsetkych vrcholov, do ktorych ideme z daneho vrchola
            for j in range(S[v][1], S[dalsieU+1][1]):
                d[H[j][1]] -= 1
                if d[H[j][1]] == 0:
                    p.append(H[j][1])
                    k += 1
            # ak su vsetky vrcholy v zozname, tak je ocislovanie skoncene
            if k == self.pocetV:
                break
            else:
                i += 1
        print(p)
        print(len(p))
        print(self.pocetV)
        with open("ocislovanievystup.txt", "w") as f:
            f.write(str(p))


o = Ocislovanie("acdigraf.hrn")
o.ocislovanie()
