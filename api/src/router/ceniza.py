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

router = APIRouter()


@router.post("/ceniza")
def ceniza(request: DatosCenizaEnvio):
    try:
        output_file = os.path.join(Path.OUTPUT, "CENIZA.xlsx")
        os.makedirs(Path.OUTPUT, exist_ok=True)
        
        
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
        
        df_final = pd.DataFrame(nuevos_datos)

        titulo = generar_titulo('ceniza')
        
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"
        
        ws['A1'] = titulo
        ws.merge_cells('A1:G1')
        titulo_cell = ws['A1']
        titulo_cell.font = Font(bold=True, size=14)
        titulo_cell.alignment = Alignment(horizontal='center')
        
        # Escribir encabezados en la segunda fila
        headers = ['Fecha', 'Placa', 'Destino', '# de Viajes', 'Tipo de Vehículo', 'Valor Unitario', 'Valor Total']
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=2, column=col, value=header)
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal='center')
        
        # Escribir datos desde la tercera fila
        for row_idx, row in enumerate(dataframe_to_rows(df_final, index=False, header=False), 3):
            for col_idx, value in enumerate(row, 1):
                cell = ws.cell(row=row_idx, column=col_idx, value=value)
                
                # Formatear columnas de moneda (Valor Unitario y Valor Total)
                if col_idx == 6:  # Valor Unitario
                    cell.number_format = '"$"#,##0.00'
                elif col_idx == 7:  # Valor Total
                    cell.number_format = '"$"#,##0.00'
        
        # Calcular y agregar el total al final
        total_fila = len(df_final) + 3  # Fila después de los datos
        
        # Escribir "TOTAL" en la columna E (Tipo de Vehículo)
        ws.cell(row=total_fila, column=5, value="TOTAL").font = Font(bold=True)
        
        # Calcular y escribir el total en la columna G (Valor Total)
        total_valor = df_final['Valor Total'].sum()
        total_cell = ws.cell(row=total_fila, column=7, value=total_valor)
        total_cell.font = Font(bold=True)
        total_cell.number_format = '"$"#,##0.00'
        
        # Ajustar ancho de columnas de manera segura
        column_widths = {
            'A': 12,  # Fecha
            'B': 10,  # Placa
            'C': 20,  # Destino
            'D': 12,  # # de Viajes
            'E': 20,  # Tipo de Vehículo
            'F': 15,  # Valor Unitario
            'G': 15   # Valor Total
        }
        
        for column_letter, width in column_widths.items():
            ws.column_dimensions[column_letter].width = width
        
        # Guardar el archivo
        wb.save(output_file)
        
        return {
            "success": True,
            "message": f"Archivo guardado exitosamente en {output_file}",
            "registros_procesados": len(request.registros),
            "total": request.total,
            "fecha_procesamiento": datetime.now().isoformat(),
            "titulo_generado": titulo,
            "total_calculado": float(total_valor)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar los datos: {str(e)}")
    