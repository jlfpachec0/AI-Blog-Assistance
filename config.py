import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

# Acceder a las variables de entorno
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")
DEBUG = os.getenv("DEBUG")

# Verificar que las variables se han cargado correctamente
print(f"🔑 OpenAI API Key: {OPENAI_API_KEY}")
print(f"🗄️ MongoDB URI: {MONGODB_URI}")
print(f"🐞 Debug Mode: {DEBUG}")
