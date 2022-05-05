class Cama:
    __id: int
    __h: int
    __e: bool #(booleano, true indica ocupada, false indica libre)
    __nom: str|None #(valor None si no está ocupada)
    __d: str
    __fi: str
    __fa: str
    
    def __init__(self, id:int, h:int, e:bool, nom:str|None, d:str, fi:str, fa:str):
        self.__id=id
        self.__h=h
        self.__e=e
        self.__nom=nom
        self.__d=d
        self.__fi=fi
        self.__fa=fa
    
    def getNombre(self):
        return(self.__nom)
    
    def getCama(self):
        return(self.__id)
    
    def getHabitacion(self):
        return(self.__h)
    
    def getDiagnostico(self):
        return(self.__d)

    def getFi(self):
        return(self.__fi)

    def getFa(self):
        return(self.__fa)    

    def modificar(self,fecha):
        self.__e=False
        self.__fa=fecha
    
    def modificarNom(self):
        self.__nom=None
