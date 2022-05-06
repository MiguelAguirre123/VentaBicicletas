import pandas as pd

class ReferenciaArchivo:
    
    def GenerarTXT(self, nombrereferencia):
        d = {"|Nombre Referencia|":nombrereferencia}

        nombre_archivo = f'Datos/Archivos_Guardados/Referencia/{nombrereferencia}.csv'
        df = pd.DataFrame(data=d,index=[0])
        print(df)
        df.to_csv(nombre_archivo, index=False)