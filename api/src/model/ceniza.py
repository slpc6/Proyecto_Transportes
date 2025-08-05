from pydantic import BaseModel
from typing import List

class RegistroCeniza(BaseModel):
    id: str
    fecha: str
    placa: str
    destino: str
    numViajes: int
    tipoVehiculo: str
    valorUnitario: float
    valorTotal: float

class DatosCenizaEnvio(BaseModel):
    registros: List[RegistroCeniza]
    total: float 