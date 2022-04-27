import pandas as pd
from Business.Diseno import Diseno

class DisenoArchivo:
    
    def GenerarTXT(self):
        pd.DataFrame(Diseno).to_csv('Diseno.csv') 