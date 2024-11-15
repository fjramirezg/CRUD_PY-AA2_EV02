from flask import Flask
from controllers.item_controller import item_blueprint
import os

app = Flask(__name__, template_folder=os.path.join("views", "templates"))

# Registro del blueprint (controlador)
app.register_blueprint(item_blueprint)

if __name__ == "__main__":
    # Ejecutar la aplicación con modo de depuración habilitado
    app.run(debug=True)
