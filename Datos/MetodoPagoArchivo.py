import pandas as pd
from Business.MetodoPago import MetodoPago

class MetodoPagoArchivo:
    
    def GenerarTXT(self):
        pd.DataFrame(MetodoPago).to_csv('MetodoPago.csv') 