from datetime import date

def GestionarMetodoPago():

    numoperacion = input("Introduzca el numero de operacion: ")

    ano = int(input("Introduzca el ano en la que se realiza la transaccion: "))
    mes = int(input("Introduzca el mes en la que se realiza la transaccion: "))
    dia = int(input("Introduzca el dia en la que se realiza la transaccion: "))

    fechapago = date(ano, mes, dia)

    monedapago = input("Introduzca el tipo de moneda con la que se va a pagar: ")
    cuentabeneficiario = input("Introduzca la cuenta del beneficiario: ")
    monto = input("Introduzca el monto: ")

    return numoperacion, fechapago, monedapago, cuentabeneficiario, monto