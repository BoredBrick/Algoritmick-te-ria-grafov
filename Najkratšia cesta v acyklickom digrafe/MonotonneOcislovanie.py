import InicializaciaPola
import sys


class Ocislovanie():

    def __init__(self, cesta):
        p = InicializaciaPola.InicializaciaPola(cesta)
        self.H = p.vytvorPoleHran()
        self.pocetHran = p.zistiPocetHran()
        self.pocetV = p.zistiPocetVrcholov()
        maxi = max(l[1] for l in self.H)
        self.pocetV = self.pocetV if self.pocetV > maxi else maxi
        self.poleS = p.vytvorPoleS()

    def ocislovanie(self):
        H = self.H
        S = self.poleS
        d = {}
        p = []
        for i in range(1, self.pocetV + 1):
            d[i] = 0
        for line in self.H:
            if line[0] == 0:
                continue
            d[line[1]] += 1
        for v in d:
            if d[v] == 0:
                p.append(v)
        k = len(p)
        i = 0
        while (True):
            try:
                v = p[i]
            except IndexError:
                print("Nie je acyklicky")
                sys.exit()
            try:
                if S[v][1] == 0:
                    i += 1
                    continue
            except IndexError:
                i += 1
                continue
            dalsieU = v
            try:
                while (S[dalsieU+1][1] == 0):
                    dalsieU += 1
            except IndexError:
                i += 1
                continue
            for j in range(S[v][1], S[dalsieU+1][1]):
                d[H[j][1]] -= 1
                if d[H[j][1]] == 0:
                    p.append(H[j][1])
                    k += 1
            if k == self.pocetV:
                break
            else:
                i += 1
        return p


o = Ocislovanie("acdigraf.hrn")
o.ocislovanie()
