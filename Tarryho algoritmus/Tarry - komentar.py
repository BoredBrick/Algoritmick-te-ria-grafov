import InicializaciaPola
# povodna verzia, zdrojovy subor ma uz uv aj vu hrany, nic nedorabam


class TarryhoAlgoritmus():

    def __init__(self, cesta):
        # poleS a pole hran sa nacitava z druhej triedy
        p = InicializaciaPola.InicializaciaPola(cesta)
        self.H = p.vytvorPoleHran()
        self.S = p.vytvorPoleS()
        self.pocetV = p.zistiPocetVrcholov()
        # vymazanie ceny hran
        for riadok in self.H:
            riadok[2] = 0

    def tarry(self, u):
        S = self.S
        H = self.H
        # ukladanie tarryho sledu
        T = []
        T.append(u)
        objaveny = [0 for x in range(self.pocetV + 1)]
        objaveny[u] = 1
        while (True):
            # kandidat na pouzitie (hrana prveho prichodu)
            kandidat = 0
            v = 0
            # kontrola, ci vrchol po vrchole U existuje (aby som mal hranicu, kolko hran vychadza v U), ak nie, loopujem, pokial to nie je 0 - co znamena, ze je aspon jedna hrana, cize existuje
            dalsieU = u
            while (S[dalsieU+1][1] == 0):
                dalsieU += 1
            # prechadzam polom S, v nom viem, kolko hran vychadza z kazdeho vrchola, takze mi staci skontrolovat iba tie
            for i in range(S[u][1], S[u + 1][1]):
                # ak je 1, tak hrana uz bola pouzita a nemozno ju pouzit
                if H[i][2] == 1:
                    continue
                # ak je -1 tak je to hrana prveho prichodu a smiem ju pouzit ako poslednu moznost
                elif H[i][2] == -1:
                    kandidat = i
                    continue
                # ked som tu tak som nasiel este nevyuzitu hranu, priradim jej vrchol a zapisem ju ako pouzitu
                v = H[i][1]
                H[i][2] = 1
                # zapis do T
                T.append(f"{{{u},{v}}}")
                T.append(v)
                # ak som v tomto vrchole este nebol, tak musim zistit jeho hranosmer(opacnu cestu) a oznacit ju -1, aby som vedel, ze ju mozem pouzit nakoniec
                if objaveny[v] == 0:
                    # kontrola, ci som nasiel hranu vu
                    hvu = 0
                    objaveny[v] = 1
                    # rovnaka kontrola ako vyssie, tentokrat len pre v
                    dalsieV = v
                    while (S[dalsieV+1][1] == 0):
                        dalsieV += 1
                    for j in range(S[v][1], S[dalsieV + 1][1]):
                        if H[j][1] == u:
                            H[j][2] = -1
                            # nasiel som opacnu hranu, takze existuje, takze mozem pouzit povodnu hranu, jej koncovy vrchol bude teda zaciatocny v dalsej iteracii
                            hvu = j
                            u = v
                            break
                    if hvu == 0:
                        print("Chyba dat, chyba hranosmer " +
                              str(v) + " " + str(u))
                        raise SystemExit
                    break
                else:
                    # vrchol uz bol objaveny, takze len pokracujem z toho vrchola
                    u = v
                    break
            # uz som nic nenasiel, koniec
            if kandidat == 0 and v == 0:
                break
            # idem naspat cestou poslednej moznosti
            if kandidat > 0 and v == 0:
                v = H[kandidat][1]
                T.append(f"{{{u},{v}}}")
                T.append(v)
                u = v
                H[kandidat][2] = 1
        print(T)
        with open("tarryvystup.txt", "w") as f:
            f.write(str(T))


# nastavenie cesty pre subor s hranami
t = TarryhoAlgoritmus("pr1.hrn")
t.tarry(1)
