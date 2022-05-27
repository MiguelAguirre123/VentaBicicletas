from Business.Empleado import Empleado
from Business.InventarioReferencia import InventarioReferencia

class Sede:

    Nombre:str
    Direccion:str
    Ciudad:str
    IdSede:str

    def __init__(self, inventariosede:InventarioReferencia, empleados:Empleado):

        self.InventarioSede = inventariosede
        self.Empleados = empleados

    def CrearSede(self, nombre:str, direccion:str, ciudad:str, idsede:str):

        self.Nombre = nombre
        self.Direccion = direccion
        self.Ciudad = ciudad
        self.IdSede = idsede