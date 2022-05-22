class Carreras:
    __cod:int
    __nom:str
    __fi:str
    __dur:str
    __tit:str

    def __init__(self,cod:int,nom:str,fi:str,dur:str,tit:str):
        self.__cod=cod
        self.__nom=nom
        self.__fi=fi
        self.__dur=dur
        self.__tit=tit
    
    def setMostrar(self):
        print("Carrera: [%s]    Duracion:[%s]"%(self.__nom,self.__dur))
    
    def getNom(self):
        return(self.__nom)
        
    def getCod(self):
        return(self.__cod)
