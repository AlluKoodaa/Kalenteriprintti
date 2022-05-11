#----AlluKoodaa----#

import datetime


def tulostus(x, y, z): # x on alku, y on loppu, z on päiviä yhteensä
    paivat = [i for i in range(1, z+1)]
    print("Kalenteri näyttää seuraavalta:")
    print()
    print("Ma Ti Ke To Pe La Su")
    tuloste = ''
    pva = 0
    while pva < x:
        tuloste += '   '
        pva += 1
    pva = x
    for paiva in paivat:
        if paiva < 10:
            tuloste += ' ' + str(paiva)
        else:
            tuloste += str(paiva)
        if pva == 6 and paiva != paivat[-1]:
            tuloste += '\n'
            pva = 0
            continue
        tuloste += ' '
        pva +=1
    print(tuloste)

def kuukausi(kk):
    kuukaudet = ["tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu",
                 "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu",
                 "marraskuu", "joulukuu"]
    return kuukaudet[kk - 1]
    
def paaohjelma():
    vuosi = int(input("Anna vuosi: "))
    kk = int(input("Anna kuukausi: "))
    alku = datetime.date(vuosi, kk, 1).weekday()
    alkupva = datetime.datetime.strptime(f"{vuosi}{kk}1", "%Y%m%d")
    if alkupva.month == 12:
        ensikuu = datetime.datetime.strptime(f"{vuosi + 1} 1 1", "%Y %m %d")
    else:
        ensikuu = datetime.datetime.strptime(f"{vuosi}{kk+1}1", "%Y%m%d")
    loppupva = ensikuu - alkupva
    paivia = loppupva.days
    kuu = kuukausi(kk)
    print(f"Vuoden {vuosi} {kuu}ssa {paivia} päivää.")
    loppu = datetime.date(vuosi, kk, loppupva.days).weekday()
    tulostus(alku, loppu, paivia)
    print()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()

#----eof----#
