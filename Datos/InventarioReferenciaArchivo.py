import pandas as pd
from Business.InventarioReferencia import InventarioReferencia

class InventarioReferenciaArchivo:
    
    def GenerarTXT(self):
        pd.DataFrame(InventarioReferencia).to_csv('InventarioReferencia.csv') 