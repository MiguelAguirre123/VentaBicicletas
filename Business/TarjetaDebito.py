from Business.MetodoPago import MetodoPago
import pandas as pd

class TarjetaDebito(MetodoPago):

    NumTarjeta:str
    Contrasena:int

    def CrearTarjetaDebito(self):

        tarjetadebito= None

        while tarjetadebito == None:
            
            print("¿Que Quiere Hacer?")
            print("1. Crear un metodo de pago por tarjeta de credito")
            print("2. Buscar un metodo de pago por tarjeta de credito existente")
            num = int(input("Introduzca un numero: "))

            if num == 1:

                tarjetadebito = TarjetaDebito()

                tarjetadebito.CrearMetodoPago()

                tarjetadebito.NumTarjeta = input("Introduzca el numero de la tarjeta debito: ")
                tarjetadebito.Contrasena = int(input("Introduzca la contrasena de la tarjeta debito: "))

            elif num == 2:

                nombre_archivo = input("Introduzca el nombre del archivo: ")
                
                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/TarjetaDebito/{nombre_archivo}.csv').empty == False:
                        
                        df_tarjetadebito = pd.read_csv(f'Datos/Archivos_Guardados/TarjetaDebito/{nombre_archivo}.csv')

                        tarjetadebito = TarjetaDebito()

                        tarjetadebito._NumOperacion = str(df_tarjetadebito["|NumOperacion|"][0])
                        tarjetadebito._FechaPago = df_tarjetadebito["|FechaPago|"][0]
                        tarjetadebito._MonedaPago = str(df_tarjetadebito["|MonedaPago|"][0])
                        tarjetadebito._CuentaBeneficiario = str(df_tarjetadebito["|CuentaBeneficiario|"][0])
                        tarjetadebito._Monto = str(df_tarjetadebito["|Monto|"][0])
                        tarjetadebito.NumTarjeta = str(df_tarjetadebito["|NumTarjeta|"][0])
                        tarjetadebito.Contrasena = int(df_tarjetadebito["|Contrasena|"][0])
   
                except FileNotFoundError:
                    print("No se encontro el archivo") 

        return tarjetadebito, num