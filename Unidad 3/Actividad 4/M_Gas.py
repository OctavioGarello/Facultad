from Gas import Gas
import numpy as np
import csv

class M_Gas:
    __arrG: np.ndarray

    def __init__(self,ruta):
        self.__arrG = np.empty(0, dtype=Gas)
        self.LeerArchivo(ruta)
        #self.Mostrar()
    
    def LeerArchivo(self,ruta):
        with open(ruta,"r") as archivo:
            contenido=csv.reader(archivo,delimiter=";")
            next(contenido)
            for linea in contenido:
                    self.__arrG = np.append(self.__arrG, Gas(linea[0],linea[1],linea[2],int(linea[3]),float(linea[4])))#type: ignore 

    def Mostrar(self):
        print("Gas:")
        for i in self.__arrG:
            print("%s"%(i.getMarca()))
    
    def getArrG(self):
        return self.__arrG
    
    def Ingresar(self):
        costo=float(input("Ingrese el costo por m3:"))
        cantidad=float(input("Ingrese la cantidad que se estima consumir en m3:"))
        total=costo*cantidad
        print("El/Los calefactor/es de menor costo de consumo son:")
        for i in self.__arrG:
            if i.getCostoConsumo()<=total:
                print("Calefactor[%s]:Modelo[%s] Matricula[%s] Costo[%.2f] Costo Consumo[%.2f]"%(i.getTipo(),i.getModelo(),i.getMatricula(),i.getCosto(),i.getCostoConsumo()))

