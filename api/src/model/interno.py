from pydantic import BaseModel
from typing import List

class RegistroInterno(BaseModel):
    id: str
    fecha: str
    placa: str
    numViajes: int
    tipoVehiculo: str
    valorUnitario: float
    valorTotal: float

class DatosInternoEnvio(BaseModel):
    registros: List[RegistroInterno]
    total: float 