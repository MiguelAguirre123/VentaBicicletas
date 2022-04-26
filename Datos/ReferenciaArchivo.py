import pandas as pd
from Business.Referencia import Referencia

class ReferenciaArchivo:
    
    def GenerarTXT(self):
        pd.DataFrame(Referencia).to_csv('Referencia.csv') 