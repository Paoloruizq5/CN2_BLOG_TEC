FROM python:3.12.2-alpine3.21

# Instala dependencias del sistema si las necesitas
# RUN apk add --no-cache gcc musl-dev libffi-dev

WORKDIR /app

# Copia solo requirements primero (mejor caché)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Ahora copia el resto del código
COPY . .

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
