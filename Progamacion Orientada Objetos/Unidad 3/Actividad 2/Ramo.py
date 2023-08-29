import numpy as np
from Flores import Flores

class Ramo:
    __tam:str
    __listaFlores:list[Flores]

    def __init__(self,tam:str,lista):
        self.__tam=tam
        self.__listaFlores=lista
    
    def getListaFlores(self):
        return(self.__listaFlores)

    def getTamaño(self):
        return(self.__tam)

    