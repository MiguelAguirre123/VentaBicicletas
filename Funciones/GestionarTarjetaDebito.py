from Business.TarjetaDebito import TarjetaDebito
from Funciones.GestionarMetodoPago import GestionarMetodoPago
import pandas as pd

def GestionarTarjetaDebito():

    tarjetadebito= None

    while tarjetadebito == None:
        
        print("¿Que Quiere Hacer?")
        print("1. Crear un metodo de pago por tarjeta de debito")
        print("2. Buscar un metodo de pago por tarjeta de debito existente")
        num = int(input("Introduzca un numero: "))

        if num == 1:

            valores_metodopago = GestionarMetodoPago()

            numtarjeta = input("Introduzca el numero de la tarjeta credito: ")
            contrasena = int(input("Introduzca la contrasena de la tarjeta credito: "))

            tarjetadebito = TarjetaDebito()

            tarjetadebito.CrearMetodoPago(valores_metodopago[0], valores_metodopago[1],
            valores_metodopago[2], valores_metodopago[3], valores_metodopago[4])
            tarjetadebito.CrearPago(numtarjeta, contrasena)  

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")
            
            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/TarjetaDebito/{nombre_archivo}.csv').empty == False:
                    
                    df_tarjetadebito = pd.read_csv(f'Datos/Archivos_Guardados/TarjetaDebito/{nombre_archivo}.csv')

                    numoperacion = str(df_tarjetadebito["|NumOperacion|"][0])
                    fechapago = df_tarjetadebito["|FechaPago|"][0]
                    monedapago = str(df_tarjetadebito["|MonedaPago|"][0])
                    cuentabeneficiario = str(df_tarjetadebito["|CuentaBeneficiario|"][0])
                    monto = str(df_tarjetadebito["|Monto|"][0])
                    numtarjeta = str(df_tarjetadebito["|NumTarjeta|"][0])
                    contrasena = int(df_tarjetadebito["|Contrasena|"][0])

                    tarjetadebito = TarjetaDebito()

                    tarjetadebito.CrearMetodoPago(numoperacion, fechapago, monedapago,
                    cuentabeneficiario, monto)
                    tarjetadebito.CrearPago(numtarjeta, contrasena)   

            except FileNotFoundError:
                print("No se encontro el archivo") 

    return tarjetadebito, num