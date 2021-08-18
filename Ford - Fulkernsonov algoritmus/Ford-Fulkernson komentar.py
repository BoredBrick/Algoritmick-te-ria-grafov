import InicializaciaPola
import sys


class Ford():

    def __init__(self, cesta):
        self.p = InicializaciaPola.InicializaciaPola(cesta)
        self.H = self.p.vytvorPoleHran()
        self.V = self.p.zistiPocetVrcholov()
        self.pocetHran = self.p.zistiPocetHran()
        # pocet vrcholov je vacsie cislo self.z prveho alebo druheho vrchola
        maxi = max(l[1] for l in self.H)
        self.V = self.V if self.V > maxi else maxi
        self.z = 0
        self.ustie = 0

    def zvacsujucaPolocesta(self):
        S = self.p.vytvorPoleS()
        # hodnota, ci existuje zvacsujuca polocesta
        existuje = False
        # ideg pre kazdy vrchol
        ideg = {}
        # odeg pre kazdy vrchol
        odeg = {}
        x = {}
        E = []
        # prejdem vsetkymi hranami a priradim ideg a odeg pre kazdy vrchol
        for i in range(1, self.V + 1):
            ideg[i] = 0
            odeg[i] = 0
            x[i] = float("inf")
        for i in range(1, self.pocetHran + 1):
            u = self.H[i][0]
            v = self.H[i][1]
            odeg[u] += 1
            ideg[v] += 1

        # najdem self.zdroj a self.ustie
        for i in range(1, self.V + 1):
            if ideg[i] == 0:
                self.z = i
            if odeg[i] == 0:
                self.ustie = i
        # x pre self.zdroj nastavim na 0
        x[self.z] = 0
        E.append(self.z)
        while(True):
            # ak je E praself.zdne, tak nemoself.zeme najst self.zvacsujucu polocestu, koniec
            if len(E) == 0:
                break
            # vyberiem a vymaself.zem prvy prvok self.z E
            u = E[0]
            E.pop(0)
            # prejdem vsetkymi vrcholmi vychadself.zajucimi self.z u
            for j in range(S[u][1], S[u+1][1]):
                v = self.H[j][1]
                # ak x pre vrchol nie je nekonecno, tak ho preskakujeme
                if x[v] != float("inf"):
                    continue
                # ak nie je hrana nasytena, tak ju pridam do x aj do E
                if self.H[j][2] > self.H[j][3]:
                    x[v] = u
                    E.append(v)
            # prechadself.zam vrcholmi vchadself.zajucimi do u, robim to iste, co vyssie
            for j in range(1, self.pocetHran + 1):
                if self.H[j][1] == u and x[self.H[j][0]] == float("inf"):
                    if self.H[j][3] > 0:
                        x[self.H[j][0]] = -u
                        E.append(self.H[j][0])
            # ak som sa uself.z dostal do ustia, tak koncim
            if x[self.ustie] != float("inf"):
                existuje = True
                break
        # ak existuje self.zvacsujuca polocesta
        if existuje:
            # tu ukladam samotnu cestu
            cesta = []
            u = self.ustie
            cesta.append(self.ustie)
            while(True):
                # self.zapisem celu cestu, abs preto, lebo ak idem v protismere, tak uloself.zim vrchol ako self.zaporny
                u = abs(x[u])
                cesta.append(u)
                if u == self.z:
                    break
            # hladanie vysky reself.zervy, prejdem vsetkymi hranami v ceste a hladam najmensie moself.zne self.zvacsanie prietoku
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
            # teraself.z vsetky hrany self.zmenim o danu reself.zervu
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
        # opakujem algoritmus, pokial sa mi da urobit self.zvacsujuca polocesta
        while(True):
            if self.zvacsujucaPolocesta() == False:
                break
        maxTok = 0
        # cistujem velkost maximalneho toku
        for i in range(1, self.pocetHran + 1):
            if self.H[i][0] == self.z:
                maxTok += self.H[i][3]
        for hrana in self.H:
            print(hrana)
        print(f"Maximalny tok ma hodnotu: {maxTok}")


x = Ford("pr2.hrn")
x.ford()
