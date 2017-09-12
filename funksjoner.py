"""
Dette programmet handler om funksjoner. 
"""

def adder(tall1, tall2):
    """
    Funksjon som tar in to tall som parametere, og returnerer summen av de to tallene.
    """
    return tall1 + tall2

print("1 + 2 = {}".format(adder(1, 2)))
print("3 + 4 = {}".format(adder(3, 4)))


def tellForekomst(minTekst, minBokstav):
    """
    Funksjon som tar inn en string (tekst) og en bokstav, og sjekker hvor mange ganger bokstaven
    forekommer i teksten.
    """
    print(minTekst.count(minBokstav))
    # Evt:
    # antallForekomster = 0
    # for bokstav in minTekst:
    #     if bokstav == minBokstav:
    #         antallForekomster += 1
    # print(antallForekomster)


tekst = input("Skriv inn et ord eller en setning: ")
bokstav = input("Skriv inn en bokstav: ")

tellForekomst(tekst, bokstav)




