"""EndPoint para generar el archivo para transportes de escoria"""

from datetime import datetime
from fastapi import APIRouter, HTTPException
import pandas as pd

from model.escoria import DatosEscoriaEnvio
from util.titulo import generar_titulo
from util.generar_archivo import generar_archivo


router = APIRouter()


@router.post("/escoria")
def escoria(request: DatosEscoriaEnvio) -> dict:
    """Tabla para los transportes de escoria.
    :args:
    - request: Ver model/escoria.
    :returns:
    - Diccionario con la informacion del documento generado.
    
    """
    try:
        nuevos_datos = [{
                'Fecha': registro.fecha,
                'Placa': registro.placa,
                'Destino': registro.destino,
                '# de Viajes': registro.numViajes,
                'Tipo de Vehículo': registro.tipoVehiculo,
                'Valor Unitario': registro.valorUnitario,
                'Valor Total': registro.valorTotal
            } for registro in request.registros]
        
        datos = pd.DataFrame(nuevos_datos)
        titulo: str = generar_titulo('escoria')
        headers: list(str) = ['Fecha',
                                'Placa',
                                'Destino',
                                '# de Viajes',
                                'Tipo de Vehículo',
                                'Valor Unitario',
                                'Valor Total']
        total_valor = generar_archivo(datos, titulo, headers, 'ESCORIA')

        return {
            "success": True,
            "message": "Archivo guardado exitosamente",
            "registros_procesados": len(request.registros),
            "total": request.total,
            "fecha_procesamiento": datetime.now().isoformat(),
            "titulo_generado": titulo,
            "total_calculado": float(total_valor)
        }

    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=f"Error al procesar los datos: {str(e)}") from e
