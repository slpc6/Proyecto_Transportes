from fastapi import APIRouter, HTTPException
import pandas as pd
from datetime import datetime


from model.lodo import DatosLodoEnvio
from util.titulo import generar_titulo
from util.generar_archivo import generar_archivo

router = APIRouter()

@router.post('/lodo')
def lodo(request: DatosLodoEnvio):
    try:
        nuevos_datos = []

        for registro in request.registros:
            nuevos_datos.append({
                'Fecha': registro.fecha,
                'Placa': registro.placa,
                'Destino': registro.destino,
                'Producto': registro.producto,
                '# de Viajes': registro.numViajes,
                'Tipo de Vehículo': registro.tipoVehiculo,
                'Valor Unitario': registro.valorUnitario,
                'Valor Total': registro.valorTotal
            })
        df_final = pd.DataFrame(nuevos_datos)
        titulo = generar_titulo('ceniza')
        headers = ['Fecha', 'Placa', 'Destino', '# de Viajes', 'Tipo de Vehículo', 'Valor Unitario', 'Valor Total']

        total_valor = generar_archivo(df_final,titulo, headers, 'LODO')
        
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
    