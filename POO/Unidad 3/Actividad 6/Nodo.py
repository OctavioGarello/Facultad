from __future__ import annotations
from Aparatos import Aparatos

class Nodo:
    __dato: Aparatos
    __siguiente: None

    def __init__(self, dato:Aparatos):
        self.__dato = dato
        self.__siguiente = None
    
    def getDato(self):
        return self.__dato
    
    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente