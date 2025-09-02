# 🚀 Instrucciones para Ejecutar Excel Formatter

## 📋 Requisitos Previos

Antes de ejecutar la aplicación, asegúrate de tener instalado:

- **Python 3.8+** - [Descargar desde python.org](https://python.org)
- **Node.js 16+** - [Descargar desde nodejs.org](https://nodejs.org)
- **npm** (viene con Node.js)

## 🔧 Configuración Inicial

### 1. Crear el Entorno Virtual de Python

Si es la primera vez que ejecutas la aplicación, necesitas crear el entorno virtual:

```bash
cd api
python -m venv venv
```

### 2. Instalar Dependencias del Frontend

```bash
cd frontend
npm install
```

## 🚀 Ejecutar la Aplicación

### Opción 1: Script de PowerShell (Recomendado)

1. **Haz clic derecho** en `start_app.ps1`
2. Selecciona **"Ejecutar con PowerShell"**
3. Si aparece un error de políticas de ejecución, ejecuta en PowerShell como administrador:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

### Opción 2: Script de Batch

1. **Haz doble clic** en `start_app.bat`
2. O ejecuta desde Command Prompt:
   ```cmd
   start_app.bat
   ```

### Opción 3: Ejecución Manual

Si prefieres ejecutar manualmente:

#### Backend (Terminal 1):
```bash
cd api
venv\Scripts\activate
python src\main.py
```

#### Frontend (Terminal 2):
```bash
cd frontend
npm run build
npm run preview
```

## 🌐 Acceso a la Aplicación

Una vez ejecutada, podrás acceder a:

- **Frontend**: http://localhost:4173
- **Backend API**: http://localhost:8000
- **Documentación API**: http://localhost:8000/docs

## 🛑 Detener la Aplicación

- **Scripts automáticos**: Cierra las ventanas de PowerShell/Command Prompt
- **Ejecución manual**: Presiona `Ctrl+C` en cada terminal

## 🔍 Solución de Problemas

### Error: "El entorno virtual no existe"
```bash
cd api
python -m venv venv
```

### Error: "Python no está instalado"
- Descarga e instala Python desde [python.org](https://python.org)
- Asegúrate de marcar "Add Python to PATH" durante la instalación

### Error: "Node.js no está instalado"
- Descarga e instala Node.js desde [nodejs.org](https://nodejs.org)
- Reinicia la terminal después de la instalación

### Error: "Puerto ya en uso"
- Cierra otras aplicaciones que puedan estar usando los puertos 8000 o 4173
- O cambia los puertos en los archivos de configuración

### Error: "Dependencias no encontradas"
```bash
# Para Python
cd api
venv\Scripts\activate
pip install -r requirements.txt

# Para Node.js
cd frontend
npm install
```

## 📁 Estructura del Proyecto

```
Excel_formater/
├── api/                    # Backend en FastAPI
│   ├── venv/              # Entorno virtual de Python
│   ├── src/main.py        # Punto de entrada del backend
│   └── requirements.txt   # Dependencias de Python
├── frontend/              # Frontend en React + Vite
│   ├── src/               # Código fuente
│   ├── dist/              # Versión compilada (se genera automáticamente)
│   └── package.json       # Dependencias de Node.js
├── start_app.ps1          # Script de PowerShell
├── start_app.bat          # Script de Batch
└── INSTRUCCIONES_EJECUCION.md  # Este archivo
```

## 🆘 Soporte

Si encuentras problemas:

1. Verifica que todos los requisitos estén instalados
2. Asegúrate de que los puertos 8000 y 4173 estén libres
3. Revisa los mensajes de error en la consola
4. Intenta ejecutar los comandos manualmente para identificar el problema

## 🔄 Reiniciar la Aplicación

Para reiniciar la aplicación:

1. Cierra todas las ventanas de terminal
2. Ejecuta nuevamente el script `start_app.ps1` o `start_app.bat`

---

¡Disfruta usando Excel Formatter! 🎉
