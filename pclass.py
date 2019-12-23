class Bostad:

    def __init__(self, pris, yta, hyra, tfn, adress, månadskostnad, ytkostnad):
        self.pris = int(pris)
        self.yta = float(yta)                       # ska kunna vara decimaltal
        self.hyra = int(hyra)
        self.tfn = str(tfn)
        self.adress = str(adress)
        self.månadskostnad = float(månadskostnad)   # avrundas vid beräkning till en decimal
        self.ytkostnad = float(ytkostnad)           # avrundas vid beräkning till en decimal

    # metod för att printa bostäderna, "" utgör tomrum
    def __repr__(self):
        return "\nBoyta:{0:<14s}".format("") + str(self.yta) + " kvm\nPris:{0:>15s}".format("") + str(self.pris) + \
               " kr\nHyra:{0:>15s}".format("") + str(self.hyra) + "kr\nTelNr:{0:>14s}".format("") + str(self.tfn) + \
               "\nGatuadress:{0:>9s}".format("") + str(self.adress) + "\nMånadskostnad:{0:>6s}".format("") + \
               str(self.månadskostnad) + "kr\nKvadratmeterpris:{0:>3s}".format("") + str(self.ytkostnad) + "kr/kvm"

class Urval:

    def __init__(self, uMånadskostnad, uHyra, uKvmpris, uYta):   #u = urval, dvs uHyra = urvalshyra osv.
        self.uMånadskostnad = int(uMånadskostnad)
        self.uHyra = int(uHyra)
        self.uKvmpris = int(uKvmpris)
        self.uYta = int(uYta)

    def justera_uMk (self, nyuMånadskostnad):    # metod för att ändra maximala månadskostnaden i urvalet
        self.uMånadskostnad = nyuMånadskostnad

    def justera_uH (self, nyuHyra):              # metod för att ändra maximala hyran i urvalet
        self.uHyra = nyuHyra

    def justera_uKvmp (self, nyuKvmpris):        # metod för att ändra maximala kvadratmeterpriset i urvalet
        self.uKvmpris = nyuKvmpris

    def justera_uY (self, nyuYta):               # metod för att ändra minsta boendeytan i urvalet
        self.uYta = nyuYta

    def __repr__(self): # metod som printar Grundmenyn
        return "\nDina valmöjligheter: \n1) Ändra önskad Månadskostnad (< " + str(self.uMånadskostnad) + " kkr)\n2) Ändra önskad Hyra (< " +\
               str(self.uHyra) + " kkr) \n3) Ändra önskat Kvadratmeterpris (< " + str(self.uKvmpris) + " kkr/kvm) \n4) Ändra önskad Boendeyta " \
                 "(> " + str(self.uYta) + " kvm)\n5) Skapa Urval \n6) Avsluta"