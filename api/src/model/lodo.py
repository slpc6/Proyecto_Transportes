"""Modelos para la tabla de internos"""

from typing import List
from pydantic import BaseModel


class RegistroLodo(BaseModel):
    """Clase que representa los registros para la tabla de lodo"""
    id: str
    fecha: str
    placa: str
    numViajes: int
    producto: str
    destino: str
    tipoVehiculo: str
    valorUnitario: int
    valorTotal: int


class DatosLodoEnvio(BaseModel):
    """Clase que representa la tabla con los registros de lodo"""
    registros: List[RegistroLodo]
    total: float
