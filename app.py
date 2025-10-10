import os
from flask import Flask
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Crear instancia de Flask
app = Flask(__name__)

# Ruta raíz
@app.route('/')
def index():
    return 'Hola Mundo, es una prueba'

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
