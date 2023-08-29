from Calefactor import Calefactor

class Gas(Calefactor):
    __matricula: str
    __calorias: int
    __costo: float
    def __init__(self, marca:str, modelo:str, matricula:str, calorias:int, costo:float):
        super().__init__(marca,modelo)
        self.__matricula=matricula
        self.__calorias=calorias
        self.__costo=costo
    
    def getCostoConsumo(self):
        return self.__calorias*self.__costo
    
    def getMatricula(self):
        return self.__matricula
    
    def getCosto(self):
        return self.__costo
    
    def getTipo(self):
        return("Gas")