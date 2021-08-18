import InicializaciaPola
# táto verzia slúži na hľadanie najkratšej cesty medzi 2 vrcholmi


class LabelSet():

    # inicializacia pola hran a pola S
    def __init__(self, cesta):
        self.p = InicializaciaPola.InicializaciaPola(cesta)
        self.pocetV = self.p.zistiPocetVrcholov()

    def label(self, u, v):
        H = self.p.vytvorPoleHran()
        S = self.p.vytvorPoleS()
        t = {}
        x = {}
        # vrchol, z ktoreho vychadzame
        zU = u
        doV = v
        # do pola epsilon pridam prvy vrchol
        u = zU
        E = [u]

        for v in range(self.pocetV):
            # inicializacia x - klucom je vrchol, hodnotou bude vrchol, z ktoreho je najkratsia cesta do daneho vrchola
            x[v + 1] = 0
            # inicializacia t - klucom je vrchol, hodnotou bude najkratsia cesta z u do daneho vrchola, pri inicializacii je hodnota nekonecno
            t[v + 1] = float("inf")
            # t prveho vrchola nastavim na 0, kedze z neho vychadzame
            t[u] = 0
        # pokial mam hodnoty v epsilone, loopujem
        while(E):
            noveU = float("inf")
            # prechadzam vsetkymi vrcholmi ulozenymi v epsilone, vyberam ten s najmensou znackou
            for e in E:
                if t.get(e) < noveU:
                    noveU = e
            # vybraty vrchol odstranim z mnoziny epsilon
            E.remove(noveU)
            u = noveU
            # tu prebieha kontrola pola S, v pripade, ze by neexistoval nasledujuci vrchol,tak nevieme zistit pocet vychadzajuci hran z vrchola u,
            # preto loopujem, pokial nenajdem hodnotu x != 0, cize viem zistit pocet hran
            dalsieU = u
            while (S[dalsieU+1][1] == 0):
                dalsieU += 1
            # teraz prejdem kazdou jednou hranou vychadzajucou z daneho vrchola
            for j in range(S[u][1], S[dalsieU+1][1]):
                # vezmem j-tu hranu z dostupnych hran
                v = H[j][1]
                # ak sucasna cesta do u + cesta z u do v je < ako sucasna znama cesta z u do v, tak zapisem novu najkratsiu cestu do t, taktiez predchadzajuci vrchol do x
                if H[j][2] + t[u] < t[v]:
                    t[v] = H[j][2] + t[u]
                    x[v] = u
                    E.append(v)
        # cesta, obsahuje jednotlive vrcholy, ktorymi prechadzame, aby sme mali najkratsiu cestu z u do v
        cesta = []
        cesta.append(doV)
        v = doV
        while(True):
            v = x.get(v)
            cesta.append(v)
            # ak sa rovnaju, tak sme uz presli celu cestu
            if v == zU:
                break
        print(f"{zU} - {doV} má dlžku {t.get(doV)}")
        print(cesta[::-1])
        with open("LabelSetUVVystup.txt", 'w')as f:
            f.write(f"{zU} - {doV} má dlžku {t.get(doV)}")
            f.write("\n*********ZACIATOK X **********\n")
            f.write(str(cesta[::-1]))


d = LabelSet("pr1.hrn")
d.label(5, 6)
