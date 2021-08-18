import InicializaciaPola
import MonotonneOcislovanie


class Cesta():

    def __init__(self, cesta):
        self.p = MonotonneOcislovanie.Ocislovanie(cesta).ocislovanie()
        pole = InicializaciaPola.InicializaciaPola(cesta)
        self.V = pole.zistiPocetVrcholov()
        self.H = pole.vytvorPoleHran()
        self.S = pole.vytvorPoleS()
        maxi = max(l[1] for l in self.H)
        self.V = self.V if self.V > maxi else maxi

    def najkratsiaCesta(self, u):
        prveU = u
        i = self.p.index(u)
        S = self.S
        H = self.H
        p = self.p
        t = {}
        x = {}
        for vr in range(1, self.V + 1):
            t[vr] = float("inf")
            x[vr] = 0
        t[u] = 0
        while (True):
            if i == self.V:
                break
            u = p[i]
            try:
                if S[u][1] == 0:
                    i += 1
                    continue
            except IndexError:
                i += 1
                continue
            dalsieU = u
            try:
                while (S[dalsieU+1][1] == 0):
                    dalsieU += 1
            except IndexError:
                i += 1
                continue
            for j in range(S[u][1], S[dalsieU + 1][1]):
                w = H[j][1]
                if t[w] > t[u] + H[j][2]:
                    t[w] = t[u] + H[j][2]
                    x[w] = u
            i += 1
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


c = Cesta("CPM_stred.hrn")
c.najkratsiaCesta(1)
