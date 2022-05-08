from Business.Bicicleta import Bicicleta
import pandas as pd

class BicicletaArchivo:
    
    def GenerarTXT(self, bicicleta:Bicicleta):
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

        print(df)
        df.to_csv(nombre_archivo, index=False) 