"""Listas: En una aerolínea ofrece una promoción a sus viajeros frecuentes
que consiste en acumular puntos por los viajes que realizan, pudiendo luego recibir 
beneficios a través del canje de puntos.
Usted trabaja en el área de sistemas de la aerolínea y le han 
solicitado la implementación de un sistema capaz de gestionar la promoción. Respetando el siguiente diseño de clase:(esta en clase)

1- Leer de un archivo separado por comas los datos para crear instancias de la clase ViajeroFrecuente, y 
almacenarlas en una lista.

2- Lea por teclado un número de viajero frecuente y presente un menú con las siguientes opciones:

a- Consultar Cantidad de Millas.

b- Acumular Millas.

c- Canjear Millas.

3- Represente el almacenamiento en memoria para la lista cargada con 4 viajeros.

"""
from clase import ViajeroFrecuente
import csv

def test():
    print("------------\n#TEST")
    instancia=ViajeroFrecuente(1,"43281084","Octavio","Garello",500)
    acum=100
    print("Cantidad:[%s]"%(instancia.cantidadTotalMillas()))
    print("Acumular [%d] Millas: [Total:%d]"%(acum,instancia.acumularMillas(acum)))
    print("Canjear [%d] Millas: [Total:%d]"%(acum,instancia.canjearMillas(acum)))
    print("------------\n")


if __name__=="__main__":
    test()
    #Leer archivo 
    with open("Actividad 2\\viajeros.csv","r") as archivo:
        lista = csv.reader(archivo,delimiter=',')#Es mi lista
        
        #Leer por teclado
        print("----")
        num_viajero=int(input("Ingresar Num. Viajero: "))

        instancia=None
        for linea in lista:
            if(num_viajero==int(linea[0])):
                instancia=ViajeroFrecuente(int(linea[0]), linea[1], linea[2], linea[3], int(linea[4]))
        if(instancia==None):           
           print("Error")
        else:   
            
            menu=int(input("""
#Menu
-Seleccione >[1] Consultar Millas
-Seleccione >[2] Acumular Millas
-Seleccione >[3] Canjear Millas

-Ingrese Opcion(0 Finaliza): 
            """)) 

            while(menu!=0):
                if(menu==1):
                    print("-----")
                    print("*Cantidad:"+str(instancia.cantidadTotalMillas()))

                elif(menu==2):
                    print("-----")
                    acumulador=int(input("*Ingrese Millas para acumular: "))

                elif(menu==3):
                    print("-----")
                    canjear=int(input("*Ingrese Millas para Canjear: "))
                    
                elif(menu==0):
                    print("-----")
                    print("Finalizo")

                else: print("Error")

                print("-----")
                print("")
                menu=int(input("-Ingrese Opcion(0 Finaliza):"))

                       

    









