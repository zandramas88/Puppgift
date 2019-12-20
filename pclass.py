class Bostad():
      def __init__(self,Boyta,Pris,Hyra,TelNr,Gatuadress,Månadskostnad,Ytkostnad):#klassen skapas med attributen 
         self.Boyta = Boyta
         self.Pris = Pris
         self.Hyra = Hyra
         self.TelNr = TelNr
         self.Gatuadress = Gatuadress
         self.Månadskostnad = Månadskostnad
         self.Ytkostnad = Ytkostnad

      def __str__(self):#metod för att skriva ut en viss Bostad och dess stats
          return "\n"+self.Boyta+" \nPris: "+str(self.Pris)+"\nHyra: "+str(self.Hyra)+"\nTelNr: "+self.Gatuadress+"\nMånadskostnad: "+str(self.Månadskostnad)+"\nYtkostnad: "+str(self.Ytkostnad)+"\n"

      def Bestäm_Månadskostnaden(self, Hyra, Pris, Kontantinsats, Ränta, Ränteavdrag):
          self.Månadskostnaden = Hyra + ((Pris-Kontantinsats)*(Ränta/100)*(1-Ränteavdrag/100))/12

      def Bestäm_Ytkostnaden(self, Boyta, Pris):
          self.Ytkostnaden = Boyta/Pris


class Urval():
      def __init__(self,uMånadskostnad,uHyra,uKvmpris,uBoendeyta):#klassen skapas med attributen (u=urval)
            self.uMånadskostnad = uMånadskostnad
            self.uHyra = uHyra
            self.uKvmpris = uKvmpris
            self.uBoendeyta = uBoendeyta

      def ändra_uMånadskostnad(self, ny_uMånadskostnad):
            self.uMånadskostnad = ny_uMånadskostnad

      def ändra_uHyra(self, ny_uHyra):
            self.uHyra = ny_uHyra

      def ändra_uKvmpris(self, ny_uKvmpris):
            self.uKvmpris = ny_uKvmpris

      def ändra_uBoendeyta(self, ny_uBoendeyta):
            self.uBoendeyta = ny_uBoendeyta
