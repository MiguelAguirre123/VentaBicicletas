from Business.TarjetaCredito import TarjetaCredito
import pandas as pd

class TarjetaCreditoArchivo:
    
    def GenerarTXT(self, tarjetacredito:TarjetaCredito):

        datos_tarjetacredito = {"|NumOperacion|":tarjetacredito._NumOperacion, "|FechaPago|":tarjetacredito._FechaPago,
        "|MonedaPago|":tarjetacredito._MonedaPago, "|CuentaBeneficiario|":tarjetacredito._CuentaBeneficiario, "|Monto|":tarjetacredito._Monto,
        "|NumTarjeta|":tarjetacredito.NumTarjeta, "|Contrasena|":tarjetacredito.Contrasena}

        nombre_archivo = f'Datos/Archivos_Guardados/TarjetaCredito/{tarjetacredito._NumOperacion}.csv'
        df = pd.DataFrame(data=datos_tarjetacredito, index=[0])           

        print(df)
        df.to_csv(nombre_archivo, index=False) 