from Business.Referencia import Referencia
import pandas as pd

class ReferenciaArchivo:
    
    def GenerarTXT(self, referencia:Referencia):
<<<<<<< HEAD
        
        datos_referencia = {"|Nombre Referencia|":referencia._NombreReferencia}

        nombre_archivo = f'Datos/Archivos_Guardados/Referencia/{referencia._NombreReferencia}.csv'
        df = pd.DataFrame(data=datos_referencia,index=[0])
=======
        Datos_Referencia = {"|Nombre Referencia|":referencia._NombreReferencia}

        nombre_archivo = f'Datos/Archivos_Guardados/Referencia/{referencia._NombreReferencia}.csv'
        df = pd.DataFrame(data=Datos_Referencia,index=[0])
>>>>>>> 66bd4a2f57680edb34ac7e8af71d54b60e88daac
        print(df)
        df.to_csv(nombre_archivo, index=False)