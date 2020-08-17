# Johan Johannisson Lundquist 12/23-2019 (Ändrad 17/8-2020)

from pclass import *

def skapaBostad(f_namn):  # funktion för att ta in data från indata.txt och skapa Bostad objekt. Returnerar lista av dessa objekt

    ret = []
    i = 0
    b, k, r = grundInställningar()  # b = bankränta, k = kontantinsats, r = ränteavdrag

    with open(f_namn, "r") as file:
        file.readline()          # skippar första raden
        data = file.readlines()  # läser in resterande raderna
        file.close()

    while i < len(data):                       # skapar bostad objekten i listan ret
        ret.append(Bostad(data[i].rstrip(),    # pris
                          data[i+1].rstrip(),  # yta
                          data[i+2].rstrip(),  # hyra
                          data[i+3].rstrip(),  # tfn
                          data[i+4].rstrip(),  # adress
                          round(int(data[i+2].rstrip()) + ((int(data[i].rstrip())-k)*(b/100)*(1-(r/100)))/12, 1),
                                               # månadskostnad
                          round(int(data[i].rstrip()) / float(data[i+1].rstrip()), 1)))
                                               # ytkostnad
        i += 5                                 # ny bostad efter 5 rader i filen
    return ret

def inner(text):
    while True:
        try:
            x = float(input(text))
            if x >= 0:
                break
            else:
                print("Ange ett positivt tal.")
        except ValueError:
            print("Vänligen ange ett tal!")
    return x

def fåBankränta():
    return inner("Vänligen ange den aktuella bankräntan (%): ")

def fåKontantinsats():
    return inner("Vänligen ange din kontantinsats (kr): ")

def fåRänteavdrag():
    return inner("Vänligen ange det aktuella ränteavdraget (%): ")

def grundInställningar():  # funktion för att ta in nödvändiga inputs
    bankränta = fåBankränta()
    kontantinsats = fåKontantinsats()
    ränteavdrag = fåRänteavdrag()
    return bankränta, kontantinsats, ränteavdrag

def skapaGrundUrval(f_namn):                     # funktion för att skapa grundinställningarna för urvalet från urval.txt
    with open(f_namn, "r") as file:
        file.readline()                          # skippar första raden
        data = file.readline()
        file.close()
    uMånadskostnad, uHyra, uKvmpris, uYta = data.split(",", 4)
    U = Urval(int(uMånadskostnad), int(uHyra), int(uKvmpris), int(uYta))
    return U

def skapaUrval(bostad,urval,wl,bl):                                                                     # funktion för att skapa och visa urvalet som valts
    print("\nDitt urval:")
    for hus in bostad:
        if hus.månadskostnad < urval.uMånadskostnad * 1000 and \
                hus.hyra < urval.uHyra * 1000 and \
                hus.ytkostnad < urval.uKvmpris * 1000 and \
                hus.yta > urval.uYta:
            input("\n-----\nTryck var som helst för nästa bostad i urvalet:")  # bostäderna från urvalet ska presenteras en i taget
            print(hus)
            wl.append(hus)
        else:
            bl.append(hus)
            continue
    return wl,bl

def grundmeny(bostad,urval,wl,bl):         # funktion som sköter menyn
    while True:
        print(urval)     # grundinställningarna från urval.txt
        try:
            justeraParameter = int(input(":"))
        except ValueError:
            justeraParameter = 7

        if justeraParameter == 1:
            nyuMånadskostnad = fåMånadskostnad()
            urval.justera_uMk(nyuMånadskostnad)

        elif justeraParameter == 2:
            nyuHyra = fåHyran()
            urval.justera_uH(nyuHyra)

        elif justeraParameter == 3:
            nyuKvmpris = fåKvmpris()
            urval.justera_uKvmp(nyuKvmpris)

        elif justeraParameter == 4:
            while True:
                try:
                    nyuYta = int(input("Boendeytan ska minst vara (kvm): "))
                    urval.justera_uY(nyuYta)
                    break
                except ValueError:
                    print("Vänligen ange ett heltal.")

        elif justeraParameter == 5:
            wl,bl = skapaUrval(bostad,urval,wl,bl) #wl&bl fylls i utifrån de önskade urvalsparametrarna
            wl = sortU(bostad,urval,wl,bl)  #wl sorteras utifrån parameter som väljs
            wl = redigeraUrval(bostad,urval,wl,bl)
            print("Här är ditt urval:\n")
            for hus in wl:
                print(hus)
            saveU("lista_bostadsurval.txt", wl)  # skriver ut urvalet i nämnd txt fil

        elif justeraParameter == 6:
            saveU("lista_bostadsurval.txt", wl)  # skriver ut urvalet i nämnd txt fil
            exit()

        else:
            print("Vänligen välj något av de ovanstående alternativen.")

