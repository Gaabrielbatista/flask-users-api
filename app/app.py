from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

app = Flask(__name__)
cors = CORS(app)

from routes.user_routes import *

# Parar de ordenar
app.json.sort_keys = False

load_dotenv()

if __name__ == "__main__":
    app.run(debug=True, port=os.getenv('PORT'), load_dotenv=True)
