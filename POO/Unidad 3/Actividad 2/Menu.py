from ManejadorRamos import MRamos
class Menu:
    __opcion: int
    __control: MRamos
    def __init__(self):
        self.__opcion=0
        self.__control=MRamos() 
    def getOpcion(self):
        centinela=None
        while(centinela==None):
            self.__opcion=int(input("""\n**Menu**
Opcion >>[1] : Registrar un Ramo
Opcion >>[2] : Mostrar las 5 Flores mas Pedidas en un Ramo
Opcion >>[3] : Ingresar y Mostrar Flores de un tipo de Ramo
Opcion >>[0] : Finalizar Programa
Ingrese Opcion>> """))

            if (self.__opcion==1):
                self.__control.CargarRamo()
            
            elif (self.__opcion==2):
                self.__control.Mostrar()

            elif(self.__opcion==3):
                self.__control.Ingresar()
         
            elif(self.__opcion==0):
                Centinela=0

            else:
                print("Syntax Error")