def redigeraUrval(bostad,urval,wl,bl):
    x = menyredigeraUrval()
    if x == 1:
        return wl
        #grundmeny(bostad, urval, wl, bl) #återvänder
    elif x == 2:
        if len(bl) == 0:
            print("Det finns inga bostäder att lägga till i ditt urval")
            redigeraUrval(bostad,urval,wl,bl)
        else:
            for hus in bl:
                print(hus)
                print("\nVill du lägga till den här bostaden i ditt urval? Tryck 1 för Ja eller 2 för Nej\n")
                while True:
                    try:
                        edit = int(input(":"))
                    except ValueError:
                        edit = 3
                    if edit == 1:
                        wl.append(hus)
                        bl.remove(hus)
                        break
                    elif edit == 2:
                        break
                    else:
                        print("Vänligen ange ett av de ovanstående alternativen!")
            return wl, bl
    elif x == 3:
        if len(wl) == 0:
            print("Ditt urval är tomt")
            redigeraUrval(bostad, urval, wl, bl)
        else:
            for hus in wl:
                print(hus)
                print("\nVill du ta bort den här bostaden i ditt urval? Tryck 1 för Ja eller 2 för Nej\n")
                while True:
                    try:
                        edit = int(input(":"))
                    except ValueError:
                        edit = 3
                    if edit == 1:
                        bl.append(hus)
                        wl.remove(hus)
                        break
                    elif edit == 2:
                        break
                    else:
                        print("Vänligen ange ett av de ovanstående alternativen!")
            return wl, bl

def menyredigeraUrval():
    while True:
        try:
            meny = int(input("\nVill du redigera ditt urval?\n1) Nej\n2) Ja, jag vill lägga till en bostad\n3) Ja, jag vill ta bort en bostad\n:"))
        except ValueError:
            meny == 4
        if meny in range(1,4):
            return meny
        else:
            print("Vänligen ange ett av de ovanstående alternativen!")

def felHantering(text):
    while True:
        try:
            x = int(input(text))
            if x >= 0:
                break
            else:
                print("Ange ett positivt tal.")
        except ValueError:
            print("Vänligen ange ett tal!")
    return x

def fåMånadskostnad():
    return felHantering("Månadskostnaden ska högst vara (kkr): ")

def fåHyran():
    return felHantering("Hyran ska högst vara (kkr): ")

def fåKvmpris():
    return felHantering("Kvadramterpriset ska högst vara (kkr): ")

def sortU(bostad,urval,wl,bl): # ska sortera lista med objekt... elr finns annat sätt?
    x = menySortU()
    for hus in wl:
        if x == 1:
            wl = sorted(wl, key=lambda hus: float(hus.månadskostnad))
        elif x == 2:
            wl = sorted(wl, key=lambda hus: int(hus.hyra))
        elif x == 3:
            wl = sorted(wl, key=lambda hus: float(hus.ytkostnad))
        elif x == 4:
            wl = sorted(wl, key=lambda hus: float(hus.yta), reverse=True)
        elif x == 5:
            continue
            #skippa sortering
        else:
            grundmeny(bostad,urval,wl,bl) #gå till grundmeny
    return wl

def menySortU():
    while True:
        try:
            VilkenParameter = int(input("\nUtifrån vilken parameter skulle du vilja sortera urvalet efter?\n1) Månadskostnad\n2) Hyra\n3) Kvadratmeterpris\n"
                                        "4) Boendeyta \n5) Ingen \n6) Återvänd till Grundmenyn\n:"))
        except ValueError:
            VilkenParameter == 7
        if VilkenParameter in range(1,7):
            return VilkenParameter
        else:
            print("Vänligen ange ett av de ovanstående alternativen!")

def saveU(f_namn,bostad):
    i = 1
    with open(f_namn, "w") as file: #skriver över den från förra körningen
        for hus in bostad:
            file.write(str(i)+"."+str(hus)+"\n\n")
            i = i+1
    file.close()

def uppstart():
    wl = []
    bl = []
    bostad = skapaBostad("indata.txt")
    for hus in bostad:  # printar bostäderna första gången
        print(hus)
    urval = skapaGrundUrval("urval.txt")
    grundmeny(bostad,urval,wl,bl)
    return bostad,urval

uppstart()
