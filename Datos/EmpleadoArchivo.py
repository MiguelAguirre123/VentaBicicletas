import pandas as pd
from Business.Empleado import Empleado

class EmpleadoArchivo:
    
    def GenerarTXT(self):
        pd.DataFrame(Empleado).to_csv('Empleado.csv') 