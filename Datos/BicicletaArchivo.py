from Business.Bicicleta import Bicicleta
<<<<<<< HEAD
from Business.Diseno import Diseno
=======
>>>>>>> 66bd4a2f57680edb34ac7e8af71d54b60e88daac
import pandas as pd

class BicicletaArchivo:
    
    def GenerarTXT(self, bicicleta:Bicicleta):
<<<<<<< HEAD

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
=======
        Datos_Bicicleta = {"|NombreBici|":bicicleta.NombreBici,"|NumVelocidades|":bicicleta.NumVelocidades,
        "|Material|":bicicleta.Material, "|ID|":bicicleta.Identificacion,
        "|Tipobici|":bicicleta.TipoBici, "|TamanoBici|":bicicleta.TamanoBici,"|Valor|":bicicleta.Valor}

        nombre_archivo = f'Datos/Archivos_Guardados/Bicicleta/{bicicleta.NombreBici}.csv'
        df = pd.DataFrame(data=Datos_Bicicleta,index=[0])

        try:

            if pd.read_csv(f'Datos/Archivos_Guardados/Referencia/{bicicleta.Referenciacion}.csv').empty == False:

                df_referencia = pd.read_csv(f'Datos/Archivos_Guardados/Referencia/{bicicleta.Referenciacion}.csv')
                df = pd.merge(df, df_referencia, right_index=True, left_index=True, how='outer')

        except OSError:

            df_referencia = pd.read_csv(f'Datos/Archivos_Guardados/Referencia/{bicicleta.Referenciacion._NombreReferencia}.csv')
            df = pd.merge(df, df_referencia, right_index=True, left_index=True, how='outer')

        for contador_disenos in range(len(bicicleta.Disenos)):

            try:

                if pd.read_csv(f'Datos/Archivos_Guardados/Diseno/{bicicleta.Disenos[contador_disenos]}.csv').empty == False:

                    df_diseno = pd.read_csv(f'Datos/Archivos_Guardados/Diseno/{bicicleta.Disenos[contador_disenos]}.csv')
                    df_diseno = df_diseno.add_suffix(f'|{contador_disenos+1}|')
                    df = pd.merge(df, df_diseno, right_index=True, left_index=True, how='outer')

            except OSError:

                df_diseno = pd.read_csv(f'Datos/Archivos_Guardados/Diseno/{bicicleta.Disenos[contador_disenos]._Id}.csv')
                df_diseno = df_diseno.add_suffix(f'|{contador_disenos+1}|')
                df = pd.merge(df, df_diseno, right_index=True, left_index=True, how='outer')                
>>>>>>> 66bd4a2f57680edb34ac7e8af71d54b60e88daac

        print(df)
        df.to_csv(nombre_archivo, index=False) 