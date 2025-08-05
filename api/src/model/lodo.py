from pydantic import BaseModel
from typing import List

class RegistroLodo(BaseModel):
    id: str
    Fecha: str
    Placa: str
    numViajes: str	
    Producto: str	
    Destino: str	
    TipoVehiculo: str
    ValorUnitario: str
    ValorTotal: str

class DatosLodoEnvio(BaseModel):
    registros: List[RegistroLodo]
    total: float 
    