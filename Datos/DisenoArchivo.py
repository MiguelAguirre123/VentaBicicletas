from Business.Diseno import Diseno
import pandas as pd

class DisenoArchivo:
    
    def GenerarTXT(self,diseno:Diseno):
        Datos_Diseno = {"|ID Diseno|":diseno._Id, "|Color 1|":diseno._Color1,"|Color 2|":diseno._Color2}

        nombre_archivo = f'Datos/Archivos_Guardados/Diseno/{diseno._Id}.csv'
        df = pd.DataFrame(data=Datos_Diseno,index=[0])
        print(df)
        df.to_csv(nombre_archivo, index=False) 