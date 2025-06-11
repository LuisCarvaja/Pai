#frontend.Dockerfile

FROM node:20

#Crear directorio
WORKDIR /app

#Copiar archivos 
COPY Frontend/package*.json ./

#Instalar Dependencias
RUN npm install

#Copiar todo el proyecto
COPY . .

#Exponer en el puerto 5173
EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "--port", "5173"]
