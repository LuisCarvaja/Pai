# backend.Dockerfile

FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos del backend
COPY ../backend /app

# Instalar dependencias
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Exponer puerto de Django
EXPOSE 8000

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
