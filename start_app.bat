@echo off
chcp 65001 >nul
title Excel Formatter - Iniciador de Aplicación

echo 🚀 Iniciando Excel Formatter...
echo.

REM Cambiar al directorio de la API
echo 📁 Cambiando al directorio de la API...
cd api

REM Verificar si el entorno virtual existe
if not exist "venv" (
    echo ❌ Error: El entorno virtual no existe en api/venv/
    echo Por favor, crea el entorno virtual ejecutando: python -m venv venv
    pause
    exit /b 1
)

REM Activar el entorno virtual
echo 🔧 Activando entorno virtual...
call venv\Scripts\activate.bat

REM Verificar si las dependencias están instaladas
if not exist "venv\Lib\site-packages\fastapi" (
    echo 📦 Instalando dependencias de Python...
    pip install -r requirements.txt
)

REM Iniciar el backend en segundo plano
echo 🚀 Iniciando el backend (FastAPI)...
start "Backend - FastAPI" cmd /k "cd /d %CD% && venv\Scripts\activate.bat && python src\main.py"

REM Esperar a que el backend esté listo
echo ⏳ Esperando a que el backend esté listo...
timeout /t 5 /nobreak >nul

REM Cambiar al directorio del frontend
echo 📁 Cambiando al directorio del frontend...
cd ..\frontend

REM Verificar si las dependencias del frontend están instaladas
if not exist "node_modules" (
    echo 📦 Instalando dependencias del frontend...
    npm install
)

REM Construir el frontend si no existe la carpeta dist
if not exist "dist" (
    echo 🔨 Construyendo el frontend...
    npm run build
)

REM Iniciar el servidor de preview del frontend
echo 🌐 Iniciando el frontend...
start "Frontend - Vite Preview" cmd /k "cd /d %CD% && npm run preview"

REM Esperar a que el frontend esté listo
echo ⏳ Esperando a que el frontend esté listo...
timeout /t 5 /nobreak >nul

REM Volver al directorio raíz
cd ..

echo.
echo 🎉 ¡Aplicación iniciada exitosamente!
echo 📱 Backend: http://localhost:8000
echo 🌐 Frontend: http://localhost:4173
echo 📚 Documentación de la API: http://localhost:8000/docs
echo.
echo 💡 Para detener la aplicación, cierra las ventanas de Command Prompt
echo 🔄 Para reiniciar, ejecuta este script nuevamente
echo.
echo Presiona cualquier tecla para salir...
pause >nul
