class Factura:

    __ValorTotal:int
    __CodigoFactura:str


    def __init__(self, detallesfactura[], datoscliente, metodopagar):

        self.__DetallesFactura = detallesfactura
        self.__DatosCliente = datoscliente
        self.__MetodoPagar = metodopagar