# Imagen base
FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del backend
COPY . .

# Exponer el puerto de FastAPI
EXPOSE 8000

# Comando de arranque
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
