from Business.Persona import Persona
import pandas as pd

class PersonaArchivo:
    
    def GenerarTXT(self, persona:Persona):
        datos_persona = {"|Nombre|":persona.Nombre, "|Apellido|":persona.Apellido,
        "|ID Persona|":persona.IdPersona, "|Telefono|":persona.Telefono, "|Direccion|":persona.Direccion}

        nombre_archivo = f'Datos/Archivos_Guardados/Persona/{persona.IdPersona}.csv'
        df = pd.DataFrame(data=datos_persona, index=[0])

        print(df)
        df.to_csv(nombre_archivo, index=False) 