"""
Dette programmet ber brukeren om aa oppgi et sted, et klesplagg og en avreisedato 5 ganger.
Disse inputene legges inn i 3 respektive lister, som saa settes inn i en ny liste.
Tilslutt bes brukeren oppgi to indekser, én som gir kategori, og én som gir indeks i kategori.
"""

steder = []
klesplagg = []
avreisedatoer = []

for i in range(5):
    sted = input("Skriv inn et sted: ")
    plagg = input("Skriv inn et klesplagg: ")
    avreisedato = input("Skriv inn en avreisedato: ")
    steder.append(sted)
    klesplagg.append(plagg)
    avreisedatoer.append(avreisedato)

reiseplan = [steder, klesplagg, avreisedatoer]

for lst in reiseplan:
    print(lst)

i1 = int(input("Hvilken kategori? 0(steder), 1(klesplagg) eller 2(avreisedatoer): "))
i2 = int(input("Skriv inn en indeks: "))

if 0 <= i1 <= (len(reiseplan)-1) and 0 <= i2 <= (len(reiseplan[i1])-1): #Sjekker om inputene er innenfor riktige verdier.
    print(reiseplan[i1][i2])
else:
    print("Ugyldig input.")

valg = input("Hva onsker du aa gjore?\n Legg til en film (1)\n Fjern en film (2)\n Oversikt over alle filmer (3)\n Informasjon om en film (4)\n Finn hylleplassering (5)\n Avslutte (6)\n\n\n\n> ")
