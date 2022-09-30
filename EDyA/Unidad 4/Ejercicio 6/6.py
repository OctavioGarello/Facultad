"""Ejercicio Nº6: Codifique un programa que simule el funcionamiento de la lista de espera del quirófano de un hospital.
Cada vez que el quirófano esté desocupado, se operará al paciente de mayor urgencia, dentro de esa lista de espera.
Al ingresar un paciente al hospital,además de solicitarle los datos personales,
se le asignará una prioridad relacionada con la gravedad de su caso."""

import numpy as np

class Paciente:
    __nombre: str
    __edad: int
    __prioridad: int

    def __init__(self, nombre: str, edad: int, prioridad: int):
        self.__nombre = nombre
        self.__edad = edad
        self.__prioridad = prioridad

    def __str__(self):
        return f"{self.__nombre} - {self.__edad} - {self.__prioridad}"

    def __gt__(self, other):
        return self.__prioridad > other.__prioridad

    def __lt__(self, other):
        if isinstance(other, Paciente):
            return self.__prioridad < other.__prioridad
        else:
            return self.__prioridad < other

    def __repr__(self):
        return f"( {self.__nombre} )"

class BinaryHeap:
    __items: np.ndarray
    __head: int=0

    def __init__(self,size):
        self.__items=np.empty(size,dtype=Paciente)
        self.__head=0
        self.__items[0]=-1

    def clear(self):
        return self.__head == 0

    def insert(self,item):
        self.__head+=1
        self.__items[self.__head]=item 

        current=self.__head
        previous=self.__head//2

        while self.__items[previous]>self.__items[current]:
            aux=self.__items[previous]
            self.__items[previous]=self.__items[current]
            self.__items[current]=aux

            current=self.__head
            previous=self.__head//2
    
    def suppress(self):
        item=self.__items[1]
        self.auxsuppress(1)
        self.__head-=1

        return item
    
    def degree(self,index):
        posLeft=index*2
        posRight=index*2+1

        if posLeft>self.__head:
            return 0
        
        elif posRight>self.__head:
            return 1
        
        else: 
            return 2
        
    def auxsuppress(self,index):
        if self.degree(index)==0:
            self.__items[index]=None
            return

        posLeft=index*2
        posRight=index*2+1

        itemLeft=self.__items[posLeft]
        itemRight=self.__items[posRight]

        if self.degree(index)==1:
            if itemLeft is None:
                self.__items[index]=itemRight
                self.auxsuppress(itemRight)
            
            else:
                self.__items[index]=itemLeft
                self.auxsuppress(itemLeft)
        
        elif self.degree(index)==2:
            if itemLeft < itemRight:
                self.__items[index]=itemLeft
                self.auxsuppress(itemLeft)
    
            else:
                self.__items[index]=itemRight
                self.auxsuppress(itemRight)

if __name__ == '__main__':
    monticulo = BinaryHeap(20)

    monticulo.insert(Paciente("Juan", 20, 1))
    monticulo.insert(Paciente("Pedro", 20, 2))
    monticulo.insert(Paciente("Maria", 20, 3))

    while True:
        opcion = int(input("""1. Agregar paciente
2. Atender paciente
3. Salir
Opcion: """))

        if opcion == 1:
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            prioridad = int(input("Prioridad: "))

            paciente = Paciente(nombre, edad, prioridad)
            monticulo.insert(paciente)
        elif opcion == 2:
            if monticulo.clear():
                print("No hay pacientes en la lista de espera")
            else:
                paciente = monticulo.suppress()
                print(f"Se atendió a {paciente}")
        elif opcion == 3:
            break
        else:
            print("Opción inválida")

