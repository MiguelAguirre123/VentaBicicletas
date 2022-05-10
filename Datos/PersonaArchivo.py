import pandas as pd

class PersonaArchivo:
    
    def GenerarTXT(self, nombre, apellido, id, telefono, direccion):
        d = {"|Nombre|":pd.Series(nombre,index=[1]), "|Apellido|":pd.Series(apellido,index=[1]),
        "|ID|":id, "|Telefono|":pd.Series(telefono,index=list(range(len(telefono)+1))),
        "|Direccion|":pd.Series(direccion,index=[1])}

        nombre_archivo = f'Datos/Archivos_Guardados/Persona/{nombre} {apellido}.csv'
        df = pd.DataFrame(data=d,index=range(len(telefono)+1))
        df.to_csv(nombre_archivo, index=False) 