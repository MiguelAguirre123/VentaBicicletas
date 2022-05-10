class Factura:

    _ValorTotal:int
    _CodigoFactura:str


    def __init__(self, detallesfactura[], datoscliente, metodopagar):

        self._DetallesFactura = detallesfactura
        self._DatosCliente = datoscliente
        self._MetodoPagar = metodopagar