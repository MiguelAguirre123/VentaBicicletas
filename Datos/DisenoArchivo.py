import pandas as pd

class DisenoArchivo:
    
    def GenerarTXT(self, color1, color2, id):
        d = {"|ID Diseno|":id, "|Color 1|":color1,"|Color 2|":color2}

        nombre_archivo = f'Datos/Archivos_Guardados/Diseno/{id}.csv'
        df = pd.DataFrame(data=d,index=[0])
        print(df)
        df.to_csv(nombre_archivo, index=False) 