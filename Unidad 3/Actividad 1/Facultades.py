from Carreras import Carreras
class Facultades:
    __cod:int
    __nom:str
    __dir:str
    __loc:str
    __tel:str
    __lista:list[Carreras]

    def __init__(self,cod:int,nom:str,dir:str,loc:str,tel:str):
        self.__cod=cod
        self.__nom=nom
        self.__dir=dir
        self.__loc=loc
        self.__tel=tel
        self.__lista=[]

    def setAgregar(self,linea:list[str]):
        instancia=Carreras(int(linea[1]),linea[2],linea[3],linea[4],linea[5])
        self.__lista.append(instancia)

    def getNom(self):
        return(self.__nom)   

    def getCod(self):
        return(self.__cod)

    def getCarreras(self):
        return(self.__lista)
    
    def getDir(self):
        return(self.__dir)