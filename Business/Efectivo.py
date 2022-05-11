from Business.MetodoPago import MetodoPago
import pandas as pd

class Efectivo(MetodoPago):

    ValorPagar:int

    def CrearEfectivo(self):

        efectivo = None

        while efectivo == None:
            
            print("¿Que Quiere Hacer?")
            print("1. Crear un metodo de pago por efectivo")
            print("2. Buscar un metodo de pago por efectivo existente")
            num = int(input("Introduzca un numero: "))

            if num == 1:

                efectivo = Efectivo()

                efectivo.CrearMetodoPago()

                efectivo.ValorPagar = int(input("Introduzca el valor a pagar en efectivo: "))

            elif num == 2:

                nombre_archivo = input("Introduzca el nombre del archivo: ")
                
                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/Efectivo/{nombre_archivo}.csv').empty == False:
                        
                        df_efectivo = pd.read_csv(f'Datos/Archivos_Guardados/Efectivo/{nombre_archivo}.csv')

                        efectivo = Efectivo()

                        efectivo._NumOperacion = str(df_efectivo["|NumOperacion|"][0])
                        efectivo._FechaPago = df_efectivo["|FechaPago|"][0]
                        efectivo._MonedaPago = str(df_efectivo["|MonedaPago|"][0])
                        efectivo._CuentaBeneficiario = str(df_efectivo["|CuentaBeneficiario|"][0])
                        efectivo._Monto = str(df_efectivo["|Monto|"][0])
                        efectivo.ValorPagar = str(df_efectivo["|ValorPagar|"][0])
   
                except FileNotFoundError:
                    print("No se encontro el archivo")             
        
        return efectivo, num