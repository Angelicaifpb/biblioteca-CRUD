from app.models.autor_model import AutorModel
from app.repository.autor_repository import AutorRepository
from app.repository.livro_repository import LivroRepository

class AutorService:
    def __init__(self):
        self.autor_repository = AutorRepository()
        self.livro_repository = LivroRepository()

    def get_all_autores(self):
        return self.autor_repository.get_all_autores()

    def create_autor(self, autor: AutorModel):
        if autor.get_id() is not None:
            raise ValueError("ID do autor deve ser vazio ao criar.")

        if not autor.get_nome() or autor.get_nome().strip() == "":
            raise ValueError("Nome do autor não pode estar vazio.")

        if any(char.isdigit() for char in autor.get_nome()):
            raise ValueError("O nome do autor não pode conter números.")

        if autor.get_nacionalidade() is not None and any(char.isdigit() for char in autor.get_nacionalidade()):
            raise ValueError("Nacionalidade não pode conter números.")

        return self.autor_repository.create_autor(autor)

    def get_autor_by_id(self, id):
        if id is None:
            raise ValueError("ID do autor não pode estar vazio.")
        return self.autor_repository.get_autor_by_id(id)

    def update_autor(self, autor: AutorModel):
        if autor.get_id() is None:
            raise ValueError("ID do autor não pode estar vazio para atualização.")

        if not autor.get_nome() or autor.get_nome().strip() == "":
            raise ValueError("Nome do autor não pode estar vazio.")

        if any(char.isdigit() for char in autor.get_nome()):
            raise ValueError("O nome do autor não pode conter números.")

        if autor.get_nacionalidade() and any(char.isdigit() for char in autor.get_nacionalidade()):
            raise ValueError("Nacionalidade não pode conter números.")

        return self.autor_repository.update_autor(autor)

    def delete_autor(self, id):
        if id is None:
            raise ValueError("ID do autor não pode estar vazio para exclusão.")

        livros = self.livro_repository.get_livros_by_autor(id)
        if livros:
            raise Exception("Não é possível deletar o autor pois ele possui livros associados.")

        return self.autor_repository.delete_autor(id)
