from Business.Referencia import Referencia
import pandas as pd

class ReferenciaArchivo:
    
    def GenerarTXT(self, referencia:Referencia):
        
        datos_referencia = {"|Nombre Referencia|":referencia._NombreReferencia}

        nombre_archivo = f'Datos/Archivos_Guardados/Referencia/{referencia._NombreReferencia}.csv'
        df = pd.DataFrame(data=datos_referencia,index=[0])
        print(df)
        df.to_csv(nombre_archivo, index=False)