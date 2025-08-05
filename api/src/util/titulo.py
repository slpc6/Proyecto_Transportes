from datetime import datetime, timedelta

def obtener_mes_anterior():
    """Obtiene el mes anterior al actual en español"""
    hoy = datetime.now()
    primer_dia_mes_actual = hoy.replace(day=1)
    ultimo_dia_mes_anterior = primer_dia_mes_actual - timedelta(days=1)
    mes_anterior = ultimo_dia_mes_anterior.month
    año_actual = hoy.year
    
    meses = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    
    return meses[mes_anterior], año_actual

def generar_titulo(tipo_material):
    """Genera el título dinámico para el archivo Excel según el tipo de material"""
    mes_anterior, año_actual = obtener_mes_anterior()
    
    # Diccionario de títulos según el tipo de material
    titulos = {
        'ceniza': f"Enka de Colombia relacion transporte de Ceniza mes de {mes_anterior} del {año_actual}",
        'escoria': f"Enka de Colombia relacion transporte de Escoria mes de {mes_anterior} del {año_actual}",
        'interno': f"Enka de Colombia relacion transporte de Interno mes de {mes_anterior} del {año_actual}",
        'lodo': f"Enka de Colombia relacion transporte de Lodo mes de {mes_anterior} del {año_actual}"
    }
    
    return titulos.get(tipo_material.lower(), f"Enka de Colombia relacion transporte de {tipo_material.title()} mes de {mes_anterior} del {año_actual}")