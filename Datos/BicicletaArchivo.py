import pandas as pd
from Business.Bicicleta import Bicicleta

class BicicletaArchivo:
    
    def GenerarTXT(self):
        pd.DataFrame(Bicicleta).to_csv('Bicicleta.csv') 