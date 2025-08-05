from fastapi import APIRouter, HTTPException
from datetime import datetime
import pandas as pd

from model.interno import DatosInternoEnvio
from util.titulo import generar_titulo
from util.generar_archivo import generar_archivo

router = APIRouter()


@router.post("/interno")
def interno(request: DatosInternoEnvio):
    try:

        nuevos_datos = [{
            'Fecha': registro.fecha,
            'Placa': registro.placa,
            '# de Viajes': registro.numViajes,
            'Tipo de Vehículo': registro.tipoVehiculo,
            'Valor Unitario': registro.valorUnitario,
            'Valor Total': registro.valorTotal
        } for registro in request.registros]

        
        df_final = pd.DataFrame(nuevos_datos)
        titulo = generar_titulo('interno')
        headers = ['Fecha', 'Placa', '# de Viajes', 'Tipo de Vehículo', 'Valor Unitario', 'Valor Total']

        total_valor = generar_archivo(df_final, titulo, headers)
        
        return {
            "success": True,
            "message": f"Archivo guardado exitosamente",
            "registros_procesados": len(request.registros),
            "total": request.total,
            "fecha_procesamiento": datetime.now().isoformat(),
            "titulo_generado": titulo,
            "total_calculado": float(total_valor)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar los datos: {str(e)}")
