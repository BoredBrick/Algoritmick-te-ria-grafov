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
            u = E[0]
            E.pop(0)
            dalsieU = u
            try:
                if S[u][1] == 0:
                    continue
            except IndexError:
                continue
            try:
                while (S[dalsieU+1][1] == 0):
                    dalsieU += 1
            except IndexError:
                if len(E) == 0:
                    SystemExit(0)
                continue
            for j in range(S[u][1], S[dalsieU+1][1]):
                if bezCyklu == False:
                    break
                v = H[j][1]
                cuv = H[j][2]
                if t[v] > t[u] + cuv:
                    t[v] = t[u] + cuv
                    x[v] = u
                    noveV = v
                    E.append(v)
                    cyklus = []
                    cyklus.append(v)
                    while(True):
                        noveV = x[noveV]
                        cyklus.append(noveV)
                        if noveV == 0:
                            break
                        elif noveV == v:
                            bezCyklu = False
                            break
            if len(E) == 0:
                print("Neexistuje cyklus")
                SystemExit(0)
        cena = 0
        cyklus.reverse()
        for i in range(len(cyklus) - 1):
            u = cyklus[i]
            v = cyklus[i + 1]
            for j in range(1, self.pocetHran + 1):
                if H[j][0] == u and H[j][1] == v:
                    cena += H[j][2]
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


c = CyklusZapornejCeny("CYKL_maxi.hrn")
c.cyklus()
