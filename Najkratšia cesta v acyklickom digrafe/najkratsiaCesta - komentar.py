import InicializaciaPola
import MonotonneOcislovanie


class Cesta():

    def __init__(self, cesta):
        # monotonne ocislujem graf, postupnost vrcholov ulozim do p
        self.p = MonotonneOcislovanie.Ocislovanie(cesta).ocislovanie()
        pole = InicializaciaPola.InicializaciaPola(cesta)
        self.V = pole.zistiPocetVrcholov()
        self.H = pole.vytvorPoleHran()
        self.S = pole.vytvorPoleS()
        # pocet vrcholov je vacsie cislo z prveho alebo druheho stlpca vrcholov
        maxi = max(l[1] for l in self.H)
        self.V = self.V if self.V > maxi else maxi

    def najkratsiaCesta(self, u):
        # zapamätanie prvého vrchola z dôvodu výpisu na koniec
        prveU = u
        # zistim index vrchola u
        i = self.p.index(u)
        S = self.S
        H = self.H
        p = self.p
        t = {}
        x = {}
        # len inicializacie
        for vr in range(1, self.V + 1):
            t[vr] = float("inf")
            x[vr] = 0
        t[u] = 0
        while (True):
            # ak sa index rovna indexu posledneho vrchola, tak som na konci, koncim
            if i == self.V:
                break
            u = p[i]
            # len hladanie dalsieho vrcholu v poli S, loopujem v pripade, ze by nasledujuci vrchol neexistoval
            dalsieU = u
            try:
                while (S[dalsieU+1][1] == 0):
                    dalsieU += 1
            # v pripade ze taky vrchol neexistuje, tak z neho len nevychadzam, to nevadi, pokracujem s vacsim indexom
            except IndexError:
                i += 1
                continue
            # ak je cesta kratsia, tak zmenim jej najmensiu cenu, taktiez priradil vrchol do x
            for j in range(S[u][1], S[dalsieU + 1][1]):
                w = H[j][1]
                if t[w] > t[u] + H[j][2]:
                    t[w] = t[u] + H[j][2]
                    x[w] = u
            i += 1
        # len vypisovanie vysledkov
        vysledneX = {}
        vysledneT = {}
        for i in range(1, self.V + 1):
            if(t[i] != float("inf") and t[i] != 0):
                vysledneT[i] = t[i]
            if(x[i] != 0):
                vysledneX[i] = x[i]
        print(f"Výsledné t pre všetky dosiahnutelné vrcholy z vrchola {prveU}")
        print(vysledneT)
        print(f"Vysledné x pre všetky dosiahnutelné vrcholy z vrchola {prveU}")
        print(vysledneX)
        with open("najkratsiaCestaVystup.txt", "w") as f:
            f.write(
                f"Výsledné t pre všetky dosiahnutelné vrcholy z vrchola {prveU}")
            f.write(str(vysledneT))
            f.write(
                f"Vysledné x pre všetky dosiahnutelné vrcholy z vrchola {prveU}")
            f.write(str(vysledneX))


c = Cesta("acdigraf.hrn")
c.najkratsiaCesta(1)
