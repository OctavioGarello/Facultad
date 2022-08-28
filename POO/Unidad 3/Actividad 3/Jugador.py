from datetime import datetime

class Jugador:
    __nom:str
    __dni:str
    __cn:str
    __po:str
    __fn: datetime
    def __init__(self,nom:str,dni:str,cn:str,po:str,fn:str):
        self.__nom=nom
        self.__dni=dni
        self.__cn=cn
        self.__po=po
        self.__fn= datetime.strptime(fn, "%d/%m/%Y")
    
    def getNom(self):
        return(self.__nom)  
    
    def getDni(self):
        return(self.__dni)

    