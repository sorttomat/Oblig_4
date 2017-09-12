

def leggTilVenn(dict):
    navn = input("Navn? ")
    bursdag = [int(input("Dag: ")), int(input("Maaned: ")), int(input("Aar: "))]
    dict[navn] = bursdag
    return dict

vennerBursdager = {}

maaneder = {
    "Januar" : 1,
    "Februar" : 2,
    "Mars" : 3,
    "April" : 4,
    "Mai" : 5,
    "Juni" : 6,
    "Juli" : 7,
    "August" : 8,
    "September" : 9,
    "Oktober" : 10,
    "November" : 11,
    "Desember" : 12
}

for i in range(5):
    leggTilVenn(vennerBursdager)


for key in vennerBursdager:
    for mndkey in maaneder:
        if maaneder[mndkey] == vennerBursdager[key][1]:
            print("{} har bursdag {}. {} {}".format(key, vennerBursdager[key][0], mndkey, vennerBursdager[key][2]))



