#valg = input("Hva onsker du aa gjore?\n Legg til en film (1)\n Fjern en film (2)\n Oversikt over alle filmer (3)\n Informasjon om en film (4)\n Finn hylleplassering (5)\n Avslutte (6)\n\n\n\n> ")

dic = {
    "c": 1,
    "h": 2,
    "a": 3
}

for key in sorted(dic):
    print(key)