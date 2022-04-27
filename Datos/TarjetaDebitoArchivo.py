import pandas as pd
from Business.TarjetaDebito import TarjetaDebito

class TarjetaDebitoArchivo:
    
    def GenerarTXT(self):
        pd.DataFrame(TarjetaDebito).to_csv('TarjetaDebito.csv') 