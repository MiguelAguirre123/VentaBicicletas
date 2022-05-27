from Business.MetodoPago import MetodoPago

class CuentaAhorro(MetodoPago):

    NumCuenta:str
    Contrasena:int

    def CrearPago(self, numcuenta:str, contrasena:int):

        self.NumCuenta = numcuenta
        self.Contrasena = contrasena