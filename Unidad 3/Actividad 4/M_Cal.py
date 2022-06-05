import numpy as np
from Calefactor import Calefactor
from M_Elec import M_Elec
from M_Gas import M_Gas

class M_Cal:
    __arrC: np.ndarray

    def __init__(self,Electrico,Gas):
        self.__arrC = np.empty(0, dtype=Calefactor)
        self.cargarArreglo(Electrico,Gas)
        #self.Mostrar()
    
    def cargarArreglo(self,Electrico,Gas):
        tamaño=len(Electrico)+len(Gas)
        self.__arrC = np.empty(tamaño, dtype=Calefactor)

        for i in range(0,tamaño):
            if(i<len(Electrico)):
                self.__arrC[i]=Calefactor(Electrico[i].getMarca(),Electrico[i].getModelo())
            elif(i>=len(Electrico)):
                self.__arrC[i]=Calefactor(Gas[i-len(Electrico)].getMarca(),Gas[i-len(Electrico)].getModelo())
        
    def Mostrar(self):
        print("Calefactor:")
        for i in self.__arrC:
            print("%s"%(i.getMarca()))
    
