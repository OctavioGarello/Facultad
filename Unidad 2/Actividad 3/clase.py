class Registro:
    __vtemperatura: float=0
    __vhumedad: int=0
    __vpatmosferica: int=0

    def __init__(self, vt:float, vh:int, vpa:int):
        self.__vtemperatura=vt
        self.__vhumedad=vh
        self.__vpatmosferica=vpa
    
    def getTemp(self):
        return(self.__vtemperatura)
    
    def getHumedad(self):
        return(self.__vhumedad)
    
    def getPatmosferica(self):
        return(self.__vpatmosferica)



