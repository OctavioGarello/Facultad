class Flores:
    __num:int
    __nom:str
    __color:str
    __des:str
    
    def __init__(self,num:int,nom:str,color:str,des:str):
        self.__num=num
        self.__nom=nom
        self.__color=color
        self.__des=des
    
    def getNom(self):
        return(self.__nom)