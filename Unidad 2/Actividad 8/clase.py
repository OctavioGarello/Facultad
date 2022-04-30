from __future__ import annotations

class Conjunto:
    __lista=[]
    
    def __init__(self,lista_num:list[int]):
        self.__lista=lista_num

    def getLista(self):
        return(self.__lista)
    
    def __add__(self,otro:Conjunto):
        lista=self.__lista.copy()
        self.__lista.sort()
        otro.__lista.sort()

        for i in otro.__lista:
            if i not in lista:
                lista.append(i)

        return Conjunto(lista)

    def __sub__(self,otro:Conjunto):
        lista=self.__lista.copy()


        for elemento in otro.getLista():
            if elemento in lista:
                lista.remove(elemento)
    
        return Conjunto(lista)
    
    def __eq__(self, otro:Conjunto):
        lista=self.__lista
        b=True

        if len(lista)!=len(otro.getLista()):
            b=False

        for elemento in otro.getLista():
            if elemento not in lista:
                b=False
                
        return(b)


