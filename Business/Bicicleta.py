from enum import Enum

class Bicicleta:

    NombreBici:str
    NumVelocidades:int
    Material:Enum
    Identificacion:str
    TipoBici:Enum
    TamanoBici:str
    Valor:int

    def __init__(self, referencia, disenos):

        self.Relacion = referencia
        self.Disenos = disenos