from Aparatos import Aparatos

class Televisores(Aparatos):
    __tipoPantalla: str
    __pulgadas: float
    __tipoDefinicion: str
    __conexionInternet: bool

    def __init__(self, marca: str, modelo: str, color: str, pais: str, precio: float, tipoPantalla: str, pulgadas: float, tipoDefinicion: str, conexionInternet: bool):
        super().__init__(marca, modelo, color, pais, precio)
        self.__tipoPantalla = tipoPantalla
        self.__pulgadas = pulgadas
        self.__tipoDefinicion = tipoDefinicion
        self.__conexionInternet = conexionInternet
    
    
    def toJson(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    marca= self.getMarca(),
                    modelo= self.getModelo(),
                    color= self.getColor(),
                    pais= self.getPais(),
                    precio= self.getPrecio(),
                    tipoPantalla = self.__tipoPantalla,
                    pulgadas= self.__pulgadas,
                    tipoDefinicion= self.__tipoDefinicion,
                    conexionInternet= self.__conexionInternet
                )
            )
        return d