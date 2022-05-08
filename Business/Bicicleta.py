from Business.Referencia import Referencia
from Business.Diseno import Diseno
from Business.EnumMaterial import EnumMaterial
from Business.EnumTipoBici import EnumTipoBici

class Bicicleta:

    NombreBici:str
    NumVelocidades:int
    Material:EnumMaterial
    Identificacion:str
    TipoBici:EnumTipoBici
    TamanoBici:str
    Valor:int

    def __init__(self, referencia:Referencia, disenos:Diseno):

        self.Referenciacion = referencia
        self.Disenos = disenos