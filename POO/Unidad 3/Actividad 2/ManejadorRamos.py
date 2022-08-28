from numpy import intp
from Ramo import Ramo
from ManejadorFlores import MFlores
class MRamos:
    __lista: list[Ramo]
    __mf: MFlores
    def __init__(self):
        self.__lista=[]
        self.__mf=MFlores()
    
    def CargarRamo(self):
        lista=[]
        tamaño=str(input("\n#Ingrese Tamaño de Ramo(Pequeño,Mediano,Grande)>> "))

        if tamaño=="Pequeño" or tamaño=="Mediano" or tamaño=="Grande":

            flor=str(input("Ingrese el tipo de Flor>> "))
            while((flor!="Fin") and (len(lista)<4)):
                instancia=self.__mf.buscarFlor(flor)
                lista.append(instancia)
                
                if(len(lista)<4):
                    flor=str(input("Ingrese el tipo de Flor>> "))
                else: flor="Fin"   

            instancia=Ramo(tamaño,lista) 
            self.__lista.append(instancia)

        else: print("Syntax Error")

    def Mostrar(self):
        diccionario: dict[str,int]={}
        for linea in self.__lista:
            for linea2 in linea.getListaFlores():
                nom=linea2.getNom()
                if nom in diccionario:
                    diccionario[nom] += 1
                else:
                    diccionario[nom] = 1
        
        lista = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)
        #Generas una lista con el diccionario con los items que son (str y int)
        #Elegis la llave es decir por lo que los vas a ordenar
        #Elegis si el ordes es ascendiente o decrecente, en este caso decreciente

        print("\n#Los 5 Tipos mas Vendidos:")
        i = 0
        while (i<5) and (i<len(lista)):
            print(" [%s]"%lista[i][0])
            i += 1
        #Esto dice que mientras la i<5 es decir no supere ese valor y depaso ese tampoco sea mayor a la cantidad va a funcionar
        """
         i= 0  (0='flor1',1= 3),
         i= 1  (0='flor2',1=1),
         i= 2  (0='flor3',1=4),
          """
    def Ingresar(self):
        nom=str(input("\n#Ingrese el nombre de un Tipo de Ramo>> "))
        lista=[]

        if nom=="Pequeño" or nom=="Mediano" or nom=="Grande":
            for ramo in self.__lista:
                if(nom==ramo.getTamaño()):
                    for flor in ramo.getListaFlores():
                        if(flor.getNom() not in lista):
                            lista.append(flor.getNom()) 

            for nomflor in lista:
                    print("[%s]"%(nomflor))
                    
                
        else:print("Syntax Error")