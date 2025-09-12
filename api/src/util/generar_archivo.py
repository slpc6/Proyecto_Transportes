from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from openpyxl.utils.dataframe import dataframe_to_rows
from pandas import DataFrame
import os

from util.path import Path

def generar_archivo(df_final: DataFrame, titulo: str, headers: list[str], nombre: str = 'ARCHIVO')-> int:
    output_file = os.path.join(Path.OUTPUT, f"{nombre}.xlsx")
    os.makedirs(Path.OUTPUT, exist_ok=True)

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
        
    ws['A1'] = titulo
    ws.merge_cells('A1:G1')
    titulo_cell = ws['A1']
    titulo_cell.font = Font(bold=True, size=14)
    titulo_cell.alignment = Alignment(horizontal='center')

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=2, column=col, value=header)
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal='center')
        
    # Escribir datos desde la tercera fila
    for row_idx, row in enumerate(dataframe_to_rows(df_final, index=False, header=False), 3):
        for col_idx, value in enumerate(row, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            if col_idx == 6:  # Valor Unitario
                cell.number_format = '"$"#,##0.00'
            elif col_idx == 7:  # Valor Total
                cell.number_format = '"$"#,##0.00'
        
        
    total_fila = len(df_final) + 3
        
       
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
     
    return total_valor

def generar_archivo_multiple_hojas(df_principal: DataFrame, df_subtabla: DataFrame, 
                                  titulo_principal: str, titulo_subtabla: str,
                                  headers_principal: list[str], headers_subtabla: list[str], 
                                  nombre: str = 'ARCHIVO') -> tuple[float, float]:
    """
    Genera un archivo Excel con dos hojas: una principal y una sub-tabla
    """
    output_file = os.path.join(Path.OUTPUT, f"{nombre}.xlsx")
    os.makedirs(Path.OUTPUT, exist_ok=True)

    wb = Workbook()
    
    # Hoja principal (Sheet1)
    ws_principal = wb.active
    ws_principal.title = "Sheet1"
    
    # Configurar hoja principal
    ws_principal['A1'] = titulo_principal
    ws_principal.merge_cells('A1:G1')
    titulo_cell = ws_principal['A1']
    titulo_cell.font = Font(bold=True, size=14)
    titulo_cell.alignment = Alignment(horizontal='center')

    for col, header in enumerate(headers_principal, 1):
        cell = ws_principal.cell(row=2, column=col, value=header)
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal='center')
        
    # Escribir datos de la hoja principal
    for row_idx, row in enumerate(dataframe_to_rows(df_principal, index=False, header=False), 3):
        for col_idx, value in enumerate(row, 1):
            cell = ws_principal.cell(row=row_idx, column=col_idx, value=value)
            if col_idx == 6:  # Valor Unitario
                cell.number_format = '"$"#,##0.00'
            elif col_idx == 7:  # Valor Total
                cell.number_format = '"$"#,##0.00'
        
    total_fila_principal = len(df_principal) + 3
    ws_principal.cell(row=total_fila_principal, column=5, value="TOTAL").font = Font(bold=True)
    
    total_valor_principal = df_principal['Valor Total'].sum()
    total_cell_principal = ws_principal.cell(row=total_fila_principal, column=7, value=total_valor_principal)
    total_cell_principal.font = Font(bold=True)
    total_cell_principal.number_format = '"$"#,##0.00'
    
    # Ajustar ancho de columnas de la hoja principal
    column_widths_principal = {
        'A': 12,  # Fecha
        'B': 10,  # Placa
        'C': 20,  # Destino
        'D': 12,  # # de Viajes
        'E': 20,  # Tipo de Vehículo
        'F': 15,  # Valor Unitario
        'G': 15   # Valor Total
    }
    
    for column_letter, width in column_widths_principal.items():
        ws_principal.column_dimensions[column_letter].width = width

    # Hoja sub-tabla (Sheet2)
    ws_subtabla = wb.create_sheet("Sheet2")
    
    # Configurar hoja sub-tabla
    ws_subtabla['A1'] = titulo_subtabla
    ws_subtabla.merge_cells('A1:H1')
    titulo_cell_subtabla = ws_subtabla['A1']
    titulo_cell_subtabla.font = Font(bold=True, size=14)
    titulo_cell_subtabla.alignment = Alignment(horizontal='center')

    for col, header in enumerate(headers_subtabla, 1):
        cell = ws_subtabla.cell(row=2, column=col, value=header)
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal='center')
        
    # Escribir datos de la sub-tabla
    for row_idx, row in enumerate(dataframe_to_rows(df_subtabla, index=False, header=False), 3):
        for col_idx, value in enumerate(row, 1):
            cell = ws_subtabla.cell(row=row_idx, column=col_idx, value=value)
            if col_idx == 7:  # Valor Unitario
                cell.number_format = '"$"#,##0.00'
            elif col_idx == 8:  # Valor Total
                cell.number_format = '"$"#,##0.00'
        
    total_fila_subtabla = len(df_subtabla) + 3
    ws_subtabla.cell(row=total_fila_subtabla, column=6, value="TOTAL").font = Font(bold=True)
    
    total_valor_subtabla = df_subtabla['Valor Total'].sum()
    total_cell_subtabla = ws_subtabla.cell(row=total_fila_subtabla, column=8, value=total_valor_subtabla)
    total_cell_subtabla.font = Font(bold=True)
    total_cell_subtabla.number_format = '"$"#,##0.00'
    
    # Ajustar ancho de columnas de la sub-tabla
    column_widths_subtabla = {
        'A': 12,  # Fecha
        'B': 10,  # Placa
        'C': 15,  # Material (para CENIZA) o # Viajes (para ESCORIA)
        'D': 12,  # # de Viajes (para CENIZA) o Destino (para ESCORIA)
        'E': 20,  # Tipo de Vehículo (para CENIZA) o Tipo de Vehículo (para ESCORIA)
        'F': 20,  # Destino (para CENIZA) o Valor Unitario (para ESCORIA)
        'G': 15,  # Valor Unitario (para CENIZA) o Valor Total (para ESCORIA)
        'H': 15   # Valor Total (para CENIZA)
    }
    
    for column_letter, width in column_widths_subtabla.items():
        ws_subtabla.column_dimensions[column_letter].width = width
        
    # Guardar el archivo
    wb.save(output_file)
     
    return total_valor_principal, total_valor_subtabla