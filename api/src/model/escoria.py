"""Modelos para la tabla de escoria"""

from typing import List
from pydantic import BaseModel


class RegistroEscoria(BaseModel):
    """Clase que representa los registros para la tabla de escoria"""
    id: str
    fecha: str
    placa: str
    destino: str
    numViajes: int
    tipoVehiculo: str
    valorUnitario: float
    valorTotal: float


class DatosEscoriaEnvio(BaseModel):
    """Clase que representa la tabla con los registros de escoria"""
    registros: List[RegistroEscoria]
    total: float
