import InicializaciaPola


class LabelSet():

    def __init__(self, cesta):
        self.p = InicializaciaPola.InicializaciaPola(cesta)
        self.pocetV = self.p.zistiPocetVrcholov()

    def label(self, u):
        H = self.p.vytvorPoleHran()
        S = self.p.vytvorPoleS()
        t = {}
        x = {}
        E = [u]
        for v in range(self.pocetV):
            x[v + 1] = 0
            t[v + 1] = float("inf")
        t[u] = 0
        while(E):
            noveU = float("inf")
            for e in E:
                if t.get(e) < noveU:
                    noveU = e
            E.remove(noveU)
            u = noveU
            dalsieU = u
            while (S[dalsieU+1][1] == 0):
                dalsieU += 1
            for j in range(S[u][1], S[dalsieU+1][1]):
                v = H[j][1]
                try:
                    if H[j][2] + t[u] < t[v]:
                        t[v] = H[j][2] + t[u]
                        x[v] = u
                        E.append(v)
                except KeyError:
                    continue
        with open("LabelSetVystup.txt", 'w')as f:
            f.write(str(t))
            f.write("\n*********ZACIATOK X **********\n")
            f.write(str(x))
        print(t, "\n**ZACIATOK X**\n", x)


d = LabelSet("pr1.hrn")
d.label(1)
