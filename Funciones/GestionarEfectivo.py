from Business.Efectivo import Efectivo
from Funciones.GestionarMetodoPago import GestionarMetodoPago
import pandas as pd

def GestionarEfectivo():

    efectivo = None

    while efectivo == None:
        
        print("¿Que Quiere Hacer?")
        print("1. Crear un metodo de pago por efectivo")
        print("2. Buscar un metodo de pago por efectivo existente")
        num = int(input("Introduzca un numero: "))

        if num == 1:

            valores_metodopago = GestionarMetodoPago()

            valorpagar = int(input("Introduzca el valor a pagar en efectivo: "))
            
            efectivo = Efectivo()

            efectivo.CrearMetodoPago(valores_metodopago[0], valores_metodopago[1],
            valores_metodopago[2], valores_metodopago[3], valores_metodopago[4])
            efectivo.CrearPago(valorpagar)           

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")
            
            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/Efectivo/{nombre_archivo}.csv').empty == False:
                    
                    df_efectivo = pd.read_csv(f'Datos/Archivos_Guardados/Efectivo/{nombre_archivo}.csv')

                    numoperacion = str(df_efectivo["|NumOperacion|"][0])
                    fechapago = df_efectivo["|FechaPago|"][0]
                    monedapago = str(df_efectivo["|MonedaPago|"][0])
                    cuentabeneficiario = str(df_efectivo["|CuentaBeneficiario|"][0])
                    monto = str(df_efectivo["|Monto|"][0])
                    valorpagar = str(df_efectivo["|ValorPagar|"][0])

                    efectivo = Efectivo()

                    efectivo.CrearMetodoPago(numoperacion, fechapago, monedapago,
                    cuentabeneficiario, monto)
                    efectivo.CrearPago(valorpagar)  

            except FileNotFoundError:
                print("No se encontro el archivo")             
    
    return efectivo, num