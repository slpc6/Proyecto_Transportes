# ============================
# 1. Etapa de compilación
# ============================
FROM node:18-alpine AS build

# Establecer directorio de trabajo
WORKDIR /opt

# Copiar package.json y package-lock.json
COPY . .

# Instalar dependencias
RUN npm install \
    && npm install -g serve \
    && npm run build

EXPOSE 4173

# Iniciar Nginx
CMD ["serve", "-s", "dist", "-l", "4173"]
