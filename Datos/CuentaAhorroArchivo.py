from Business.CuentaAhorro import CuentaAhorro
import pandas as pd

class CuentaAhorroArchivo:
    
    def GenerarTXT(self,cuentaahorro:CuentaAhorro):

        datos_cuentaahorro = {"|NumOperacion|":cuentaahorro._NumOperacion, "|FechaPago|":cuentaahorro._FechaPago,
        "|MonedaPago|":cuentaahorro._MonedaPago, "|CuentaBeneficiario|":cuentaahorro._CuentaBeneficiario, "|Monto|":cuentaahorro._Monto,
        "|NumCuenta|":cuentaahorro.NumCuenta, "|Contrasena|":cuentaahorro.Contrasena}

        nombre_archivo = f'Datos/Archivos_Guardados/CuentaAhorro/{cuentaahorro._NumOperacion}.csv'
        df = pd.DataFrame(data=datos_cuentaahorro, index=[0])           

        print(df)
        df.to_csv(nombre_archivo, index=False) 