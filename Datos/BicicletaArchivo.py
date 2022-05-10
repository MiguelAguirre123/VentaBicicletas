from Business.Bicicleta import Bicicleta
from Business.Diseno import Diseno
import pandas as pd

class BicicletaArchivo:
    
    def GenerarTXT(self, bicicleta:Bicicleta):

        datos_bicicleta = {"|NombreBici|":bicicleta.NombreBici, "|NumVelocidades|":bicicleta.NumVelocidades,
        "|Material|":bicicleta.Material, "|ID|":bicicleta.IdBicicleta,
        "|TipoBici|":bicicleta.TipoBici, "|TamanoBici|":bicicleta.TamanoBici,"|Valor|":bicicleta.Valor}

        nombre_archivo = f'Datos/Archivos_Guardados/Bicicleta/{bicicleta.NombreBici}.csv'
        df = pd.DataFrame(data=datos_bicicleta,index=[0])

        df_referencia = pd.read_csv(f'Datos/Archivos_Guardados/Referencia/{bicicleta.Referenciacion._NombreReferencia}.csv')
        df = pd.merge(df, df_referencia, right_index=True, left_index=True, how='outer')

        contador_disenos:Diseno

        for contador_disenos in bicicleta.Disenos:

            df_diseno = pd.read_csv(f'Datos/Archivos_Guardados/Diseno/{contador_disenos._IdDiseno}.csv')
            df_diseno = df_diseno.add_suffix(f'|{bicicleta.Disenos.index(contador_disenos)+1}|')
            df = pd.merge(df, df_diseno, right_index=True, left_index=True, how='outer')                

        print(df)
        df.to_csv(nombre_archivo, index=False) 