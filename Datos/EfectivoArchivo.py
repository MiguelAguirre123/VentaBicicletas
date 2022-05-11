from Business.Efectivo import Efectivo
import pandas as pd

class EfectivoArchivo:
    
    def GenerarTXT(self,efectivo:Efectivo):

        datos_efectivo = {"|NumOperacion|":efectivo._NumOperacion, "|FechaPago|":efectivo._FechaPago,
        "|MonedaPago|":efectivo._MonedaPago, "|CuentaBeneficiario|":efectivo._CuentaBeneficiario, "|Monto|":efectivo._Monto,
        "|ValorPagar|":efectivo.ValorPagar}

        nombre_archivo = f'Datos/Archivos_Guardados/Efectivo/{efectivo._NumOperacion}.csv'
        df = pd.DataFrame(data=datos_efectivo, index=[0])           

        print(df)
        df.to_csv(nombre_archivo, index=False) 