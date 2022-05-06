import pandas as pd

class BicicletaArchivo:
    
    def GenerarTXT(self, nombreBici, numVelocidades, material, identificacion, tipoBici, tamanoBici, valor, referencia, disenos):
        d = {"|NombreBici|":nombreBici,"|NumVelocidades|":numVelocidades, "|Material|":material, "|ID|":identificacion,
        "|Tipobici|":tipoBici, "|TamanoBici|":tamanoBici,"|Valor|":valor,}
        

        nombre_archivo = f'Datos/Archivos_Guardados/Bicicleta/{nombreBici}.csv'
        df = pd.DataFrame(data=d,index=[0])
        df_referencia = pd.read_csv(f'Datos/Archivos_Guardados/Referencia/{referencia}.csv')
        df = pd.merge(df, df_referencia, right_index=True, left_index=True, how='outer')

        for i in range(len(disenos)):
            df_diseno = pd.read_csv(f'Datos/Archivos_Guardados/Diseno/{disenos[i]}.csv')
            df_diseno = df_diseno.add_suffix(f'|{i+1}|')
            df = pd.merge(df, df_diseno, right_index=True, left_index=True, how='outer')

        print(df)
        df.to_csv(nombre_archivo, index=False) 