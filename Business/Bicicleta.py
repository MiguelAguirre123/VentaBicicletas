from EnumMaterial import EnumMaterial
from EnumTipoBici import EnumTipoBici

class Bicicleta:

    NombreBici:str
    NumVelocidades:int
    Material:EnumMaterial
    Identificacion:str
    TipoBici:EnumTipoBic
    TamanoBici:str
    Valor:int


    def __init__(self, referencia, disenos[]):

        self.Relacion = referencia
        self.Disenos = disenos