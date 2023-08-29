class Equipo:
    __nom:str
    __ciu:str

    def __init__(self,nom:str,ciu:str):
        self.__nom=nom
        self.__ciu=ciu
    
    def getNom(self):
        return self.__nom