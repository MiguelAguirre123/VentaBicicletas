from Business.CuentaAhorro import CuentaAhorro
from Funciones.GestionarMetodoPago import GestionarMetodoPago
import pandas as pd

def GestionarCuentaAhorro():

    cuentaahorro = None

    while cuentaahorro == None:
        
        print("¿Que Quiere Hacer?")
        print("1. Crear un metodo de pago por cuenta de ahorro")
        print("2. Buscar un metodo de pago por cuenta de ahorro existente")
        num = int(input("Introduzca un numero: "))

        if num == 1:

            valores_metodopago = GestionarMetodoPago()

            numcuenta = input("Introduzca la cuenta de ahorro: ")
            contrasena = int(input("Introduzca la contrasena de la cuenta de ahorro: "))

            cuentaahorro = CuentaAhorro()

            cuentaahorro.CrearMetodoPago(valores_metodopago[0], valores_metodopago[1],
            valores_metodopago[2], valores_metodopago[3], valores_metodopago[4])
            cuentaahorro.CrearPago(numcuenta, contrasena)

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")
            
            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/CuentaAhorro/{nombre_archivo}.csv').empty == False:
                    
                    df_cuentaahorro = pd.read_csv(f'Datos/Archivos_Guardados/CuentaAhorro/{nombre_archivo}.csv')

                    numoperacion = str(df_cuentaahorro["|NumOperacion|"][0])
                    fechapago = df_cuentaahorro["|FechaPago|"][0]
                    monedapago = str(df_cuentaahorro["|MonedaPago|"][0])
                    cuentabeneficiario = str(df_cuentaahorro["|CuentaBeneficiario|"][0])
                    monto = str(df_cuentaahorro["|Monto|"][0])
                    numcuenta = str(df_cuentaahorro["|NumCuenta|"][0])
                    contrasena = int(df_cuentaahorro["|Contrasena|"][0])
            
                    cuentaahorro = CuentaAhorro()

                    cuentaahorro.CrearMetodoPago(numoperacion, fechapago, monedapago,
                    cuentabeneficiario, monto)
                    cuentaahorro.CrearPago(numcuenta, contrasena)

            except FileNotFoundError:
                print("No se encontro el archivo")             
    
    return cuentaahorro, num