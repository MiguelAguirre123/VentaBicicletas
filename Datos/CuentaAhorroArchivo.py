import pandas as pd
from Business.CuentaAhorro import CuentaAhorro

class CuentaAhorroArchivo:
    
    def GenerarTXT(self):
        pd.DataFrame(CuentaAhorro).to_csv('CuentaAhorro.csv') 