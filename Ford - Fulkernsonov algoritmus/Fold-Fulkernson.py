import InicializaciaPola
import sys


class Ford():

    def __init__(self, cesta):
        self.p = InicializaciaPola.InicializaciaPola(cesta)
        self.H = self.p.vytvorPoleHran()
        self.V = self.p.zistiPocetVrcholov()
        self.pocetHran = self.p.zistiPocetHran()
        maxi = max(l[1] for l in self.H)
        self.V = self.V if self.V > maxi else maxi
        self.z = 0
        self.ustie = 0

    def zvacsujucaPolocesta(self):
        S = self.p.vytvorPoleS()
        existuje = False
        ideg = {}
        odeg = {}
        x = {}
        E = []
        for i in range(1, self.V + 1):
            ideg[i] = 0
            odeg[i] = 0
            x[i] = float("inf")
        for i in range(1, self.pocetHran + 1):
            u = self.H[i][0]
            v = self.H[i][1]
            odeg[u] += 1
            ideg[v] += 1
        for i in range(1, self.V + 1):
            if ideg[i] == 0:
                self.z = i
            if odeg[i] == 0:
                self.ustie = i
        x[self.z] = 0
        E.append(self.z)
        while(True):
            if len(E) == 0:
                break
            u = E[0]
            E.pop(0)
            for j in range(S[u][1], S[u+1][1]):
                v = self.H[j][1]
                if x[v] != float("inf"):
                    continue
                if self.H[j][2] > self.H[j][3]:
                    x[v] = u
                    E.append(v)
            for j in range(1, self.pocetHran + 1):
                if self.H[j][1] == u and x[self.H[j][0]] == float("inf"):
                    if self.H[j][3] > 0:
                        x[self.H[j][0]] = -u
                        E.append(self.H[j][0])
            if x[self.ustie] != float("inf"):
                existuje = True
                break
        if existuje:
            cesta = []
            u = self.ustie
            cesta.append(self.ustie)
            while(True):
                u = abs(x[u])
                cesta.append(u)
                if u == self.z:
                    break
            r = float("inf")
            for i in range(len(cesta) - 1):
                u = cesta[i]
                v = cesta[i + 1]
                for j in range(1, self.pocetHran + 1):
                    if self.H[j][0] == u and self.H[j][1] == v:
                        if r > self.H[j][2] - self.H[j][3]:
                            r = self.H[j][2] - self.H[j][3]
                    elif self.H[j][0] == v and self.H[j][1] == u:
                        if r > self.H[j][2] - self.H[j][3]:
                            r = self.H[j][2] - self.H[j][3]
            cesta.reverse()
            for i in range(len(cesta) - 1):
                u = cesta[i]
                v = cesta[i + 1]
                for j in range(1, self.pocetHran + 1):
                    if self.H[j][0] == u and self.H[j][1] == v:
                        self.H[j][3] += r
                    elif self.H[j][0] == v and self.H[j][1] == u:
                        self.H[j][3] -= r
        return existuje

    def ford(self):
        while(True):
            if self.zvacsujucaPolocesta() == False:
                break
        maxTok = 0
        for i in range(1, self.pocetHran + 1):
            if self.H[i][0] == self.z:
                maxTok += self.H[i][3]
        for hrana in self.H:
            print(hrana)
        print(f"Maximalny tok ma hodnotu: {maxTok}")


x = Ford("pr1.hrn")
x.ford()
# hrany su vo formate [u,v,kapacita,tok]
# pr2 je taky ocividny digraf na ktorom vidno fungovanie algoritmu
