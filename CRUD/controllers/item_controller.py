from flask import Blueprint, render_template, request, redirect, url_for
from models.item_model import ItemModel

# Definimos un blueprint para agrupar las rutas
item_blueprint = Blueprint("items", __name__)

# Inicializamos la base de datos al cargar el controlador
ItemModel.initialize_db()

# Ruta principal que muestra todos los registros
@item_blueprint.route("/")
def index():
    items = ItemModel.get_all()
    return render_template("index.html", items=items)

# Ruta para crear un nuevo registro
@item_blueprint.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form.get("name")
        ItemModel.create(name)
        return redirect(url_for("items.index"))
    return render_template("create.html")

# Ruta para editar un registro existente
@item_blueprint.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit(item_id):
    item = ItemModel.get_by_id(item_id)
    if request.method == "POST":
        name = request.form.get("name")
        ItemModel.update(item_id, name)
        return redirect(url_for("items.index"))
    return render_template("edit.html", item=item)

# Ruta para eliminar un registro
@item_blueprint.route("/delete/<int:item_id>")
def delete(item_id):
    ItemModel.delete(item_id)
    return redirect(url_for("items.index"))
