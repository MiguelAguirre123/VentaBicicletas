from Business.Bicicleta import Bicicleta

class Detalle:

    _CantidadProducto:int
    _IdDetalle:str


    def __init__(self, producto:Bicicleta):

        self._Producto = producto

    def CrearDetalle(self, cantidadproducto:int, iddetalle:str):

        self._CantidadProducto = cantidadproducto
        self._IdDetalle = iddetalle