# Johan Johannisson Lundquist 12/23-2019

from pclass import *

def mapFileToBostadObjects(f_name):  # funktion för att ta in data från indata.txt och skapa Bostad objekt. Returnerar lista av dessa objekt

    ret = []
    i = 0
    b, k, r = StartupSettings()  # b = bankränta, k = kontantinsats, r = ränteavdrag

    with open(f_name, "r") as file:
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


def StartupSettings():  # funktion för att ta in nödvändiga inputs, med felhantering och ser till att rimliga värden, dvs >=0, matas in
    while True:
        try:
            bankränta = float(input("Vänligen ange den aktuella bankräntan (%): "))
            if bankränta >= 0:
                break
            else:
                print("Ange ett positivt tal.")
        except ValueError:
            print("Vänligen ange ett tal!")
    while True:
        try:
            kontantinsats = int(input("Vänligen ange din kontantinsats (kr): "))
            if kontantinsats >= 0:
                break
            else:
                print("Ange ett positivt tal.")
        except ValueError:
            print("Vänligen ange ett tal!")
    while True:
        try:
            ränteavdrag = float(input("Vänligen ange det aktuella ränteavdraget (%): "))
            if ränteavdrag >= 0:
                break
            else:
                print("Ange ett positivt tal.")
        except ValueError:
            print("Vänligen ange ett tal!")
    return bankränta, kontantinsats, ränteavdrag


def mapFileToUrvalObjects(f_name):               # funktion för att skapa grundinställningarna för urvalet från settings.txt
    with open(f_name, "r") as file:
        file.readline()                          # skippar första raden
        data = file.readline()
        file.close()
    uMånadskostnad, uHyra, uKvmpris, uYta = data.split(",", 4)
    U = Urval(int(uMånadskostnad), int(uHyra), int(uKvmpris), int(uYta))
    return U

def SkapaUrval():                                                              # funktion för att skapa och visa urvalet som valts
    print("\nDitt urval:")
    for hus in bostad:
        if hus.månadskostnad < urval.uMånadskostnad * 1000 and \
                hus.hyra < urval.uHyra * 1000 and \
                hus.ytkostnad < urval.uKvmpris * 1000 and \
                hus.yta > urval.uYta:
            wait = input("\nTryck var som helst för nästa bostad i urvalet:")  # bostäderna från urvalet ska presenteras en i taget
            print(hus)
        else:
            continue


def Grundmeny():         # funktion som sköter menyn
    while True:
        print(urval)     # grundinställningarna från settings.txt
        try:
            Justera_Parameter = int(input(":"))
        except ValueError:
            Justera_Parameter = 7

        if Justera_Parameter == 1:
            while True:
                try:
                    nyuMånadskostnad = int(input("Månadskostnaden ska högst vara (kkr): "))
                    urval.justera_uMk(nyuMånadskostnad)
                    break
                except ValueError:
                    print("Vänligen ange ett heltal.")

        elif Justera_Parameter == 2:
            while True:
                try:
                    nyuHyra = int(input("Hyran ska högst vara (kkr): "))
                    urval.justera_uH(nyuHyra)
                    break
                except ValueError:
                    print("Vänligen ange ett heltal.")

        elif Justera_Parameter == 3:
            while True:
                try:
                    nyuKvmpris = int(input("Kvadratmeterpriset ska högst vara (kkr/kvm): "))
                    urval.justera_uKvmp(nyuKvmpris)
                    break
                except ValueError:
                    print("Vänligen ange ett heltal.")

        elif Justera_Parameter == 4:
            while True:
                try:
                    nyuYta = int(input("Boendeytan ska minst vara (kvm): "))
                    urval.justera_uY(nyuYta)
                    break
                except ValueError:
                    print("Vänligen ange ett heltal.")

        elif Justera_Parameter == 5:
            SkapaUrval()

        elif Justera_Parameter == 6:
            exit()

        else:
            print("Vänligen välj något av de ovanstående alternativen.")

bostad = mapFileToBostadObjects("indata.txt")
for hus in bostad:  # printar bostäderna första gången
    print(hus)
urval = mapFileToUrvalObjects("settings.txt")
Grundmeny()
