from Business.Diseno import Diseno
import pandas as pd

class DisenoArchivo:
    
    def GenerarTXT(self,diseno:Diseno):

        datos_diseno = {"|ID Diseno|":diseno._IdDiseno, "|Color 1|":diseno._Color1,"|Color 2|":diseno._Color2}

        nombre_archivo = f'Datos/Archivos_Guardados/Diseno/{diseno._IdDiseno}.csv'
        df = pd.DataFrame(data=datos_diseno,index=[0])
        
        print(df)
        df.to_csv(nombre_archivo, index=False) 