from Business.Referencia import Referencia
import pandas as pd

class ReferenciaArchivo:
    
    def GenerarTXT(self, referencia:Referencia):
        Datos_Referencia = {"|Nombre Referencia|":referencia._NombreReferencia}

        nombre_archivo = f'Datos/Archivos_Guardados/Referencia/{referencia._NombreReferencia}.csv'
        df = pd.DataFrame(data=Datos_Referencia,index=[0])
        print(df)
        df.to_csv(nombre_archivo, index=False)