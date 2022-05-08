import pandas as pd
from Business.Efectivo import Efectivo

class EfectivoArchivo:
    
    def GenerarTXT(self):
        pd.DataFrame(Efectivo).to_csv('Efectivo.csv') 