from Aparatos import Aparatos

class Heladeras(Aparatos):
    __capacidad: float
    __freezer: bool
    __cyclica: bool

    def __init__(self, marca: str, modelo: str, color: str, pais: str, precio: float, capacidad: float, freezer: bool, cyclica: bool):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidad = capacidad
        self.__freezer = freezer
        self.__cyclica = cyclica
    
    def toJson(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    marca= self.getMarca(),
                    modelo= self.getModelo(),
                    color= self.getColor(),
                    pais= self.getPais(),
                    precio= self.getPrecio(),
                    capacidad = self.__capacidad,
                    freezer= self.__freezer,
                    cyclica= self.__cyclica
                )
            )
        return d
