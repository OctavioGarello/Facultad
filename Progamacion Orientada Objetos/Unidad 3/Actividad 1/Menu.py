from ManejaFacultades import ManjeaFaultades
class Menu:
    __op: int
    def __init__(self):
        self.__op=0
    
    def getMenu(self):
        control=ManjeaFaultades()
        centinela=None
        while(centinela==None):
            self.__op=int(input("""
                                **Menu**
                Opcion[1]>> Ingresar un Codigo y luego Mostrar
                Opcion[2]>> Ingresar el Nombre de la Carrera y luego Mostrar
                Ingresar Opcion>> """))

            if(self.__op==1):
                control.setInciso1()

            if(self.__op==2):
                control.setInciso2()