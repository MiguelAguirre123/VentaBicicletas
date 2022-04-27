import pandas as pd
from Business.TarjetaCredito import TarjetaCredito

class TarjetaCreditoArchivo:
    
    def GenerarTXT(self):
        pd.DataFrame(TarjetaCredito).to_csv('TarjetaCredito.csv') 