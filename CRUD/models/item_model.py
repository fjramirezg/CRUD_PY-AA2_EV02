import sqlite3

class ItemModel:
    # Inicializa la base de datos en memoria
    @staticmethod
    def initialize_db():
        with sqlite3.connect("data.db") as conn:
            cursor = conn.cursor()
            # Crea la tabla si no existe
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            """)
            conn.commit()

    # Obtiene todos los registros de la base de datos
    @staticmethod
    def get_all():
        with sqlite3.connect("data.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM items")
            return cursor.fetchall()

    # Crea un nuevo registro
    @staticmethod
    def create(name):
        with sqlite3.connect("data.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO items (name) VALUES (?)", (name,))
            conn.commit()

    # Obtiene un registro por ID
    @staticmethod
    def get_by_id(item_id):
        with sqlite3.connect("data.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
            return cursor.fetchone()

    # Actualiza un registro
    @staticmethod
    def update(item_id, name):
        with sqlite3.connect("data.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE items SET name = ? WHERE id = ?", (name, item_id))
            conn.commit()

    # Elimina un registro
    @staticmethod
    def delete(item_id):
        with sqlite3.connect("data.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
            conn.commit()
