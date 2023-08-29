import os
from Interface import IColeccion
from Lista import ListaEnlazada
from Aparatos import Aparatos
from ManipularJSON import ManipularJSON
from ManejadorInterface import ManejadorInterface

if __name__=="__main__":

    Lista=ListaEnlazada()
    Manipulador=ManipularJSON()
    Manipulador.cargarObjeto(Lista)
    MI=ManejadorInterface()

    os.system("cls")
    opcion=0
    while(opcion!=-1):
        print("\n")
        print("1. Insertar")
        print("2. Agregar")
        print("3. Mostrar un Elemento")
        print("4. Mostrar la cantidad de elementos")
        print("5. Mostrar la marca de los lavarropas")
        print("6. Mostrar Toda la lista")
        print("7. Almacenar en un archivo")
        print("0. Salir")

        opcion=int(input("Ingrese una opcion: "))
        if opcion==1 or opcion==2 or opcion==3 or opcion==4 or opcion==5 or opcion==6 or opcion==7: 
            MI.setInterface(IColeccion(Lista),opcion)
        elif opcion==0:
            print("\n")
            print("Saliendo...")
            opcion=-1
        else: 
            print("Opcion no valida")
            
        

        
