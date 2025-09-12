from fastapi import APIRouter, HTTPException
import pandas as pd
import os
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from openpyxl.utils.dataframe import dataframe_to_rows

from model.ceniza import DatosCenizaEnvio
from util.path import Path
from util.titulo import generar_titulo
from util.generar_archivo import generar_archivo_multiple_hojas

router = APIRouter()


@router.post("/ceniza")
def ceniza(request: DatosCenizaEnvio):
    try:
        # Procesar datos de la tabla principal
        nuevos_datos = []
        for registro in request.registros:
            nuevos_datos.append({
                'Fecha': registro.fecha,
                'Placa': registro.placa,
                'Destino': registro.destino,
                '# de Viajes': registro.numViajes,
                'Tipo de Vehículo': registro.tipoVehiculo,
                'Valor Unitario': registro.valorUnitario,
                'Valor Total': registro.valorTotal
            })
        
        df_principal = pd.DataFrame(nuevos_datos)
        
        # Procesar datos de la sub-tabla
        nuevos_datos_subtabla = []
        for registro in request.registrosSubtabla:
            nuevos_datos_subtabla.append({
                'Fecha': registro.fecha,
                'Placa': registro.placa,
                'Material': registro.material,
                '# de Viajes': registro.numViajes,
                'Tipo de Vehículo': registro.tipoVehiculo,
                'Destino': registro.destino,
                'Valor Unitario': registro.valorUnitario,
                'Valor Total': registro.valorTotal
            })
        
        df_subtabla = pd.DataFrame(nuevos_datos_subtabla)
        
        # Generar títulos
        titulo_principal = generar_titulo('ceniza')
        titulo_subtabla = generar_titulo('ceniza') + " - Sub-tabla"
        
        # Headers
        headers_principal = ['Fecha', 'Placa', 'Destino', '# de Viajes', 'Tipo de Vehículo', 'Valor Unitario', 'Valor Total']
        headers_subtabla = ['Fecha', 'Placa', 'Material', '# de Viajes', 'Tipo de Vehículo', 'Destino', 'Valor Unitario', 'Valor Total']

        # Generar archivo con múltiples hojas
        total_principal, total_subtabla = generar_archivo_multiple_hojas(
            df_principal, df_subtabla, 
            titulo_principal, titulo_subtabla,
            headers_principal, headers_subtabla, 
            'CENIZA'
        )
        
        return {
            "success": True,
            "message": f"Archivo guardado exitosamente con dos hojas",
            "registros_procesados": len(request.registros),
            "registros_subtabla_procesados": len(request.registrosSubtabla),
            "total_principal": request.total,
            "total_subtabla": request.totalSubtabla,
            "fecha_procesamiento": datetime.now().isoformat(),
            "titulo_generado": titulo_principal,
            "total_calculado_principal": float(total_principal),
            "total_calculado_subtabla": float(total_subtabla)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar los datos: {str(e)}")
    