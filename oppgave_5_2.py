filmhylle = {}

def leggTilFilm(dic):
    tittel = input("Hva er tittelen til filmen? ")
    sjanger = input("Hvilken sjanger er filmen? ")
    regissor = input("Hvem har regissert filmen? ")
    aar = input("Hvilket aar ble filmen utgitt? ")
    hylleplassering = None
    dic[tittel] = [regissor, sjanger, aar, hylleplassering]
    leggTilHylleplassering(dic) 

def leggTilHylleplassering(dic):
    teller = 0
    for key in sorted(dic):
        dic[key][-1] = teller
        teller += 1
    return dic

def printAlleFilmer(dic):
    for key in sorted(dic):
        print("Tittel: {} \n Regissor: {} \n Sjanger: {} \n Utgivelsesaar: {} \n Hylleplassering: {} ".format(key, dic[key][0], dic[key][1], dic[key][2], dic[key][3]))

def printEnFilm(dic, tittel):
    if tittel in dic:
        print("Tittel: {} \n Regissor: {} \n Sjanger: {} \n Utgivelsesaar: {} \n Hylleplassering: {} ".format(tittel, dic[tittel][0], dic[tittel][1], dic[tittel][2], dic[tittel][3]))

 def fjernFilm(dic, tittel):
     dic.pop(tittel)

def finnHylleplassering(dic, tittel):
    if tittel in dic:
        print("{} er plassert paa plass {} i hylla.".format(tittel, dic[tittel[-1]]))
         

def filmhylleProgram(dic):
    valg = input("Hva onsker du aa gjore?\n Legg til en film (1)\n Fjern en film (2)\n Oversikt over alle filmer (3)\n Informasjon om en film (4)\n Finn hylleplassering (5)\n Avslutte (6)\n\n\n\n> ")
    muligheter = ["1", "2", "3", "4", "5", "6"]
    while valg not in muligheter:
        print("Ugyldig kommando.")
        valg = input("Hva onsker du aa gjore?\n Legg til en film (1)\n Fjern en film (2)\n Oversikt over alle filmer (3)\n Informasjon om en film (4)\n Finn hylleplassering (5)\n Avslutte (6)\n\n\n\n> ")

    if valg == "1":
        leggTilFilm(dic)
    elif valg == "2":
        svar = input("Hvilken film vil du fjerne? Tast 1 hvis du vil se en oversikt over filmene dine.\n>")
        if svar == "1":
            printAlleFilmer(dic)
        else:
            fjernFilm(dic, svar)
    elif valg == "3":
        print("Her er en oversikt over alle filmene i hylla:")
        printAlleFilmer(dic)
    elif valg == "4":
        svar = input("Hvilken film onsker du informasjon om? ")
        
