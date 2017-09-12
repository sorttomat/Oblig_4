"""
Dette programmet utforsker lister og loekker.
"""

listeMedTall = []

tall = 1
while tall != 0:
    """
    Problemet med denne while-loekken, er at når brukeren taster inn tallet 0,
    blir også det tallet puttet inn i listen. Da vil det minste tallet alltid vaere 0.
    Man kan bruke en if-test og en break for aa forhindre det.
    """
    tall = float(input("Skriv inn et tall: "))
    if tall == 0:
        break
    listeMedTall.append(tall)

for tall in listeMedTall:
    print(tall)


minSum = 0
for tall in listeMedTall:
    minSum += tall
print(minSum)

#Finner det minste tallet i listen:
minst = listeMedTall[0]
for tall in listeMedTall:
    if tall < minst:
        minst = tall

#Finner det stoerste tallet i listen:
storst = listeMedTall[0]
for tall in listeMedTall:
    if tall > storst:
        storst = tall

print(minst, storst)


