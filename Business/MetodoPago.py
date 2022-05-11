from datetime import date

class MetodoPago:

    _NumOperacion:str
    _FechaPago:date
    _MonedaPago:str
    _CuentaBeneficiario:str
    _Monto:str

    def CrearMetodoPago(self):

        self._NumOperacion = input("Introduzca el numero de operacion: ")

        ano = int(input("Introduzca el ano en la que se realiza la transaccion: "))
        mes = int(input("Introduzca el mes en la que se realiza la transaccion: "))
        dia = int(input("Introduzca el dia en la que se realiza la transaccion: "))

        self._FechaPago = date(ano, mes, dia)

        self._MonedaPago = input("Introduzca el tipo de moneda con la que se va a pagar: ")
        self._CuentaBeneficiario = input("Introduzca la cuenta del beneficiario: ")
        self._Monto = input("Introduzca el monto: ")
