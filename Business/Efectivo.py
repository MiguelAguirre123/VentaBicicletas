from Business.MetodoPago import MetodoPago

class Efectivo(MetodoPago):

    ValorPagar:int

    def CrearPago(self, valorpagar:int):

        self.ValorPagar = valorpagar