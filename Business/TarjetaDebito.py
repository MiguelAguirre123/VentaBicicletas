from Business.MetodoPago import MetodoPago

class TarjetaDebito(MetodoPago):

    NumTarjeta:str
    Contrasena:int

    def CrearPago(self, numtarjeta:str, contrasena:int):

        self.NumTarjeta = numtarjeta
        self.Contrasena = contrasena