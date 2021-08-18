import InicializaciaPola
import sys
import MonotonneOcislovanie


class CPM():

    def __init__(self, cesta):
        self.mo = MonotonneOcislovanie.Ocislovanie(cesta).ocislovanie()
        self.p = InicializaciaPola.InicializaciaPola(cesta)
        self.H = self.p.vytvorPoleHran()
        self.V = self.p.zistiPocetVrcholov()
        self.pocetHran = self.p.zistiPocetHran()
        maxi = max(l[1] for l in self.H)
        self.V = self.V if self.V > maxi else maxi

    def CPM(self, cestaKuP):
        S = self.p.vytvorPoleS()
        odeg = {}
        p = {}
        z = {}
        x = {}
        with open(cestaKuP, "r") as f:
            for i, time in enumerate(f):
                tim = time.split()
                p[i+1] = int(tim[0])
                x[i+1] = 0
                z[i+1] = 0
                odeg[i + 1] = 0
        for i in range(1, self.pocetHran + 1):
            odeg[self.H[i][0]] += 1
        for i in range(self.V - 1):
            r = self.mo[i]
            dalsieR = r
            try:
                if S[r][1] == 0:
                    i += 1
                    continue
            except IndexError:
                i += 1
                continue
            try:
                while (S[dalsieR+1][1] == 0):
                    dalsieR += 1
            except IndexError:
                continue
            for j in range(S[r][1], S[dalsieR+1][1]):
                w = self.H[j][1]
                if z[w] < z[r] + p[r]:
                    z[w] = z[r] + p[r]
                    x[w] = r
        T = 0
        for i in odeg:
            if odeg[i] == 0:
                w = i
                if z[w] + p[w] > T:
                    T = z[w] + p[w]
        k = {}
        y = {}
        for i in range(1, self.V + 1):
            k[i] = T
            y[i] = 0
        i = self.V - 1
        while i != -1:
            r = self.mo[i]
            i -= 1
            dalsieR = r
            try:
                if S[r][1] == 0:
                    continue
            except IndexError:
                continue
            try:
                while (S[dalsieR+1][1] == 0):
                    dalsieR += 1
            except IndexError:
                continue
            for j in range(S[r][1], S[dalsieR+1][1]):
                w = self.H[j][1]
                if k[r] > k[w] - p[w]:
                    k[r] = k[w] - p[w]
                    y[r] = w
        R = {}
        for i in range(1, self.V + 1):
            R[i] = 0
        for i in range(1, self.V + 1):
            R[i] = k[i] - z[i] - p[i]
        kriticka = []
        for i in range(1, self.V + 1):
            if R[i] == 0:
                kriticka.append(i)
        print(str(kriticka))


c = CPM("CPM_midi.hrn")
c.CPM("CPM_midi.tim")
