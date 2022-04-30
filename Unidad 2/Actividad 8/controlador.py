from clase import Conjunto

class Controlador:
    __conjunto1=Conjunto([1,2,3])
    __conjunto2=Conjunto([1,2,3])
    def __init__(self):
        self.__conjunto1
        self.__conjunto2
    
    def mostrar(self):
        print("\n**Mostrar Conjuntos**")
        print("#Conjunto A:{}\n#Conjunto B:{}".format(self.__conjunto1.getLista(),self.__conjunto2.getLista()))
    
    def union(self):
        print("\n**Union de Conjuntos**")
        conj_union=self.__conjunto1+self.__conjunto2
        print("Union A + B :{}".format(conj_union.getLista()))
    
    def diferencia(self):
        print("\n**Diferencia de Conjuntos**")
        conj_diferencia=self.__conjunto1-self.__conjunto2
        print("Diferencia A - B :{}".format(conj_diferencia.getLista()))
    
    def verificacion(self):
        print("\n**Verificacion de Conjuntos**")
        conj_verificacion=self.__conjunto1==self.__conjunto2
        print("Verificacion A == B :{}".format(conj_verificacion))        




