# frontend.Dockerfile

FROM node:20

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos del frontend
COPY ../frontend /app

# Instalar dependencias y construir (para Vite o React CRA)
RUN npm install

# Exponer puerto de desarrollo
EXPOSE 3000

# Comando por defecto
CMD ["npm", "run", "dev"]
