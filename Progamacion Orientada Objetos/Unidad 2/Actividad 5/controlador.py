import csv
from clase import PlanAhorro


class Controlador:
    __nomarchivo:str
    __lista: list[PlanAhorro]

    def __init__(self):
        self.__nomarchivo="planes.csv"
        self.__lista=self.getLista()

    def getLista(self):

        with open(self.__nomarchivo,"r") as archivo:
            ListaArchivo= csv.reader(archivo,delimiter=";")
            lista=[]
            for linea in ListaArchivo:
                instancia=PlanAhorro(int(linea[0]),str(linea[1]),str(linea[2]),int(linea[3]))
                instancia.setCambiarVcp(int(linea[4]))
                instancia.setCambiarVcl(int(linea[5]))
                lista.append(instancia)
                
            return(lista)

    def modificar(self):

        i=0
        print("\n**Cambiar**")
        for plan in self.__lista:
            i+=1
            print("Plan [%d]: (Cod:[%d]) (Modelo:[%s]) (Version:[%s]) (Valor:[%d])"%(i,plan.getCodigo(),plan.getModelo(),plan.getVersion(),plan.getValor()))
            nuevo=int(input("Ingrese nuevo Valor--> "))
            plan.cambiarValor(nuevo)

        i=0
        print("\n**Valores Modificados**")
        for plan in self.__lista:
            i+=1
            print("Plan [%d]: (Nuevo Valor:[%d])"%(i,plan.getValor()))

    def buscar(self):
        
        print("\n**Buscar**")
        num=float(input("Ingresa un Valor--> "))

        print("\n**Los valores Inferiores son:**")
        for linea in self.__lista:
            if(linea.valorCuota()<num):
                print("Cod Plan:[%d]|| Modelo:[%s] || Version[%s]"%(linea.getCodigo(),linea.getModelo(),linea.getVersion()))

    def monto(self):

        i=0
        print("\n**Mostrar**")
        for linea in self.__lista:
            i+=1
            print("Plan[%d]: (Monto Licito[%.2f])"%(i,linea.montoLicitado()))
    
    def modificar2(self):

        print("\n**Modificar**")
        print("\nCantidad Actual:[%d]"%(self.__lista[0].getCantidadVl()))
        num=float(input("Ingresa un Valor--> "))
        self.__lista[0].setCambiarVcl(num)
        print("Nueva Cantidad:[%d]"%(self.__lista[1].getCantidadVl()))

    def modificar3(self):
        num=float(input("Ingresa un Valor--> "))
        PlanAhorro.setCambiarVcl(num)
        print("Nueva Cantidad:[%d]"%(self.__lista[1].getCantidadVl())) #Otra manera de hacer el modificar2
    