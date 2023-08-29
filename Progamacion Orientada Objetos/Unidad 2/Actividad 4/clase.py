class Ventana:
    __titulo: str
    __xsup: int
    __ysup: int
    __xinf: int 
    __yinf: int

    def __init__(self,titulo=None,xsup=0,ysup=0,xinf=400,yinf=400):
        self.__titulo=titulo
        self.__xsup=xsup
        self.__ysup=ysup
        self.__xinf=xinf 
        self.__yinf=yinf

    def validar(self):
        if  self.__xsup<0 or self.__ysup<0:
            print("*** Error de Coordenadas ***") 
        if  self.__xinf>500 or self.__yinf>500:
            print("*** Error de Coordenadas ***") 
        if (self.__xinf< self.__xsup) or (self.__yinf < self.__ysup):
            print("*** Error de Coordenadas ***") 

    def getTitulo(self):
        return(self.__titulo)
    
    def alto(self):
        return(self.__xinf-self.__xsup)

    def ancho(self):
        return(self.__yinf-self.__ysup)

    def mostrar(self):
        print("""
        Titulo=[%s]
        Xsup=[%d] Xinf=[%d]
        Ysup=[%d] Yinf=[%d]"""%(self.__titulo,self.__xsup,self.__xinf,self.__ysup,self.__yinf))

    def moverDerecha(self,mover:int):
        self.__xinf=self.__xinf + mover
        self.__xsup=self.__xsup + mover
        self.validar()

    def moverIzquierda(self,mover2:int):
        self.__xinf=self.__xinf - mover2
        self.__xsup=self.__xsup - mover2
        self.validar()

    def bajar(self,mover3=1):
        self.__yinf=self.__yinf + mover3
        self.__ysup=self.__ysup + mover3
        self.validar()

    def subir(self,mover4=1):
        self.__yinf=self.__yinf - mover4
        self.__ysup=self.__ysup - mover4
        self.validar()