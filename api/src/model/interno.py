"""Modelos para la tabla de internos"""

from typing import List
from pydantic import BaseModel


class RegistroInterno(BaseModel):
    """Clase que representa los registros para la tabla de internos"""
    id: str
    fecha: str
    placa: str
    numViajes: int
    tipoVehiculo: str
    valorUnitario: float
    valorTotal: float


class DatosInternoEnvio(BaseModel):
    """Clase que representa la tabla con los registros de internos"""
    registros: List[RegistroInterno]
    total: float
