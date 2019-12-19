from pclass import

def läs_filB():#öppnar textfilen med alla Bostäder och lägger dem i Bostad_lista
        f = open("pbostad.txt", "r")
        allt = f.readlines()
        Bostad_lista = []

        for rad in allt:
                Boyta,Pris,Hyra,TelNr,Gatuadress = rad.split(",",5)
                B= Bostad(int(Boyta), int(Pris), int(Hyra), int(TelNr), Gatuadress)
                Bostad_lista.append(B)
        return Bostad_lista
        f.close()

def läs_filU(): #öppnar fillen med urvals inställningarna
    f = open("purval.txt", "r")
    allt = f.readlines()
    Urvals_lista = []

    for rad in allt:
        pMånadskostnad,pHyra,pKvadrameterpris,pBoendeyta = rad.split(",",4)
        U = Urval(int(pMånadskostnad),int(pHyra),int(pKvadrameterpris),int(pBoendeyta))
        Urvals_lista.append(U)
    return Urvals_lista
    f.close

def spara_filU(Urvals_lista): #öppnar textfilen och ändrar innehållet till den uppdaterade Urvals_lista
        f=open("purval.txt", "w")
        for Urval in Urvals_lista:
            pMånadskostnad = Urval.pMånadskostnad
            pHyra = Urval.pHyra
            pKvadratmeterpris = Urval.pKvadratmeterpris
            pBoendeyta = Urval.pBoendeyta
            f.write(str(pMånadskostnad)+", "+str(pHyra)+", "+str(pKvadratmeterpris)+", "+str(pBoendeyta)+"\n")
        f.close()
