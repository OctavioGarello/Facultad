
from controlador import Controlador
from clase import PlanAhorro
import os

class Menu:
    __op: int
    __control: Controlador 

    def __init__(self):
        self.__op=0
        self.__control=Controlador()
    
    def mostrar(self):
        centinela=None
        while(centinela!=0):
            self.__op=int(input("""
            **Menu**        
Opcion ->[1] : Actualizar(Valor del vehículo de cada plan)
Opcion ->[2] : Mostrar Valores Inferiores [Cod. Plan] [Modelo] [Version](Ingrese el Importe)
Opcion ->[3] : Mostrar monto licitado para c/plan
Opcion ->[4] : Modificar Cuotas Licitadas

Ingrese Opcion-> """))
            if(self.__op==1):
               self.opcion1()

            elif(self.__op==2):
                self.opcion2()

            elif(self.__op==3):
                self.opcion3()

            elif(self.__op==4):
                self.opcion4()

            elif(self.__op==0):
                centinela=0
            else:
                print("Error")

    def opcion1(self):
        os.system("cls")
        self.__control.modificar()
    
    def opcion2(self):
        os.system("cls")
        self.__control.buscar()

    def opcion3(self):
        os.system("cls")
        self.__control.monto()

    def opcion4(self):
        os.system("cls")
        self.__control.modificar2()
