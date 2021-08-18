import InicializaciaPolaPreUV
# v tejto verzii mam specialnu verziu inicializacie pola, v ktorom si potrebujem dorobit hranu VU, keďže mám len UV


class TarryhoAlgoritmus():

    def __init__(self, cesta):
        p = InicializaciaPolaPreUV.InicializaciaPola(cesta)

        self.H = p.vytvorPoleHran()
        self.S = p.vytvorPoleS()
        self.pocetHran = p.zistiPocetHran()
        self.pocetV = p.zistiPocetVrcholov()
        for riadok in self.H:
            riadok[2] = 0

    def tarry(self, u):
        S = self.S
        H = self.H
        T = []
        T.append(u)
        objaveny = [0 for x in range(self.pocetV + 1)]
        objaveny[u] = 1
        while (True):
            kandidat = 0
            v = 0
            dalsieU = u
            while (S[dalsieU+1][1] == 0):
                dalsieU += 1
            for i in range(S[u][1], S[dalsieU + 1][1]):
                if H[i][2] == 1:
                    continue
                elif H[i][2] == -1:
                    kandidat = i
                    continue
                v = H[i][1]
                H[i][2] = 1
                T.append(f"{{{u},{v}}}")
                T.append(v)
                if objaveny[v] == 0:
                    hvu = 0
                    objaveny[v] = 1
                    dalsieV = v
                    while (S[dalsieV+1][1] == 0):
                        dalsieV += 1
                    for j in range(S[v][1], S[dalsieV + 1][1]):
                        if H[j][1] == u:
                            H[j][2] = -1
                            hvu = j
                            u = v
                            break
                    if hvu == 0:
                        print("Chyba dat, chyba hranosmer " +
                              str(v) + " " + str(u))
                        raise SystemExit
                    break
                else:
                    u = v
                    break
            if kandidat == 0 and v == 0:
                break
            if kandidat > 0 and v == 0:
                v = H[kandidat][1]
                T.append(f"{{{u},{v}}}")
                T.append(v)
                u = v
                H[kandidat][2] = 1
        print(T)
        with open("tarryvystupUV.txt", "w") as f:
            f.write(str(T))


t = TarryhoAlgoritmus(
    "TEST_mini.hrn")
t.tarry(1)
