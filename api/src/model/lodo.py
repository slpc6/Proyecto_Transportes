from pydantic import BaseModel
from typing import List

class RegistroLodo(BaseModel):
    id: str
    Fecha: str
    Placa: str
    numViajes: int	
    Producto: str	
    Destino: str	
    TipoVehiculo: str
    ValorUnitario: int
    ValorTotal: int

class DatosLodoEnvio(BaseModel):
    registros: List[RegistroLodo]
    total: float 
    