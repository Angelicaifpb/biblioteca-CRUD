from app.models.livro_model import LivroModel
from app.repository.livro_repository import LivroRepository
from app.repository.autor_repository import AutorRepository
from datetime import datetime

class LivroService:
    def __init__(self):
        self.livro_repository = LivroRepository()
        self.autor_repository = AutorRepository()

    def _validate_year(self, ano_publicacao):
        if ano_publicacao is not None:
            if not isinstance(ano_publicacao, int):
                raise ValueError("Ano de publicação deve ser um número inteiro.")
            if ano_publicacao <= 0:
                raise ValueError("Ano de publicação deve ser positivo.")
            if ano_publicacao < 1450 or ano_publicacao > datetime.now().year:
                raise ValueError("Ano de publicação deve estar entre 1450 e o ano atual.")

    def get_all_livros(self):
        return self.livro_repository.get_all_livros()

    def create_livro(self, livro: LivroModel):
        if livro.get_id() is not None:
            raise ValueError("ID do livro deve ser vazio ao criar.")
        if not livro.get_titulo() or livro.get_titulo().strip() == "":
            raise ValueError("Título do livro não pode estar vazio.")
        if livro.get_titulo().isdigit():
            raise ValueError("Título do livro não pode conter apenas números.")
        self._validate_year(livro.get_ano_publicacao())
        if livro.get_autor_id() is None:
            raise ValueError("Autor do livro deve ser informado.")
        autor = self.autor_repository.get_autor_by_id(livro.get_autor_id())
        if autor is None:
            raise ValueError("Autor informado não existe.")
        genero = livro.get_genero() or ""
        if any(char.isdigit() for char in genero):
            raise ValueError("Gênero do livro não pode conter números.")
        return self.livro_repository.create_livro(livro)

    def get_livro_by_id(self, id):
        if id is None:
            raise ValueError("ID do livro não pode estar vazio.")
        return self.livro_repository.get_livro_by_id(id)

    def update_livro(self, livro: LivroModel):
        if livro.get_id() is None:
            raise ValueError("ID do livro não pode estar vazio para atualização.")

        if not livro.get_titulo() or livro.get_titulo().strip() == "":
            raise ValueError("Título do livro não pode estar vazio.")

        if livro.get_titulo().isdigit():
            raise ValueError("Título do livro não pode conter apenas números.")

        genero = livro.get_genero() or ""
        if any(char.isdigit() for char in genero):
            raise ValueError("Gênero do livro não pode conter números.")

        self._validate_year(livro.get_ano_publicacao())

        if livro.get_autor_id() is None:
            raise ValueError("Autor do livro deve ser informado.")

        autor = self.autor_repository.get_autor_by_id(livro.get_autor_id())
        if autor is None:
            raise ValueError("Autor informado não existe.")

        return self.livro_repository.update_livro(livro)

    def delete_livro(self, id):
        if id is None:
            raise ValueError("ID do livro não pode estar vazio para exclusão.")
        return self.livro_repository.delete_livro(id)
