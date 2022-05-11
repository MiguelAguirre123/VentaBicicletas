from Business.MetodoPago import MetodoPago
import pandas as pd

class TarjetaCredito(MetodoPago):

    NumTarjeta:str
    Contrasena:int

    def CrearTarjetaCredito(self):

        tarjetacredito= None

        while tarjetacredito == None:
            
            print("¿Que Quiere Hacer?")
            print("1. Crear un metodo de pago por tarjeta de credito")
            print("2. Buscar un metodo de pago por tarjeta de credito existente")
            num = int(input("Introduzca un numero: "))

            if num == 1:

                tarjetacredito = TarjetaCredito()

                tarjetacredito.CrearMetodoPago()

                tarjetacredito.NumTarjeta = input("Introduzca el numero de la tarjeta credito: ")
                tarjetacredito.Contrasena = int(input("Introduzca la contrasena de la tarjeta credito: "))

            elif num == 2:

                nombre_archivo = input("Introduzca el nombre del archivo: ")
                
                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/TarjetaCredito/{nombre_archivo}.csv').empty == False:
                        
                        df_tarjetacredito = pd.read_csv(f'Datos/Archivos_Guardados/TarjetaCredito/{nombre_archivo}.csv')

                        tarjetacredito = TarjetaCredito()

                        tarjetacredito._NumOperacion = str(df_tarjetacredito["|NumOperacion|"][0])
                        tarjetacredito._FechaPago = df_tarjetacredito["|FechaPago|"][0]
                        tarjetacredito._MonedaPago = str(df_tarjetacredito["|MonedaPago|"][0])
                        tarjetacredito._CuentaBeneficiario = str(df_tarjetacredito["|CuentaBeneficiario|"][0])
                        tarjetacredito._Monto = str(df_tarjetacredito["|Monto|"][0])
                        tarjetacredito.NumTarjeta = str(df_tarjetacredito["|NumTarjeta|"][0])
                        tarjetacredito.Contrasena = int(df_tarjetacredito["|Contrasena|"][0])
   
                except FileNotFoundError:
                    print("No se encontro el archivo")             
        
        return tarjetacredito, num

