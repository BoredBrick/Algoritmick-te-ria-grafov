import InicializaciaPola


class ZakladnyAlgoritmus():

    def __init__(self, cesta):
        self.p = InicializaciaPola.InicializaciaPola(cesta)

    def zakladny(self, u):
        V = self.p.zistiPocetVrcholov()
        H = self.p.vytvorPoleHran()
        pocetHran = self.p.zistiPocetHran()
        # inicializácie x,t; všetkým t(v) nastavím značnu na nekonečno, x(v) na nula, t(u) nastavím na nula, kedže z neho vychádzame
        x = {}
        t = {}
        for i in range(1, V + 1):
            t[i] = float("inf")
            x[i] = 0
        t[u] = 0
        zlepsenie = True
        while zlepsenie:
            zlepsenie = False
            # prechádzam všetkými načítanými hranami
            for k in range(1, pocetHran + 1):
                i = H[k][0]
                j = H[k][1]
                cij = H[k][2]
                # ak nájdem takú hranu, že jej cena + cena z u do nej je menšia ako súčasná cena uložená vo v, tak ju nahradím
                if t[j] > t[i] + cij:
                    t[j] = t[i] + cij
                    x[j] = i
                    zlepsenie = True
        print("\n*****ZACIATOK T*****\n")
        print(t)
        print("\n*****ZACIATOK X*****\n")
        print(x)
        with open("zakladnyvystup.txt", "w") as f:
            f.write(str(t))
            f.write("\n*****ZACIATOK X*****\n")
            f.write(str(x))


alg = ZakladnyAlgoritmus("pr1.hrn")
alg.zakladny(1)
