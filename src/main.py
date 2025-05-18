# src/main.py
from flask import Flask
from src.utils.controller import controller_bp
from src.utils.config import APP_NAME, VERSION

app = Flask(__name__)
app.register_blueprint(controller_bp)

if __name__ == "__main__":
    print(f"Starting {APP_NAME} v{VERSION}")
    app.run(debug=True, host="127.0.0.1", port=5000)
