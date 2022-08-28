class Medicamentos:
    __id: int
    __idc: int
    __nom: str
    __mono: str
    __pres: str
    __cant: int
    __p: float

    def __init__(self, id:int, idc:int, nom:str, mono:str, pres:str, cant:int, p:float):
        self.__id=id
        self.__idc=idc
        self.__nom=nom
        self.__mono=mono
        self.__pres=pres
        self.__cant=cant
        self.__p=p
    
    def getId(self):
        return(self.__id)
    
    def getMonodroga(self):
        return(self.__mono)
    
    def getPresentacion(self):
        return(self.__pres)
    
    def getCantidad(self):
        return(self.__cant)
    
    def getPrecio(self):
        return(self.__p)
    


    