import InicializaciaPola


class LabelSet():

    # inicializacia pola hran a pola S
    def __init__(self, cesta):
        self.p = InicializaciaPola.InicializaciaPola(cesta)
        self.pocetV = self.p.zistiPocetVrcholov()

    def label(self, u):
        H = self.p.vytvorPoleHran()
        S = self.p.vytvorPoleS()
        t = {}
        x = {}
        # do pola epsilon pridam prvy vrchol
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

        with open("LabelSetVystup.txt", 'w')as f:
            f.write(str(t))
            f.write("\n*********ZACIATOK X **********\n")
            f.write(str(x))
        print(t, "\n***X***\n", x)


d = LabelSet("pr1.hrn")
d.label(1)
