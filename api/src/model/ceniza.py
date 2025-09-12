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

class RegistroCenizaSubtabla(BaseModel):
    id: str
    fecha: str
    placa: str
    material: str
    numViajes: int
    tipoVehiculo: str
    destino: str
    valorUnitario: float
    valorTotal: float

class DatosCenizaEnvio(BaseModel):
    registros: List[RegistroCeniza]
    registrosSubtabla: List[RegistroCenizaSubtabla]
    total: float
    totalSubtabla: float 