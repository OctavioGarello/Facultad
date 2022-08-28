class PlanAhorro:
    __codigo:int
    __modelo:str
    __version:str
    __valor:int
    __cantplan: int=0
    __cantlicitar: int=0

    def __init__(self,cod,mod,vers,val):
        self.__codigo=cod
        self.__modelo=mod
        self.__version=vers
        self.__valor=val
    
    def getCodigo(self):
        return(self.__codigo)

    def getModelo(self):
        return(self.__modelo)
    
    def getVersion(self):
        return(self.__version)
        
    def getValor(self):
        return (self.__valor)
    
    def getcantCuotas(self):
        return (self.__cantplan)
    
    def cambiarValor(self, nuevo:int):
        self.__valor=nuevo

    def valorCuota(self):
        vc:float=(self.__valor/self.__cantplan)+self.__valor*0.10
        return(vc)
    
    def montoLicitado(self):
        ml:float=(self.getCantidadVl() * self.valorCuota())
        return(ml)
        
    @classmethod
    def setCambiarVcp(cls,cp):
        cls.__cantplan=cp

    @classmethod    
    def setCambiarVcl(cls,cl):
        cls.__cantlicitar=cl

    @classmethod
    def getCantidadVc(cls):
        return(cls.__cantplan)
    
    @classmethod
    def getCantidadVl(cls):
        return(cls.__cantlicitar)