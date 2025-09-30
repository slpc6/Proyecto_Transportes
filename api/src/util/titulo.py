"""Modulo para generar el titulo de las talbas"""

from datetime import datetime


def obtener_fecha() -> str:
    """Obtiene el mes anterior al actual en español.
    :returns:
    - Retorna el mes y anno actual.

    """
    hoy = datetime.now()
    mes = hoy.month
    anno = hoy.year
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    
    return meses[mes], anno


def generar_titulo(tipo_material)-> str:
    """Genera el título dinámico para el archivo Excel según el tipo de material.
    :args:
    - tipo_materia: Formato de tabla seleccionada sengun el tipo de material.
    :returns:
    - Regresa el titulo que tendra el documento con el formato y fecha correspondiente.
    
    """
    mes_anterior, año_actual = obtener_fecha()
    

    titulos = {
        'ceniza': f"Enka de Colombia relacion transporte de Ceniza mes de {mes_anterior} del {año_actual}",
        'escoria': f"Enka de Colombia relacion transporte de Escoria mes de {mes_anterior} del {año_actual}",
        'interno': f"Enka de Colombia relacion transporte de Interno mes de {mes_anterior} del {año_actual}",
        'lodo': f"Enka de Colombia relacion transporte de Lodo mes de {mes_anterior} del {año_actual}"
    }
    
    return titulos.get(tipo_material.lower(), f"Enka de Colombia relacion transporte de {tipo_material.title()} mes de {mes_anterior} del {año_actual}")
