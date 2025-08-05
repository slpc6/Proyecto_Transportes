from pydantic import BaseModel
from typing import List

class RegistroEscoria(BaseModel):
    id: str
    fecha: str
    placa: str
    destino: str
    numViajes: int
    tipoVehiculo: str
    valorUnitario: float
    valorTotal: float

class DatosEscoriaEnvio(BaseModel):
    registros: List[RegistroEscoria]
    total: float 