class Apartment:

    def __init__(self, pris, yta, hyra, tfn, adress):
        try:
            self._pris = int(pris) # Require integer
        except ValueError:
            raise Exception("Price not valid: " + pris)

        try:
            self._yta = float(yta) # Sample data says float
        except ValueError:
            raise Exception("Area not valid: " + yta)

        try:
            self._hyra = int(hyra) # Require integer
        except ValueError:
            raise Exception("Rent not valid: " + hyra)

        self._tfn = str(tfn) # treat as string

        self._adress = str(adress) # treat as string

    # mainly for print(..) friendly representation during debug
    def __repr__(self):
        return str(self._pris) + "/" + str(self._yta) + "/" + str(self._hyra) \
               + "/" + str(self._tfn) + "/" + str(self._adress)


def mapFileToAptObjects(f_name):
    ''' Function maps data in file f_name to Apartment obects amd returns list of
        Apartment objects
    '''
    ret = []
    i = 0

    with open(f_name,'r') as file:
        file.readline() # skip header line in file
        data = file.readlines() # read rest of lines to python list
        file.close()

    if len(data) % 5 != 0: #5 rows per item required
        raise Exeception('Five lines per item required')

    while i < len (data):
        # create apartment objects, remove trailing newlines from data
        ret.append(Apartment(data[i].rstrip(),
                    data[i+1].rstrip(),
                    data[i+2].rstrip(),
                    data[i+3].rstrip(),
                    data[i+4].rstrip()))
        i+=5

    return ret


apts = mapFileToAptObjects('indata.dat')

for apt in apts:
    print(apt)
