import InicializaciaPola


class ZakladnyAlgoritmus():

    def __init__(self, cesta):
        self.p = InicializaciaPola.InicializaciaPola(cesta)

    def zakladny(self, u, v):
        V = self.p.zistiPocetVrcholov()
        H = self.p.vytvorPoleHran()
        pocetHran = self.p.zistiPocetHran()
        x = {}
        t = {}
        for i in range(1, V + 1):
            t[i] = float("inf")
            x[i] = 0
        t[u] = 0
        zlepsenie = True
        while zlepsenie:
            zlepsenie = False
            for k in range(1, pocetHran + 1):
                i = H[k][0]
                j = H[k][1]
                cij = H[k][2]
                if t[j] > t[i] + cij:
                    t[j] = t[i] + cij
                    x[j] = i
                    zlepsenie = True
        cesta = []
        pomV = v
        cesta.append(v)
        while(True):
            pomV = x[pomV]
            cesta.append(pomV)
            if pomV == u:
                break
        cesta.reverse()
        print(f"{u} - {v} má dĺžku {t[v]}")
        print(cesta)
        with open("zakladnyUVvystup.txt", "w", encoding='utf-8') as f:
            f.write(f"{u} - {v} má dĺžku {t[v]}")
            f.write("\n")
            f.write(str(cesta))


alg = ZakladnyAlgoritmus("pr1.hrn")
alg.zakladny(2, 110)
