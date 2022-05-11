from Business.TarjetaDebito import TarjetaDebito
import pandas as pd

class TarjetaDebitoArchivo:
    
    def GenerarTXT(self, tarjetadebito:TarjetaDebito):

        datos_tarjetadebito = {"|NumOperacion|":tarjetadebito._NumOperacion, "|FechaPago|":tarjetadebito._FechaPago,
        "|MonedaPago|":tarjetadebito._MonedaPago, "|CuentaBeneficiario|":tarjetadebito._CuentaBeneficiario, "|Monto|":tarjetadebito._Monto,
        "|NumTarjeta|":tarjetadebito.NumTarjeta, "|Contrasena|":tarjetadebito.Contrasena}

        nombre_archivo = f'Datos/Archivos_Guardados/TarjetaDebito/{tarjetadebito._NumOperacion}.csv'
        df = pd.DataFrame(data=datos_tarjetadebito, index=[0])           

        print(df)
        df.to_csv(nombre_archivo, index=False)  