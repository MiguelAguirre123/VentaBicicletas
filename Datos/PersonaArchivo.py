import pandas as pd
from Business.Persona import Persona

class PersonaArchivo:
    
    def GenerarTXT(self):
        pd.DataFrame(Persona).to_csv('Persona.csv') 