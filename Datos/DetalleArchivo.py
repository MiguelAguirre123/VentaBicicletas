import pandas as pd
from Business.Detalle import Detalle

class DetalleArchivo:
    
    def GenerarTXT(self):
        pd.DataFrame(Detalle).to_csv('Detalle.csv') 