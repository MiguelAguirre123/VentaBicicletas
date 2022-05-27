from datetime import date

class MetodoPago:

    _NumOperacion:str
    _FechaPago:date
    _MonedaPago:str
    _CuentaBeneficiario:str
    _Monto:str

    def CrearMetodoPago(self, numoperacion:str, fechapago:date, monedapago:str, cuentabeneficiario:str, monto:str):

        self._NumOperacion = numoperacion
        self._FechaPago = fechapago
        self._MonedaPago = monedapago
        self._CuentaBeneficiario = cuentabeneficiario
        self._Monto = monto

    def CrearPago(self):
        pass