from app.database.connection import get_db
from app.models.autor_model import AutorModel

class AutorRepository:

    def get_all_autores(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM autores")
        rows = cursor.fetchall()
        return [
            AutorModel(id=row[0], nome=row[1], nacionalidade=row[2], data_nascimento=row[3])
            for row in rows
        ]

    def get_autor_by_id(self, autor_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM autores WHERE id=?", (autor_id,))
        row = cursor.fetchone()
        return AutorModel(id=row[0], nome=row[1], nacionalidade=row[2], data_nascimento=row[3]) if row else None

    def create_autor(self, autor):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO autores (nome, nacionalidade, data_nascimento) VALUES (?, ?, ?)",
            (autor.get_nome(), autor.get_nacionalidade(), autor.get_data_nascimento())
        )
        connection.commit()

    def update_autor(self, autor):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE autores SET nome=?, nacionalidade=?, data_nascimento=? WHERE id=?",
            (autor.get_nome(), autor.get_nacionalidade(), autor.get_data_nascimento(), autor.get_id())
        )
        connection.commit()

    def delete_autor(self, autor_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM autores WHERE id=?", (autor_id,))
        connection.commit()
