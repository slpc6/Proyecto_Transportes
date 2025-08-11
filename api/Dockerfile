# Usamos la imagen oficial de Python como base
FROM python:3.12-alpine

WORKDIR /opt/python-api

COPY . .

RUN python -m venv /opt/python-api/venv \
    && /opt/python-api/venv/bin/pip install --upgrade pip \
    && /opt/python-api/venv/bin/pip install -r requirements.txt

# Exponemos el puerto 80 para acceder a la API
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["/opt/python-api/venv/bin/python", "src/main.py"]
