"""Modelos para la tabla de ceniza"""

from typing import List
from pydantic import BaseModel


class RegistroCeniza(BaseModel):
    """Clase que representa los registros para la tabla de ceniza"""
    id: str
    fecha: str
    placa: str
    destino: str
    numViajes: int
    tipoVehiculo: str
    valorUnitario: float
    valorTotal: float

class DatosCenizaEnvio(BaseModel):
    """Clase qque representa la tabla con los registros de ceniza"""
    registros: List[RegistroCeniza]
    total: float
