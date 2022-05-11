from Business.MetodoPago import MetodoPago
import pandas as pd

class CuentaAhorro(MetodoPago):

    NumCuenta:str
    Contrasena:int

    def CrearCuentaAhorro(self):

        cuentaahorro = None

        while cuentaahorro == None:
            
            print("¿Que Quiere Hacer?")
            print("1. Crear un metodo de pago por cuenta de ahorro")
            print("2. Buscar un metodo de pago por cuenta de ahorro existente")
            num = int(input("Introduzca un numero: "))

            if num == 1:

                cuentaahorro = CuentaAhorro()

                cuentaahorro.CrearMetodoPago()

                cuentaahorro.NumCuenta = input("Introduzca la cuenta de ahorro: ")
                cuentaahorro.Contrasena = int(input("Introduzca la contrasena de la cuenta de ahorro: "))

            elif num == 2:

                nombre_archivo = input("Introduzca el nombre del archivo: ")
                
                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/CuentaAhorro/{nombre_archivo}.csv').empty == False:
                        
                        df_cuentaahorro = pd.read_csv(f'Datos/Archivos_Guardados/CuentaAhorro/{nombre_archivo}.csv')

                        cuentaahorro = CuentaAhorro()

                        cuentaahorro._NumOperacion = str(df_cuentaahorro["|NumOperacion|"][0])
                        cuentaahorro._FechaPago = df_cuentaahorro["|FechaPago|"][0]
                        cuentaahorro._MonedaPago = str(df_cuentaahorro["|MonedaPago|"][0])
                        cuentaahorro._CuentaBeneficiario = str(df_cuentaahorro["|CuentaBeneficiario|"][0])
                        cuentaahorro._Monto = str(df_cuentaahorro["|Monto|"][0])
                        cuentaahorro.NumCuenta = str(df_cuentaahorro["|NumCuenta|"][0])
                        cuentaahorro.Contrasena = int(df_cuentaahorro["|Contrasena|"][0])
   
                except FileNotFoundError:
                    print("No se encontro el archivo")             
        
        return cuentaahorro, num