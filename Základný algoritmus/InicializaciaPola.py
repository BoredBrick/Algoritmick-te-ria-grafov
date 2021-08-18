class InicializaciaPola():

    def __init__(self, cesta):
        self.cestaKSuboru = cesta
        self.pocetHran = self.zistiPocetHran()
        self.poleHran = self.vytvorPoleHran()
        self.pocetVrcholov = self.zistiPocetVrcholov()
        self.poleS = self.vytvorPoleS()

    # nacitam riadok s hranami, vratim ich pocet + 1 (kedze i zacina od nuly)
    def zistiPocetHran(self):
        with open(self.cestaKSuboru, 'r') as f:
            i = -1
            for(i, _l) in enumerate(f):
                pass
            return i+1

    # nacitam kazdy riadok zo suboru a zapisem do listu v tvare - [hrana u] [hrana v] [cena uv]
    def vytvorPoleHran(self):
        pole = [[0 for x in range(3)] for y in range(self.pocetHran + 1)]
        with open(self.cestaKSuboru, 'r') as f:
            for index, riadok in enumerate(f):
                r = riadok.split()
                for index2, cislo in enumerate(r):
                    pole[index + 1][index2] = int(cislo)
        self.zoradPodlaPrvehoRiadka(pole)
        return pole

    def zoradPodlaPrvehoRiadka(self, pole):
        pole.sort(key=lambda x: x[0])

    def zistiPocetVrcholov(self):
        m = self.poleHran
        for i in range(self.pocetHran):
            max = m[i][0] if m[i][0] > m[i+1][0] else m[i + 1][0]
        return max

    # pole S sluzi na indexovanie pola H-ak vrchol 1 zacina na prvom riadku a idu z neho dve hrany, tak vrchol 2 bude mat v S hodnotu 4 - kedze bude zacinat
    # na 4 riadku v H
    def vytvorPoleS(self):
        pole = [[0 for x in range(2)] for y in range(self.pocetVrcholov + 2)]
        hpole = self.poleHran
        for i in range(self.pocetVrcholov + 1):
            pole[i][0] = i
        hladane = 0
        for i in range(self.pocetHran + 1):
            # posledny riadok na ukoncenie
            if i == self.pocetHran:
                pole[hladane + 1][0] = pole[hladane][0] + 1
                pole[hladane + 1][1] = i + 1
                break
            # zvysim i ak je dalsia hrana z rovnakeho vrchola
            elif hpole[i + 1][0] == hladane:
                continue
            # ak nasledujuci vrchol neexistuje, loopujem pokial najdem nejaky existujuci
            while hpole[i + 1][0] != hladane + 1:
                hladane += 1
            else:
                pole[hladane + 1][1] = i + 1
                hladane += 1

        return pole

