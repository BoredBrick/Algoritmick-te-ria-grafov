import InicializaciaPola


class LabelCorrect():

    def __init__(self, cesta):
        self.p = InicializaciaPola.InicializaciaPola(cesta)
        self.pocetV = self.p.zistiPocetVrcholov()

    def label(self):
        H = self.p.vytvorPoleHran()
        S = self.p.vytvorPoleS()
        t = {}
        x = {}
        u = 1
        E = [u]
        for v in range(self.pocetV):
            x[v + 1] = 0
            t[v + 1] = float("inf")
            t[u] = 0
        while(E):
            u = E[0]
            E.pop(0)
            dalsieU = u
            while (S[dalsieU+1][1] == 0):
                dalsieU += 1
            for j in range(S[u][1], S[dalsieU+1][1]):
                v = H[j][1]
                if H[j][2] + t[u] < t[v]:
                    t[v] = H[j][2] + t[u]
                    x[v] = u
                    E.append(v)
        print(t, x)


d = LabelCorrect("pr1.hrn")
d.label()
