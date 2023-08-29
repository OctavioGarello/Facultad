from Aparatos import Aparatos
from Heladeras import Heladeras
from Lavarropa import Lavarropas
from Televisores import Televisores
from Interface import IColeccion

class ManejadorInterface:
    def setInterface(self,Lista:IColeccion,opcion):
        if opcion==1:
            print("\n")
            tipo=input("Ingrese el tipo de aparato(Heladeras, Lavarropa, Televisores): ")
            posicion=int(input("Ingrese la posicion: "))
            if tipo=="Heladeras":
                Lista.insertarElemento(posicion,Heladeras(input("Ingrese la marca: "),input("Ingrese el modelo: "),input("Ingrese el color: "),input("Ingrese el pais: "),float(input("Ingrese el precio: ")),float(input("Ingrese la capacidad: ")),bool("Ingrese si tiene freezer: "),bool("Ingrese si tiene cyclica: ")))
            elif tipo=="Lavarropa":
                Lista.insertarElemento(posicion,Lavarropas(input("Ingrese la marca: "),input("Ingrese el modelo: "),input("Ingrese el color: "),input("Ingrese el pais: "),float(input("Ingrese el precio: ")),float(input("Ingrese la capacidad: ")),int(input("Ingrese la velocidad: ")),int(input("Ingrese la cantidad de programas: ")),input("Ingrese el tipo de carga: ")))
            elif tipo=="Televisores":
                Lista.insertarElemento(posicion,Televisores(input("Ingrese la marca: "),input("Ingrese el modelo: "),input("Ingrese el color: "),input("Ingrese el pais: "),float(input("Ingrese el precio: ")),input("Ingrese el tipo de pantalla: "),float(input("Ingrese la pulgadas: ")),input("Ingrese el tipo de definicion: "),bool("Ingrese si tiene conexion a internet: ")))
            else:
                print("Tipo de aparato no valido")

        elif opcion==2:
            print("\n")
            tipo=input("Ingrese el tipo de aparato(Heladeras, Lavarropa, Televisores): ")
            if tipo=="Heladeras":
                Lista.agregarElemento(Heladeras(input("Ingrese la marca: "),input("Ingrese el modelo: "),input("Ingrese el color: "),input("Ingrese el pais: "),float(input("Ingrese el precio: ")),float(input("Ingrese la capacidad: ")),bool("Ingrese si tiene freezer: "),bool("Ingrese si tiene cyclica: ")))
            elif tipo=="Lavarropa":
                Lista.agregarElemento(Lavarropas(input("Ingrese la marca: "),input("Ingrese el modelo: "),input("Ingrese el color: "),input("Ingrese el pais: "),float(input("Ingrese el precio: ")),float(input("Ingrese la capacidad: ")),int(input("Ingrese la velocidad: ")),int(input("Ingrese la cantidad de programas: ")),input("Ingrese el tipo de carga: ")))
            elif tipo=="Televisores":
                Lista.agregarElemento(Televisores(input("Ingrese la marca: "),input("Ingrese el modelo: "),input("Ingrese el color: "),input("Ingrese el pais: "),float(input("Ingrese el precio: ")),input("Ingrese el tipo de pantalla: "),float(input("Ingrese la pulgadas: ")),input("Ingrese el tipo de definicion: "),bool("Ingrese si tiene conexion a internet: ")))
            else:
                print("Tipo de aparato no valido")

        elif opcion==3:
            print("\n")
            posicion=int(input("Ingrese la posicion: "))
            Lista.mostrarElementoLista(posicion)

        elif opcion==4:
            print("\n")
            Lista.mostrarCantidadLista()

        elif opcion==5:
            print("\n")
            Lista.mostrarMarcaLavarropas()

        elif opcion==6:
            print("\n")
            Lista.mostrarLista()
        
        elif opcion==7:
            print("\n")
            ruta="aparatosNuevo.json"
            Lista.GuardarJson(ruta)
        

        
