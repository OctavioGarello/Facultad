import csv
import numpy as np
from Flores import Flores

class MFlores:
    __arreglo: np.ndarray

    def __init__(self):
        self.__arreglo= np.array(self.getArreglo())
    
    def getArreglo(self):
        with open("flores.csv","r") as archivo:
            contenido=csv.reader(archivo,delimiter=";")
            lista=[]
            next(contenido)
            for linea in contenido:
                instancia=Flores(int(linea[0]),linea[1],linea[2],linea[3])
                lista.append(instancia)
            
        return(lista)

    def buscarFlor(self,flor:str):
        i=0
        while((i<len(self.__arreglo))and(self.__arreglo[i].getNom()!=flor)):
            i=i+1

        if i>=len(self.__arreglo):
            raise Exception("Error")
        else:
            return(self.__arreglo[i])


    