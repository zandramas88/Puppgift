class Bostad():
      def __init__(self,Boyta,Pris,Hyra,TelNr,Gatuadress,Månadskostnad,Ytkostnad):#klassen skapas med attributen 
         self.Boyta = Boyta
         self.Pris = Pris
         self.Hyra = Hyra
         self.TelNr = TelNr
         self.Gatuadress = Gatuadress
         self.Månadskostnad = Månadskostnad
         self.Ytkostnad = Ytkostnad

      def __str__(self):#metod för att skriva ut den aktuella TVn och dess konfigurationer
          return "\n"+self.Boyta+" \nPris: "+str(self.Pris)+"\nHyra: "+str(self.Hyra)+"\nTelNr: "+self.Gatuadress+"\nMånadskostnad: "+str(self.Månadskostnad)+"\nYtkostnad: "+str(self.Ytkostnad)+"\n"

      def Bestäm_Månadskostnaden(self, Hyra, Pris, Kontantinsats, Ränta, Ränteavdrag):
          self.Månadskostnaden = Hyra + ((Pris-Kontantinsats)*(Ränta/100)*(1-Ränteavdrag/100))/12

      def Bestäm_Ytkostnaden(self, Boyta, Pris):
          self.Ytkostnaden = Boyta/Pris


class Urval():
      def __init__(self,pMånadskostnad,pHyra,pKvadratmeterpris,pBoendeyta):#klassen skapas med attributen (p=parameter)
            self.pMånadskostnad = pMånadskostnad
            self.pHyra = pHyra
            self.pKvadratmeterpris = pKvadratmeterpris
            self.pBoendeyta = pBoendeyta

      def ändra_pMånadskostnad(self, ny_pMånadskostnad):
            self.pMånadskostnad = ny_pMånadskostnad

      def ändra_pHyra(self, ny_pHyra):
            self.pHyra = ny_pHyra

      def ändra_pKvadrameterpris(self, ny_pKvadrameterpris):
            self.pKvadrameterpris = ny_pKvadratmeterpris

      def ändra_pBoendeyta(self, ny_pBoendeyta):
            self.pBoendeyta = ny_pBoendeyta
