from pydantic import BaseModel
from typing import List

class RegistroLodo(BaseModel):
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
    registros: List[RegistroLodo]
    total: float 
    