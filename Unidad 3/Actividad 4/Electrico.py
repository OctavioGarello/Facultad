from Calefactor import Calefactor

class Electrico(Calefactor):
    __potmax: int
    def __init__(self, marca:str, modelo:str, potmax:int, costo:float):
        super().__init__(marca,modelo)
        self.__potmax = potmax
        self.__costo = costo

    def getCostoConsumo(self):
        return self.__potmax*self.__costo
    
    def getPotmax(self):
        return self.__potmax
    
    def getCosto(self):
        return self.__costo
    
    def getTipo(self):
        return("Electrico")