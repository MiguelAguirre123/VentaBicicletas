from Business.TarjetaCredito import TarjetaCredito
from Funciones.GestionarMetodoPago import GestionarMetodoPago
import pandas as pd

def GestionarTarjetaCredito():

    tarjetacredito= None

    while tarjetacredito == None:
        
        print("¿Que Quiere Hacer?")
        print("1. Crear un metodo de pago por tarjeta de credito")
        print("2. Buscar un metodo de pago por tarjeta de credito existente")
        num = int(input("Introduzca un numero: "))

        if num == 1:

            valores_metodopago = GestionarMetodoPago()

            numtarjeta = input("Introduzca el numero de la tarjeta credito: ")
            contrasena = int(input("Introduzca la contrasena de la tarjeta credito: "))

            tarjetacredito = TarjetaCredito()

            tarjetacredito.CrearMetodoPago(valores_metodopago[0], valores_metodopago[1],
            valores_metodopago[2], valores_metodopago[3], valores_metodopago[4])
            tarjetacredito.CrearPago(numtarjeta, contrasena)           

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")
            
            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/TarjetaCredito/{nombre_archivo}.csv').empty == False:
                    
                    df_tarjetacredito = pd.read_csv(f'Datos/Archivos_Guardados/TarjetaCredito/{nombre_archivo}.csv')

                    numoperacion = str(df_tarjetacredito["|NumOperacion|"][0])
                    fechapago = df_tarjetacredito["|FechaPago|"][0]
                    monedapago = str(df_tarjetacredito["|MonedaPago|"][0])
                    cuentabeneficiario = str(df_tarjetacredito["|CuentaBeneficiario|"][0])
                    monto = str(df_tarjetacredito["|Monto|"][0])
                    numtarjeta = str(df_tarjetacredito["|NumTarjeta|"][0])
                    contrasena = int(df_tarjetacredito["|Contrasena|"][0])

                    tarjetacredito = TarjetaCredito()

                    tarjetacredito.CrearMetodoPago(numoperacion, fechapago, monedapago,
                    cuentabeneficiario, monto)
                    tarjetacredito.CrearPago(numtarjeta, contrasena)                     

            except FileNotFoundError:
                print("No se encontro el archivo")             
    
    return tarjetacredito, num