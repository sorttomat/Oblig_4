"""
Dette programmet utforsker lister og loekker.
"""

listeMedTall = []

tall = float(input("Skriv inn et tall: "))
while tall != 0:
    listeMedTall.append(tall)
    tall = float(input("Skriv inn et tall: "))

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


