"""
Dette programmet holder oversikten over filmene paa en filmhylle. 
"""

from ezgraphics import GraphicsWindow

def leggTilFilm(dic, tittel, sjanger, regissor, aar):
    """
    Funksjon som legger til informasjon om en film i dictionaryen (filmhylla).
    """
    hylleplassering = None #Hylleplasseringen blir bestemt paa linje 13.
    dic[tittel] = [regissor, sjanger, aar, hylleplassering]
    leggTilHylleplassering(dic) #Oppdaterer hylleplassering

def leggTilHylleplassering(dic):
    """
    Funksjon som endrer hylleplasseringen utifra den alfabetiske rekkefolgen
    paa filmene. 
    """
    plassering = 1
    for key in sorted(dic):
        dic[key][3] = plassering
        plassering += 1
    return dic

def printAlleFilmer(dic):
    """
    Funksjon som printer ut alle filmene paa hylla i alfabetisk rekkefolge.
    """
    for key in sorted(dic):
        print(" Tittel: {} \n Regissor: {} \n Sjanger: {} \n Utgivelsesaar: {} \n Hylleplassering: {} ".format(key, dic[key][0], dic[key][1], dic[key][2], dic[key][3]))

def printEnFilm(dic, tittel):
    """
    Funksjon som printer ut imformasjon om en bestemt film.
    """
    if tittel in dic:
        print(" Tittel: {} \n Regissor: {} \n Sjanger: {} \n Utgivelsesaar: {} \n Hylleplassering: {} ".format(tittel, dic[tittel][0], dic[tittel][1], dic[tittel][2], dic[tittel][3]))

def printAlleTitler(dic):
    """
    Funksjon som printer ut alle titlene i filmhylla.
    """
    for key in sorted(dic):
        print(key)

def fjernFilm(dic, tittel):
    """
    Funksjon som fjerner en film.
    """
    dic.pop(tittel)

def finnHylleplassering(dic, tittel):
    """
    Funksjon som printer ut hvilken plassering en film har paa hylla.
    """
    if tittel in dic:
        print("{} er plassert paa plass {} i hylla.".format(tittel, dic[tittel][3]))

def meny():
    """
    Funksjon som printer ut menyen, og tar imot valget til brukeren.
    """
    valg = input("\n\nHva onsker du aa gjore?\n Legg til en film (1)\n Fjern en film (2)\n Oversikt over alle filmer (3)\n Informasjon om en film (4)\n Finn hylleplassering (5)\n Vis filmhylle (6)\n Avslutt (7)\n\n\n\n> ")
    muligheter = ["1", "2", "3", "4", "5", "6", "7"]
    while valg not in muligheter:
        print("Ugyldig kommando.")
        valg = input("\n\nHva onsker du aa gjore?\n Legg til en film (1)\n Fjern en film (2)\n Oversikt over alle filmer (3)\n Informasjon om en film (4)\n Finn hylleplassering (5)\n Vis filmhylle (6)\n Avslutt (7)\n\n\n\n> ")
    return valg

def displayFilmhylle(dic):
    """
    Funksjon som viser innholdet paa filmhylla i et eget vindu.
    Denne har jeg ikke faatt til aa fungere. 
    """
    win = GraphicsWindow(500, 500)
    can = win.canvas()
    y = 0
    for key in dic:
        #st = key + dic[key][0] + dic[key][1] + dic[key][2] + dic[key][3]
        st = "hei" #Testet en enkel string
        can.drawText(0, y, st)
        y += 20
    win.wait()

def filmhylleProgram(dic):
    """
    Selve programmet. Det spor brukeren om hva hen vil gjore, og handler utifra 
    det. 
    """
    valg = meny()
    while valg != "7":
        if valg == "1":
            tittel = (input("Hva er tittelen til filmen? ")).lower()
            sjanger = (input("Hvilken sjanger er filmen? ")).lower()
            regissor = (input("Hvem har regissert filmen? ")).lower()
            aar = input("Hvilket aar ble filmen utgitt? ")
            leggTilFilm(dic, tittel, sjanger, regissor, aar) 
            print("\n\nLa til {}.".format(tittel))

        elif valg == "2":
            svar = input("Hvilken film vil du fjerne? Tast 1 hvis du vil se en oversikt over filmene dine.\n>")
            if svar == "1":
                printAlleFilmer(dic)
                svar = input("Hvilken film vil du fjerne?\n>")
                fjernFilm(dic, svar)
            else:
                fjernFilm(dic, svar)

        elif valg == "3":
            if len(dic) == 0:
                print("Du har ingen filmer i hylla ennaa.")
            else:
                print("Her er en oversikt over alle filmene i hylla:")
                printAlleFilmer(dic)

        elif valg == "4":
            if len(dic) == 0:
                print("Du har ingen filmer ennaa.")
            else:    
                svar = input("Hvilken film onsker du informasjon om? Tast 1 om du onsker en oversikt over titlene dine.\n> ")
                if svar == "1":
                    printAlleTitler(dic)
                    svar = input("Hvilken film onsker du informasjon om?\n>")
                    printEnFilm(dic, svar)
                else:
                    printEnFilm(dic, svar)

        elif valg == "5":
            svar = input(("Hvilken film leter du etter? Tast 1 om du onsker en oversikt over titlene dine.\n>"))
            if svar == "1":
                printAlleTitler(dic)
                svar = input(("Hvilken film leter du etter?\n>"))
                finnHylleplassering(dic, svar)
            else:
                finnHylleplassering(dic, svar)
        elif valg == "6":
            displayFilmhylle(dic)
        valg = meny()

    

filmhylle = {}

filmhylleProgram(filmhylle)
        
