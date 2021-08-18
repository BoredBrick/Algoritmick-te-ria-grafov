import InicializaciaPola


class Kruskalov():

    def __init__(self, cesta):
        p = InicializaciaPola.InicializaciaPola(cesta)
        self.H = p.vytvorPoleHran()
        self.pocetHran = p.zistiPocetHran()
        self.pocetV = p.zistiPocetVrcholov()
        maxi = max(l[1] for l in self.H)
        self.pocetV = self.pocetV if self.pocetV > maxi else maxi
        self.H.sort(key=lambda x: x[2])

    def kruskalov(self):
        k = {}
        postupnostHran = []
        for i in range(1, self.pocetV + 1):
            k[i] = i
        p = []
        for hrana in self.H:
            p.append(f'{hrana[0]},{hrana[1]}')
        p.pop(0)
        pocetVr = 0
        cena = 0
        while (len(p) != 0) and (pocetVr < self.pocetV - 1):
            hrana = p[0].split(",")
            u = int(hrana[0])
            v = int(hrana[1])
            p.pop(0)
            if k[u] != k[v]:
                for i in range(1, self.pocetHran + 1):
                    if self.H[i][0] == u and self.H[i][1] == v:
                        cena += self.H[i][2]
                pocetVr += 1
                postupnostHran.append(f'{{{hrana[0]},{hrana[1]}}}')
                kv = k[v]
                for vrchol in k:
                    if k[vrchol] == kv:
                        k[vrchol] = k[u]
        komponenty = []
        for i in range(1, self.pocetV + 1):
            if k[i] not in komponenty:
                komponenty.append(k[i])
        for i in range(len(komponenty)):
            for j in range(1, self.pocetV + 1):
                if k[j] == komponenty[i]:
                    k[j] = i + 1
        pocetK = len(komponenty)
        print("Komponenty vrcholov\n")
        print(str(k))
        print(f"\nPocet komponentov: {pocetK}")
        print("\nPostupnost hran\n")
        print(str(postupnostHran))
        print(f"\nCena kostry grafu: {cena}")
        with open("KruskalovVypis.txt", 'w') as f:
            f.write("Komponenty vrcholov\n")
            f.write(str(k))
            f.write(f"\nPocet komponentov: {pocetK}")
            f.write("\nPostupnost hran\n")
            f.write(str(postupnostHran))
            f.write(f"\nCena kostry grafu: {cena}")


k = Kruskalov("Strakonice.hrn")
k.kruskalov()
