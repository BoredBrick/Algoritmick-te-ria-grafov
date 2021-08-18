import InicializaciaPola


class LabelSet():

    def __init__(self, cesta):
        self.p = InicializaciaPola.InicializaciaPola(cesta)
        self.pocetV = self.p.zistiPocetVrcholov()

    def label(self, u, v):
        H = self.p.vytvorPoleHran()
        S = self.p.vytvorPoleS()
        x = {}
        t = {}
        zU = u
        doV = v
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
            if S[u][1] == 0:
                continue
            dalsieU = u
            while (S[dalsieU+1][1] == 0):
                dalsieU += 1
            for j in range(S[u][1], S[dalsieU+1][1]):
                v = H[j][1]
                if H[j][2] + t[u] < t[v]:
                    t[v] = H[j][2] + t[u]
                    x[v] = u
                    E.append(v)
        cesta = []
        cesta.append(doV)
        v = doV
        while(True):
            v = x.get(v)
            cesta.append(v)
            if v == zU:
                break
        print(f"{zU} - {doV} má dlžku {t.get(doV)}")
        print(cesta[::-1])
        with open("LabelSetUVVystup.txt", 'w')as f:
            f.write(f"{zU} - {doV} má dlžku {t.get(doV)}")
            f.write("\n*********ZACIATOK X **********\n")
            f.write(str(cesta[::-1]))


d = LabelSet("pr1.hrn")
d.label(5, 555)
