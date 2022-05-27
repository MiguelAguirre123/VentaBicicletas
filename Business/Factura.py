from Business.Detalle import Detalle
from Business.MetodoPago import MetodoPago
from Business.Persona import Persona

class Factura:

    _ValorTotal:int
    _CodigoFactura:str


    def __init__(self, detallesfactura:Detalle, datoscliente:Persona, metodopagar:MetodoPago):

        self._DetallesFactura = detallesfactura
        self._DatosCliente = datoscliente
        self._MetodoPagar = metodopagar

    def CrearFactura(self, valortotal:int, codigofactura:str):

        self._ValorTotal = valortotal
        self._CodigoFactura = codigofactura