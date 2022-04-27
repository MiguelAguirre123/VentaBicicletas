import pandas as pd
from Business.Sede import Sede

class SedeArchivo:
    
    def GenerarTXT(self):
        pd.DataFrame(Sede).to_csv('Sede.csv') 