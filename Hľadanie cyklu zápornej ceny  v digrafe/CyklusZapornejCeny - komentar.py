import InicializaciaPola
import sys


class CyklusZapornejCeny:

    def __init__(self, cesta):
        self.p = InicializaciaPola.InicializaciaPola(cesta)
        self.H = self.p.vytvorPoleHran()
        self.V = self.p.zistiPocetVrcholov()
        maxi = max(l[1] for l in self.H)
        self.V = self.V if self.V > maxi else maxi
        self.pocetHran = self.p.zistiPocetHran()

    def cyklus(self):
        H = self.H
        S = self.p.vytvorPoleS()
        t = {}
        x = {}
        E = []
        for i in range(1, self.V + 1):
            t[i] = 0
            x[i] = 0
            E.append(i)
        bezCyklu = True
        while(bezCyklu):
            # vyberam prvy prvok z E, zaroven ho aj vymazem z E
            u = E[0]
            E.pop(0)
            dalsieU = u
            # kontrola, ci z daneho vrchola vychadza nejaka hrana, ak nie, tak pokracujem s dalsim vrcholom v poradi
            try:
                if S[u][1] == 0:
                    continue
            except IndexError:
                continue
            # tu prebieha kontrola pola S, v pripade, ze by neexistoval nasledujuci vrchol,tak nevieme zistit pocet vychadzajuci hran z vrchola u,
            # preto loopujem, pokial nenajdem hodnotu x != 0, cize viem zistit pocet hran
            try:
                while (S[dalsieU+1][1] == 0):
                    dalsieU += 1
            # ak som nenasiel vrchol, tak z neho len nevychadza dalsia hrana, pokracujem dalej ak nie je E prazdne
            except IndexError:
                if len(E) == 0:
                    SystemExit(0)
                continue
            for j in range(S[u][1], S[dalsieU+1][1]):
                v = H[j][1]
                cuv = H[j][2]
                # ak najdem lepsiu cenu, tak ju pridam
                if t[v] > t[u] + cuv:
                    t[v] = t[u] + cuv
                    x[v] = u
                    noveV = v
                    E.append(v)
                    cyklus = []
                    cyklus.append(v)
                    # po pridani vrcholu kontrolujem, ci uz tvori cyklus, ak ano, tak koncim
                    while(True):
                        noveV = x[noveV]
                        cyklus.append(noveV)
                        # ak je 0, tak este netvori cyklus
                        if noveV == 0:
                            break
                        elif noveV == v:
                            bezCyklu = False
                            break
            # ak je E prazdne, tak cyklus neexistuje, koniec
            if len(E) == 0:
                print("Neexistuje cyklus")
                SystemExit(0)
        # zistovanie ceny zaporneho cyklu
        cena = 0
        cyklus.reverse()
        for i in range(len(cyklus) - 1):
            u = cyklus[i]
            v = cyklus[i + 1]
            for j in range(1, self.pocetHran + 1):
                if H[j][0] == u and H[j][1] == v:
                    cena += H[j][2]
        # len vypisovanie
        print("Vypis t:\n")
        print(t)
        print("\nVypis x:\n")
        print(x)
        print(f"\nHladany cyklus so zapornou cenou: {cena}\n")
        print(cyklus)
        with open("cyklusZapornerCenyVystup.txt", "w") as f:
            f.write("Vypis t:\n")
            f.write(str(t))
            f.write("Vypis x:\n")
            f.write(str(x))
            f.write(f"Hladany cyklus so zapornou cenou: {cena}\n")
            f.write(str(cyklus))


c = CyklusZapornejCeny("pr1.hrn")
c.cyklus()
