from Business.Diseno import Diseno
from Business.Referencia import Referencia

class InventarioReferencia:

    _CantidadBodega:int
    _CantidadMostrador:int
    _CantidadVendida:int
    _IdInventario:str


    def __init__(self, referencia:Referencia, diseno:Diseno):

        self._Referenciacion = referencia
        self._Diseno = diseno

    def CrearInventarioReferencia(self, cantidadbodega:int, cantidadmostrador:int,
    cantidadvendida:int, idinventario:str):

        self._CantidadBodega = cantidadbodega
        self._CantidadMostrador = cantidadmostrador
        self._CantidadVendida = cantidadvendida
        self._IdInventario = idinventario
