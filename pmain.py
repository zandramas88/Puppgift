from pclass import*

def Startup_Settings():
        Bankränta = int(input("Vänligen ange den aktuella bankräntan (%):"))
        Kontantinsats = int(input("Vänligen ange din kontantinsats (kr):"))
        Ränteavdrag = int(input("Vänligen ange det aktuella ränteavdraget (%):"))
        
        return Bankränta, Kontantinsats, Ränteavdrag #bör beräkningarna göras här direkt?

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
        uMånadskostnad,uHyra,uKvmpris,uBoendeyta = rad.split(",",4)
        U = Urval(int(pMånadskostnad),int(pHyra),int(pKvadrameterpris),int(pBoendeyta))
        Urvals_lista.append(U)
    return Urvals_lista
    f.close

def spara_filU(Urvals_lista): #öppnar textfilen och ändrar innehållet till den uppdaterade Urvals_lista (Behövs det äns? Urvalet behöver ju inte sparas mellan körningar...)
        f=open("purval.txt", "w")
        for Urval in Urvals_lista:
            uMånadskostnad = Urval.uMånadskostnad
            uHyra = Urval.uHyra
            uKvmpris = Urval.uKvmpris
            uBoendeyta = Urval.uBoendeyta
            f.write(str(uMånadskostnad)+", "+str(uHyra)+", "+str(uKvmpris)+", "+str(uBoendeyta)+"\n")
        f.close()

def Grundmeny():
        while True:
                try:
                        Justera_Parameter = int(input("Dina valmöjligheter: \n1) Ändra önskad Månadskostnad (< "" kkr) \n2) Ändra önskad Hyra (< "" kkr) \n3) Ändra önskat Kvadratmeterpris (< "" kkr) \n4) Ändra önskad Boendeyta (> "" kvm)\n5) Skapa Urval \n6) Avsluta"))
                except ValueError:
                        Justera_Parameter = 7

                if Justera_Parameter == 1:
                        ändra_uMånadskostnaden()

                elif Justera_Parameter == 2:
                        ändra_uHyra()

                elif Justera_Parameter == 3:
                        ändra_uKvmpris()

                elif Justera_Parameter == 4:
                        ändra_uBoendeyta()

                elif Justera_Parameter == 5:
                        #skapa Urval

                elif Justera_Parameter == 6:
                        exit()

                else:
                        print("Vänligen välj något av de ovanstående alternativen!\n")

def ändra_uMånadskostnaden():
        while True:
                try:
                        ny_uMånadskostnad = int(input("Månadskostnaden ska högst vara (kkr): "))

                except ValueError:
                        print("Vänligen skriv in en siffra!")

                if ny_uMånadskostnad >= 0:
                        Urval.ändra_uMånadskostnad(ny_uMånadskostnad)
                        break
                else:
                        print("Vänligen skriv in ett tal större än 0!")

def ändra_uHyra():
        while True:
                try:
                        ny_uHyra = int(input("Hyran ska högst vara (kkr): "))
                        
                except ValueError:
                        print("Vänligen skriv in en siffra!")

                if ny_uHyra >= 0:
                        Urval.ändra_uHyra(ny_uHyra)
                        break
                else:
                        print("Vänligen skriv in ett tal större än 0!")

def ändra_uKvmpris():
        while True:
                try:
                        ny_uKvmpris = int(input("Kvadratmeterpriset ska högst vara (kkr): "))
                        
                except ValueError:
                        print("Vänligen skriv in en siffra!")

                if ny_uKvmpris >= 0:
                        Urval.ändra_uKvmpris(ny_uKvmpris)
                        break
                else:
                        print("Vänligen skriv in ett tal större än 0!")

def ändra_uBoendeyta():
        while True:
                try:
                        ny_uBoendeyta = int(input("Boendeytan ska minst vara (kvm): "))
                        
                except ValueError:
                        print("Vänligen skriv in en siffra!")

                if ny_uBoendeyta >= 0:
                        Urval.ändra_uBoendeyta(ny_uBoendeyta)
                        break
                else:
                        print("Vänligen skriv in ett tal större än 0!")


