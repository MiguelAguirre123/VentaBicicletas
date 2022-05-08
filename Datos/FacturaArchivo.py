import pandas as pd
from Business.Factura import Factura

class FacturaArchivo:
    
    def GenerarTXT(self):
        pd.DataFrame(Factura).to_csv('Factura.csv') 